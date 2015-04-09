#!/usr/bin/env python2
# Patchbay daemon for NSM
#NSM code based on rhetr's nsm-git
#Easier stuff by Viktor Nova
import liblo, sys, os, subprocess
import atexit
from signal import signal, SIGTERM
#from subprocess import call

class StagePatch(liblo.Server):
    def __init__(self):
        """
        :rtype : object
        """
        liblo.Server.__init__(self)
        self.add_method("/reply", 'ssss', self.handshake_callback)
        self.add_method("/nsm/client/open", 'sss', self.open_callback)
        self.add_method("/nsm/client/save", None, self.save_callback)
        self.add_method("/nsm/client/show_optional_gui", None, self.show_gui_callback)
        self.add_method("/nsm/client/hide_optional_gui", None, self.hide_gui_callback)
        self.add_method("/reply", 'ss', self.server_save_callback)
        self.add_method("/error", 'sis', self.error_callback)
        self.add_method(None, None, self.fallback)

        self.session_dir = None
        self.server_saved = False
        self.exit = False
        self.app = None

        self.saveFile = None
        self.pid = None
        self.gui_pid = None

        self.NSM_URL = os.getenv('NSM_URL')
        # self.NSM_URL = "osc.udp://datakTARR:10001/" # for testing purposes
        if not self.NSM_URL:
            print "NSM_URL is not set, not running inside Non Session Manager, exiting"
            sys.exit()

        self.handshake()

        self.aj_snapshot()


    # ------------------------ AJ-Snapshot ----------------------------
    def aj_snapshot(self):
        # Sets the name of the aj-snapshot file
        self.saveFile = os.path.join(self.session_dir, 'stagepatch.xml')
        print "saveFile is %s" % (self.saveFile)

        # Attempt to create the save file if it doesn't exist
        if not os.path.isfile(self.saveFile):
            print "First run, creating new patchbay file from current MIDI and JACK connections to %s" % (self.saveFile)
            subprocess.call(["aj-snapshot", self.saveFile],
                            stdout=subprocess.PIPE,
                            preexec_fn=os.setsid)

        print "Removing existing connections"
        print "Restoring connections from" + self.saveFile
        # To do: f
        self.daemon = subprocess.Popen(["aj-snapshot", "-dx", self.saveFile],
                                       stdout=subprocess.PIPE,
                                       preexec_fn=os.setsid)
        self.pid = self.daemon.pid
        print "Started patchbay daemon with pid " + repr(self.pid)

        def cleanup(self, reason):
            print "Cleaning up.."
            print "Killing aj-snapshot system-wide"
            print "FIXME! Killing all instances of aj-snapshot is a dity hack and NOT the solution!"

            #    if self.pid:
            #        print "aj-snapshot is running"
            #    else:
            #        print "aj-snapshot AINT running"
            #    if self.app.pid:
            #        print "GUI is running"
            #    else:
            #        print "GUI AINT running"

            # FIX THIS!!! FIX THIS!!! FIX THIS!!!
            os.system('killall -KILL aj-snapshot')

            sys.exit()

        signal(SIGTERM, cleanup)

    # ---------------------------------------------------------------------
    # callbacks

    def handshake_callback(self, path, args):
        print 'received handshake'

    def open_callback(self, path, args):
        self.session_dir, self.display_name, self.client_id = args
        self.session_dir = os.path.split(self.session_dir)[0]
        self.save()
        message = liblo.Message('/reply', "/nsm/client/open", 'done')
        liblo.send(self.NSM_URL, message)

    def save_callback(self, path, args):
        self.server_saved = False  #Viktor changed this from false.. might need to change it back?
        message = liblo.Message('/reply', "/nsm/client/save",
                                'NOT saved - By design NSM Patchbay must be saved manually from the GUI')
        liblo.send(self.NSM_URL, message)
        print 'NOT saved - NSM Patchbay must be saved manually from the GUI'
        saved = self.save()
        msg = "Reporting patchbay as saved, regardless"
        message = liblo.Message("/nsm/client/message", 1, msg)
        liblo.send(self.NSM_URL, message)

    def server_save_callback(self, path, args):
        if args[0] == "/nsm/server/save" and args[1] == "Saved.":
            print 'server callback received.'
            self.server_saved = True

    def error_callback(self, path, args):
        if args[1] == -6:
            print 'no session open'
            self.exit = True

        # ----------------------- SHOW GUI ----------------------------------

    def show_gui_callback(self, path, args):
        if self.app:
            if self.app.poll() == 0:
                self.app = None
            else:
                print 'gui already shown'

        if not self.app:
            self.app = subprocess.Popen([os.path.join(self.executable_dir, 'stagepatch-gui.py'),
                                         self.saveFile,
                                         repr(self.pid)],
                                        stdout=subprocess.PIPE,
                                        preexec_fn=os.setsid)
            self.gui_pid = self.app.pid
            print 'Showing gui', self.gui_pid

            # Pipe all output from the GUI subprocess and show it on the console
            gui_output = iter(self.app.stdout.readline, b"")
            for line in gui_output:
                print(line)  # yield line


    def hide_gui_callback(self, path, args):
        print 'hiding gui'
        os.killpg(self.app.pid, signal.SIGTERM)
        self.app = None


    def fallback(self, path, args, types, src):
        print "got unknown message '%s' from '%s'" % (path, src.url)
        for a, t in zip(args, types):
            print "argument of type '%s': %s" % (t, a)

    # ---------------------------------------------------------------------
    # internal methods

    def handshake(self):
        application_name = "Stagepatch"
        capabilities = ":message:optional-gui:"
        executable_name = os.path.realpath(__file__)
        self.executable_dir = os.path.dirname(executable_name)
        executable_name = "nsm-patchbay.py"  # this leads to mostly correct behaviour, I don't know how to find the actual 'correct' value though
        pid = os.getpid()
        api_version_major = 1
        api_version_minor = 2

        message = liblo.Message("/nsm/server/announce", application_name, capabilities, executable_name,
                                api_version_major, api_version_minor, pid)
        liblo.send(self.NSM_URL, message)

        while not self.session_dir:
            self.recv()
            if self.exit:
                sys.exit()

    # ---------------------------------------------------------------------
    # save methods

    def init_repo(self):
        print "FIXME: def init_repo(self) is being called"
        print "Move the initial stuff to here instead of the handshake"


    def save(self):
        print "Fix me: def save is being called."
        print "This happens when NSM asks the client to save, which is good, but it also happens when NSM opens for the first time, which makes sense for the code I forked this from, but not for typical stuff"
        return True

# --------------------- CLEANUP ON SHUTDOWN ------------------------
try:

    stage_patch = StagePatch()
except liblo.ServerError, err:
    # Debug Quazarrr
    print "Debug Quazarrr"

    print str(err)
    # cleanup() Figure out how to call cleanup from here too, in case of an error

while True:
    stage_patch.recv(100)
