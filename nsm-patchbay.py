#!/usr/bin/env python2

import liblo, sys, os, time, datetime, subprocess, signal, shutil
#from subprocess import call
import git

class NSMPatchbay(liblo.Server):
    def __init__(self):
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

        self.NSM_URL = os.getenv('NSM_URL')
        
        self.NSM_URL = "osc.udp://datakTARR:15838/"
       
###      os.environ['GIT_AUTHOR_NAME'] = 'nsm-git'
###      os.environ['GIT_AUTHOR_EMAIL'] = 'noreply@nsm-git'

        if not self.NSM_URL:
           sys.exit()

        self.handshake()

        print "testing 123"

    # ---------------------------------------------------------------------
    # callbacks

    def handshake_callback(self, path, args):
        print 'received handshake'

    def open_callback(self, path, args):
        self.session_dir, self.display_name, self.client_id = args
        self.session_dir = os.path.split(self.session_dir)[0]
        print "session dir is {}".format(self.session_dir)

        print "doopie doo"
        # Sets the name of the aj-snapshot file

        saveFile = os.path.join(self.session_dir, 'stagepatch.xml')
        print "savefile is %s" % (saveFile)
        #saveFile = .join(saveFileDerp)
        subprocess.Popen("ls %s" % (saveFile),
                          stdout=subprocess.PIPE,
                          preexec_fn=os.setsid)
#        subprocess.Popen([os.path.join(self.session_dir, 'stagepatch.xml')],
#                          stdout=subprocess.PIPE,
#                          preexec_fn=os.setsid)


        print "doopie doo 2"
        #print "saveFileDerp is %s" % (saveFileDerp)
        print "doopie doo 3"
        
        # Attempt to create the save file if it doesn't exist
        if not os.path.isfile(saveFile):
            print 'Creating blank patchbay'

        #os.system('touch %s' % (saveFile))
        # Restore patchbay
        #os.system(patchbayRestore)
        
        
        self.save()
        message = liblo.Message('/reply', "/nsm/client/open", 'done')
        liblo.send(self.NSM_URL, message)

    def save_callback(self, path, args):
        s_c = datetime.datetime.now().second
        self.server_saved = False
        message = liblo.Message('/reply', "/nsm/client/save", 'NOT saved - By design NSM Patchbay must be saved manually from the GUI')
        liblo.send(self.NSM_URL, message)
        print 'NOT saved - NSM Patchbay must be saved manually from the GUI'
        while not self.server_saved:
            s_d = datetime.datetime.now().second
            if s_d - s_c > 3:
                message = liblo.Message("/nsm/client/message", 1, "nsm-git has waited long enough")
                liblo.send(self.NSM_URL, message)
                print 'nsm-git has waited long enough. saving...'
                break
            self.recv(50)

        saved = self.save()
        msg = "nsm-git has committed" if saved else "nothing for nsm-git to commit"
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

    def show_gui_callback(self, path, args):
        if self.app:
            if self.app.poll() == 0:
                self.app = None
            else:
                print 'gui already shown'

        if not self.app:
            self.app = subprocess.Popen([os.path.join(self.executable_dir, 'nsm-patchbay-ui.py'), self.session_dir],
                                         stdout=subprocess.PIPE,
                                         preexec_fn=os.setsid)
            print 'showing gui', self.app.pid

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
        application_name = "nsm-patchbay"
        capabilities = ":message:optional-gui:"
        executable_name = os.path.realpath(__file__)
        self.executable_dir = os.path.dirname(executable_name)
        executable_name = "nsm-patchbay.py" # this leads to mostly correct behaviour, I don't know how to find the actual 'correct' value though
        pid = os.getpid()
        api_version_major = 1
        api_version_minor = 2

        message = liblo.Message("/nsm/server/announce", application_name, capabilities, executable_name, api_version_major, api_version_minor, pid)
        liblo.send(self.NSM_URL, message)

        while not self.session_dir:
            self.recv()
            if self.exit:
                sys.exit()


    # ---------------------------------------------------------------------
    # save methods
        
    def init_repo(self):
        '''
        opens the existing git repository or creates a new one
        '''
        try:
            self.repo = git.Repo(self.session_dir)
            print 'opened git repo'
        except git.exc.InvalidGitRepositoryError:
            self.repo = git.Repo.init(self.session_dir)
            print 'created git repo'


    def save(self):
        
        removed = untracked = updated = False
        self.init_repo()

        if not os.path.isfile(os.path.join(self.session_dir,'.gitignore')):
            with open(os.path.join(self.session_dir,'.gitignore'), 'wb') as gitignore:
                gitignore.write('*.swp\n*.lock\n*autosave*\n.*')

        removed = self.remove_removed()

        if self.repo.is_dirty(untracked_files=True):
            print 'adding untracked files'
            untracked = self.repo.untracked_files
            self.repo.index.add(self.repo.untracked_files)

        if self.repo.git.diff(None):
            print 'adding updated files'
            updated = [diff.a_blob.path for diff in self.repo.index.diff(None)]
            self.repo.index.add(updated)

        if any((removed, untracked, updated)):
            message = 'nsm-git'
            if removed:
                message += "\n\tremoved {}".format('\n\t        '.join(removed))
            if untracked:
                message += "\n\tadded {}".format('\n\t      '.join(untracked))
            if updated:
                message += "\n\tupdated {}".format('\n\t        '.join(updated))

            try:
                self.repo.index.commit(message)
                print 'committed'
                return True
            except git.exc.GitCommandError, err:
                print str(err)
                return False
        else:
            print 'nothing to be done'
            return False


try:
    nsm_git = NSMPatchbay()
except liblo.ServerError, err:
    ## Debug Quazarrr
    print "Debug Quazarrr"
    
    print str(err)
    sys.exit()

while True:
    nsm_git.recv(100)