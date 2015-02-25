#!/usr/bin/env python2
# filename: nsm-git-ui

import os
import argparse
from PyQt4 import QtGui, QtCore



class MainWindow(QtGui.QWidget):
    def __init__(self, repo):
        QtGui.QWidget.__init__(self)
        
        parser = argparse.ArgumentParser()
        parser.add_argument("saveFile") # Second argument (AJ-Snapshot saveFile)
        parser.add_argument("pid")      # Third argument  (AJ-Snapshot PID)
        args = parser.parse_args()
        print "Patchbay save file is %s" % args.saveFile
        print "aj-snapshot pid is %s" % args.pid
        


if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    if len(sys.argv) > 1:
        print sys.argv[1]
        main = MainWindow(sys.argv[1])
        main.show()
        sys.exit(app.exec_())
