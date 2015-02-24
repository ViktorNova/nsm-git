#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import subprocess
from PyQt4 import QtGui
from PyQt4 import QtCore
from subprocess import call
patchbay = 'aj-snapshot -x && catia'
cmd  	 = 'aj-snapshot -f /home/guest/SYSTEM/GLOBAL/GLOBAL-MIDI-ROUTING.xml'
cmd2 	 = 'sleep 1 && killall -HUP aj-snapshot'

class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        if not os.path:
            print "Launching patchbay"
            os.system(patchbay)
            reply = QtGui.QMessageBox.question(self, 'Overwrite Global Audio/MIDI Routing?', "Please close NSM and all auio/MIDI apps before continuing!", 
            QtGui.QMessageBox.Yes | QtGui.QMessageBox.Cancel, 
            QtGui.QMessageBox.Cancel)
        
	if reply == QtGui.QMessageBox.Yes:
		print 'Writing new global Audio/MIDI routing'
	        os.system(cmd)
		print 'Reloading daemon with new routing'
	        os.system(cmd2)
        	sys.exit(0)
	else:
		print 'echo Midi routing is unchanged'
		sys.exit(0)

def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

