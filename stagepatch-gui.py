#!/usr/bin/env python2
# filename: nsm-git-ui

import os
import argparse
from PyQt4 import QtGui, QtCore



class MainWindow(QtGui.QWidget):
    def __init__(self, repo):
        QtGui.QWidget.__init__(self)
        
        # Parse the arguments sent by the main process 
        # so that we know what we're working with
        parser = argparse.ArgumentParser()
        parser.add_argument("saveFile") # First argument (AJ-Snapshot saveFile)
        parser.add_argument("pid")      # Second argument  (AJ-Snapshot PID)
        args = parser.parse_args()

        # Convert the parsed arguments into variables
        saveFile = args.saveFile
        pid = int(args.pid)       
        # Print the stuff
        
        print "Patchbay save file is %s" % saveFile
        print "aj-snapshot pid is " 
        print pid
        


if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    if len(sys.argv) > 1:
        print sys.argv[1]
        main = MainWindow(sys.argv[1])
        main.show()
        sys.exit(app.exec_())
