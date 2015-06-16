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

        # niveau
        self.lbl = QtGui.QLabel('Kies hieronder het niveau:', self)
        self.lbl.resize(self.lbl.sizeHint())
        self.lbl.move(250, 120)
        # radiobuttons
        self.rbHavo = QtGui.QRadioButton('Havo', self)
        self.rbHavo.resize(self.rbHavo.sizeHint())
        self.rbHavo.move(250, 160)
            # ath
        self.rbAth = QtGui.QRadioButton('Atheneum', self)
        self.rbAth.resize(self.rbAth.sizeHint())
        self.rbAth.move(250, 180)
            # athplus
        self.rbAthPlus = QtGui.QRadioButton('Atheneum+', self)
        self.rbAthPlus.resize(self.rbAthPlus.sizeHint())
        self.rbAthPlus.move(250, 200)
            # gymnasium
        self.rbGym = QtGui.QRadioButton('Gymnasium', self)
        self.rbGym.resize(self.rbGym.sizeHint())
        self.rbGym.move(250, 220)
        # een beetje ordenen
        self.rbNiveau = QtGui.QButtonGroup()
        self.rbNiveau.addButton(self.rbHavo, 1)
        self.rbNiveau.addButton(self.rbAth, 2)
        self.rbNiveau.addButton(self.rbAthPlus, 3)
        self.rbNiveau.addButton(self.rbGym, 4)


        # volgende-knop moet rbNiv doorgeven
        self.btnVolgende = QtGui.QPushButton('Volgende', self)
        self.btnVolgende.resize(self.btnVolgende.sizeHint()) # schat grootte knop en pas die toe
        self.btnVolgende.move(450, 350)
        self.btnVolgende.clicked.connect(self.hideTwee)
        # bij doorgeven argumenten met connect, gebruik altijd lambda
        self.btnVolgende.clicked.connect(self.showDrie)

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
        # rbNiv = self.rbNiveau
        print("huey")
        # welk niveau gekozen? open a.d.h. daarvan bijbehorende vakkendinges
        sig = self.rbNiveau.checkedId()
        if sig == -1:
            # indien niks gekozen, ook niet verder gaan
            print("niks gekozen")
        elif sig == 1: # lol havo
            from Hdrie import Third
            print("havoooo")
        elif sig == 2: # atheneum opperras
            from Adrie import Third
            print("atheneum gekozen")
        elif sig == 3: # atheneum tryhards
            from APdrie import Third
            print("atheneum+ gekozen")
        elif sig == 4: # gymnasium
            from Gdrie import Third
            print("gymnasium gekozen")


        # from drie import Third
        # print('imported, showing Drie')
        global Drie
        Drie = Third()
        while Drie:
            lol

    def hideTwee(self):
        self.hide()
