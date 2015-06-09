#!/usr/bin/python
# -*- coding: utf-8 -*-

# dit bovenstaande niet aanraken, het is nodig

# let op: importeer enkel het nodige, schoolpc's zijn sceer
import sys
from PyQt4 import QtGui
from PyQt4  import QtCore

resx = 600
resy = 400

class Fourth(QtGui.QMainWindow):
    def __init__(self):
        super(Fourth, self).__init__()
        self.initUI()
    def initUI(self):

        self.lbl = QtGui.QLabel('Rohan, het is me gelukt. Dit is VIER!!!', self)
        self.lbl.resize(self.lbl.sizeHint())
        self.lbl.move(250, 120)


        # maak even menubar
        # een mooie statusbar gewoon omdat het kan
        self.statusBar().showMessage('Gereed')
        exitAction = QtGui.QAction('Exit' , self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('GEWOON OPTIEFTEN BEN ER HELEMAAL KLAAR MEE')
        exitAction.triggered.connect(QtGui.qApp.quit)

        # maak even menubar
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)
        self.resize(resx, resy)
        self.center()
        self.setWindowTitle('Overgang SLC')
        self.setWindowIcon(QtGui.QIcon('3.png'))
        # nu is het venster klaar in geheugen, projecteer naar scherm
        # pas op het laatst doen natuurlijk
        self.show()

    def center(self):

        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
