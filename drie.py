#!/usr/bin/python
# -*- coding: utf-8 -*-

# dit bovenstaande niet aanraken, het is nodig

# let op: importeer enkel het nodige, schoolpc's zijn sceer
import sys
import twee
from PyQt4 import QtGui
from PyQt4  import QtCore

resx = 600
resy = 400


class Third(QtGui.QMainWindow):
    def __init__(self):
        super(Third, self).__init__()
        self.grid = Grid()
        self.setCentralWidget(self.grid)
        self.resize(resx, resy)
        self.center()
        self.setWindowTitle('Overgang SLC')
        self.setWindowIcon(QtGui.QIcon('3.png'))
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


        self.btnVolgende = QtGui.QPushButton('Volgende', self)
        self.btnVolgende.resize(self.btnVolgende.sizeHint()) # schat grootte knop en pas die toe
        self.btnVolgende.move(450, 350)
        self.btnVolgende.clicked.connect(hideDrie)
        self.btnVolgende.clicked.connect(showVier)

        self.show()
    def center(self):

        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

class Grid(QtGui.QWidget):
    def __init__(self):
        super(Grid, self).__init__()
        self.gridUI()

    def gridUI(self):


        grid = QtGui.QGridLayout(self)

        self.label1 = QtGui.QLabel("Profielen")
        self.label2 = QtGui.QLabel("Gemeenschappelijk deel")
        self.label3 = QtGui.QLabel("Profielvakken")
        self.label4 = QtGui.QLabel("Profielkezuevakken")
        self.label5 = QtGui.QLabel("Vrije deel/ \nExtra vak")

        grid.addWidget(self.label1, 0, 0)
        grid.addWidget(self.label2, 1, 0)
        grid.addWidget(self.label3, 2, 0)
        grid.addWidget(self.label4, 3, 0)
        grid.addWidget(self.label5, 4, 0)

        self.label6 = QtGui.QLabel(" Ne \n\n En \n\n Re \n\n Ma \n\n CKV \n\n Lo \n\n Gd")
        self.label7 = QtGui.QLabel(" Ne \n\n En \n\n Re \n\n Ma \n\n CKV \n\n Lo \n\n Gd")
        self.label8 = QtGui.QLabel(" Ne \n\n En \n\n Re \n\n Ma \n\n CKV \n\n Lo \n\n Gd")
        self.label9 = QtGui.QLabel(" Ne \n\n En \n\n Re \n\n Ma \n\n CKV \n\n Lo \n\n Gd")


        grid.addWidget(self.label6, 1, 1)
        grid.addWidget(self.label7, 1, 2)
        grid.addWidget(self.label8, 1, 3)
        grid.addWidget(self.label9, 1, 4)

        # profielen
        self.rb1 = QtGui.QRadioButton("CM")
        self.rb2 = QtGui.QRadioButton("EM")
        self.rb3 = QtGui.QRadioButton("NG")
        self.rb4 = QtGui.QRadioButton("NT")
        nr_gr_1 = QtGui.QButtonGroup()
        nr_gr_1.addButton(self.rb1, 1)
        nr_gr_1.addButton(self.rb2, 2)
        nr_gr_1.addButton(self.rb3, 3)
        nr_gr_1.addButton(self.rb4, 4)

        grid.addWidget(self.rb1, 0, 1)
        grid.addWidget(self.rb2, 0, 2)
        grid.addWidget(self.rb3, 0, 3)
        grid.addWidget(self.rb4, 0, 4)

        # profielvakken
        self.cb1 = QtGui.QCheckBox("Fa")
        self.cb2 = QtGui.QCheckBox("Du")
        self.cb3 = QtGui.QCheckBox("WA")
        self.cb4 = QtGui.QCheckBox("WB")
        self.lblGs = QtGui.QLabel("Gs")

        nr_gr_2 = QtGui.QButtonGroup(self)
        nr_gr_2.addButton(self.cb1, 1)
        nr_gr_2.addButton(self.cb2, 1)
        grid.addWidget(self.lblGs, 2,1)

        nr_gr_3 = QtGui.QButtonGroup()

        hbox1 = QtGui.QHBoxLayout(self)
        hbox1.addWidget(self.cb1)
        hbox1.addWidget(self.cb2)
        hbox1.addWidget(self.cb3)
        hbox1.addWidget(self.cb4)
        grid.addLayout(hbox1, 2, 1)

        self.setLayout(grid)

        self.show()

def showVier():
    from vier import Fourth
    print('imported, showing Vier')
    Vier = Fourth()
    while Vier:
        lol


def hideDrie():
    twee.Drie.hide()
