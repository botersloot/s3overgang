#!/usr/bin/python
# -*- coding: utf-8 -*-

# dit bovenstaande niet aanraken, het is nodig

# let op: importeer enkel het nodige, schoolpc's zijn sceer
import sys
from PyQt4 import QtGui
from PyQt4 import QtCore

resx = 600
resy = 400

# dit is onze hoofdwindow
class venster(QtGui.QMainWindow):

    # indien nonexistent, maak zelf zelf aan en ga verder met initUI()
    def __init__(self):
        super(venster, self).__init__()
        self.initUI()

    # het creeren van de GUI gaat altijd via initUI()
    def initUI(self):

        self.btnVolgende = QtGui.QPushButton('Volgende', self)
        self.btnVolgende.resize(self.btnVolgende.sizeHint()) # schat grootte knop en pas die toe
        self.btnVolgende.move(450, 350)
        self.btnVolgende.clicked.connect(self.hideTwee)
        self.btnVolgende.clicked.connect(self.showDrie)



        self.lbl = QtGui.QLabel('Kies hieronder het niveau:', self)
        self.lbl.resize(self.lbl.sizeHint())
        self.lbl.move(250, 120)


        #radiobuttons
        self.rbtn1 = QtGui.QRadioButton('Havo', self)
        self.rbtn1.resize(self.rbtn1.sizeHint())
        self.rbtn1.move(250, 160)

        self.rbtn2 = QtGui.QRadioButton('Atheneum', self)
        self.rbtn2.resize(self.rbtn2.sizeHint())
        self.rbtn2.move(250, 180)

        self.rbtn3 = QtGui.QRadioButton('Atheneum+', self)
        self.rbtn3.resize(self.rbtn3.sizeHint())
        self.rbtn3.move(250, 200)

        self.rbtn4 = QtGui.QRadioButton('Gymnasium', self)
        self.rbtn4.resize(self.rbtn4.sizeHint())
        self.rbtn4.move(250, 220)

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

         # centreer venster tov scherm
    def center(self):

        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


    def showDrie(self):
        from drie import Third
        print('imported, showing Drie')
        global Drie
        Drie = Third()
        while Drie:
            lol

    def hideTwee(self):
        self.hide()
