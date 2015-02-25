#!/usr/bin/env python2
# filename: nsm-git-ui

import os
import argparse
from PyQt4 import QtGui, QtCore


class MainWindow(QtGui.QWidget):
    def __init__(self, repo):
        QtGui.QWidget.__init__(self)



if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    if len(sys.argv) > 1:
        print sys.argv[1]
        main = MainWindow(sys.argv[1])
        main.show()
        sys.exit(app.exec_())
