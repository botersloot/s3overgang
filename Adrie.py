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
        self.label4 = QtGui.QLabel("Profielkezuevakken \n(Bij CM 2 vakken bij de andere profielen 1 vak)")
        self.label5 = QtGui.QLabel("Vrije deel(verplicht 1 vak)/ \nExtra vak(optioneel) \n(Hooguit 2 aanvinken!)")

        self.btnVolgende = QtGui.QPushButton('Volgende', self)
        self.btnVolgende.resize(self.btnVolgende.sizeHint()) # schat grootte knop en pas die toe
        self.btnVolgende.clicked.connect(hideDrie)
        self.btnVolgende.clicked.connect(showVier)
        self.btnVorige = QtGui.QPushButton('Vorige', self)
        self.btnVorige.resize(self.btnVorige.sizeHint())
        self.btnVorige.clicked.connect(hideDrie)
        self.btnVorige.clicked.connect(showTwee)

        grid.addWidget(self.btnVolgende, 11, 0)
        grid.addWidget(self.btnVorige, 12, 0)
        grid.addWidget(self.label1, 0, 0)
        grid.addWidget(self.label2, 1, 0)
        grid.addWidget(self.label3, 3, 0)
        grid.addWidget(self.label4, 5, 0)
        grid.addWidget(self.label5, 8, 0)

        self.label6 = QtGui.QLabel(" Ne \n\n En \n\n Re \n\n Gd \n\n Ma \n\n CKV \n\n ANW \n\n LO")
        self.label7 = QtGui.QLabel(" Ne \n\n En \n\n Re \n\n Gd \n\n Ma \n\n CKV \n\n ANW \n\n LO")
        self.label8 = QtGui.QLabel(" Ne \n\n En \n\n Re \n\n Gd \n\n Ma \n\n CKV \n\n ANW \n\n LO")
        self.label9 = QtGui.QLabel(" Ne \n\n En \n\n Re \n\n Gd \n\n Ma \n\n CKV \n\n ANW \n\n LO")
        grid.addWidget(self.label6, 1, 1)
        grid.addWidget(self.label7, 1, 4)
        grid.addWidget(self.label8, 1, 7)
        grid.addWidget(self.label9, 1, 9)

        self.rbCMFa = QtGui.QRadioButton("Fa")
        self.rbCMDu = QtGui.QRadioButton("Du")
        ar_gr_1 = QtGui.QButtonGroup(self)
        ar_gr_1.addButton(self.rbCMFa, 1)
        ar_gr_1.addButton(self.rbCMDu, 2)
        grid.addWidget(self.rbCMFa, 2, 1)
        grid.addWidget(self.rbCMDu, 2, 2)

        self.rbEMFa = QtGui.QRadioButton("Fa")
        self.rbEMDu = QtGui.QRadioButton("Du")
        ar_gr_2 = QtGui.QButtonGroup(self)
        ar_gr_2.addButton(self.rbEMFa, 1)
        ar_gr_2.addButton(self.rbEMDu, 2)
        grid.addWidget(self.rbEMFa, 2, 4)
        grid.addWidget(self.rbEMDu, 2, 5)

        self.rbNGFa = QtGui.QRadioButton("Fa")
        self.rbNGDu = QtGui.QRadioButton("Du")
        ar_gr_3 = QtGui.QButtonGroup(self)
        ar_gr_3.addButton(self.rbNGFa, 1)
        ar_gr_3.addButton(self.rbNGDu, 2)
        grid.addWidget(self.rbNGFa, 2, 7)
        grid.addWidget(self.rbNGDu, 2, 8)

        self.rbNTFa = QtGui.QRadioButton("Fa")
        self.rbNTDu = QtGui.QRadioButton("Du")
        ar_gr_4 = QtGui.QButtonGroup(self)
        ar_gr_4.addButton(self.rbNTFa, 1)
        ar_gr_4.addButton(self.rbNTDu, 2)
        grid.addWidget(self.rbNTFa, 2, 9)
        grid.addWidget(self.rbNTDu, 2, 10)
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
        grid.addWidget(self.rb2, 0, 4)
        grid.addWidget(self.rb3, 0, 7)
        grid.addWidget(self.rb4, 0, 9)

        # profielvakken
            # CM
        self.rbCMWC = QtGui.QRadioButton("WC")
        self.rbCMWA = QtGui.QRadioButton("WA")
        self.lblCMGs = QtGui.QLabel("Gs")
            # EM
        self.rbEMWA = QtGui.QRadioButton("WA")
        self.rbEMWB = QtGui.QRadioButton("WB")
        self.lblEMEc = QtGui.QLabel("Ec")
        self.lblEMGs = QtGui.QLabel("Gs")
            # NG
        self.rbNGWA = QtGui.QRadioButton("WA")
        self.rbNGWB = QtGui.QRadioButton("WB")
        self.lblNGBi = QtGui.QLabel("Bi")
        self.lblNGSk = QtGui.QLabel("Sk")
            # NT
        self.lblNTWB = QtGui.QLabel("WB")
        self.lblNTNa = QtGui.QLabel("Na")
        self.lblNTSk = QtGui.QLabel("Sk")
        # CM
        nr_gr_CM = QtGui.QButtonGroup(self)
        nr_gr_CM.addButton(self.rbCMWC, 1)
        nr_gr_CM.addButton(self.rbCMWA, 2)
        grid.addWidget(self.rbCMWC,  3, 1)
        grid.addWidget(self.rbCMWA,  3, 2)
        grid.addWidget(self.lblCMGs, 4, 1)



        # EM
        nr_gr_EM = QtGui.QButtonGroup(self)
        nr_gr_EM.addButton(self.rbEMWA, 1)
        nr_gr_EM.addButton(self.rbEMWB, 2)
        grid.addWidget(self.lblEMEc, 4, 4)
        grid.addWidget(self.lblEMGs, 4, 5)
        grid.addWidget(self.rbEMWA,  3, 4)
        grid.addWidget(self.rbEMWB,  3, 5)
        
        # NG
        nr_gr_NG = QtGui.QButtonGroup(self)
        nr_gr_NG.addButton(self.rbNGWA, 1)
        nr_gr_NG.addButton(self.rbNGWB, 2)
        grid.addWidget(self.rbNGWA, 3,  7)
        grid.addWidget(self.rbNGWB, 3,  8)
        grid.addWidget(self.lblNGBi,4,  7)
        grid.addWidget(self.lblNGSk,4,  8)

        # NT
        grid.addWidget(self.lblNTWB, 3, 9)
        grid.addWidget(self.lblNTNa, 4, 9)
        grid.addWidget(self.lblNTSk, 4, 10)

        # profielkeuzevakken
        #CM
        self.rbCMAk = QtGui.QRadioButton("Ak")
        self.rbCMEc = QtGui.QRadioButton("Ec")
        pr_gr_CM = QtGui.QButtonGroup(self)
        pr_gr_CM.addButton(self.rbCMAk, 1)
        pr_gr_CM.addButton(self.rbCMEc, 2)
        self.rbCMFa2 = QtGui.QRadioButton("Fa")
        self.rbCMDu2 = QtGui.QRadioButton("Du")
        self.rbCMTe = QtGui.QRadioButton("Te")
        qr_gr_CM = QtGui.QButtonGroup(self)
        qr_gr_CM.addButton(self.rbCMFa2, 1)
        qr_gr_CM.addButton(self.rbCMDu2, 2)
        grid.addWidget(self.rbCMAk, 5, 1)
        grid.addWidget(self.rbCMEc, 5, 2)
        grid.addWidget(self.rbCMFa2,6, 1)
        grid.addWidget(self.rbCMDu2,6, 2)
        grid.addWidget(self.rbCMTe, 7, 1)

        #EM
        self.rbEMDu2 = QtGui.QRadioButton("Du")
        self.rbEMFa2 = QtGui.QRadioButton("Fa")
        self.rbEMAk = QtGui.QRadioButton("Ak")
        self.rbEMMo = QtGui.QRadioButton("MO")
        pr_gr_EM = QtGui.QButtonGroup(self)
        pr_gr_EM.addButton(self.rbEMDu2, 1)
        pr_gr_EM.addButton(self.rbEMFa2, 2)
        pr_gr_EM.addButton(self.rbEMAk, 3)
        pr_gr_EM.addButton(self.rbEMMo, 4)
        grid.addWidget(self.rbEMDu2, 5, 4)
        grid.addWidget(self.rbEMFa2, 5, 5)
        grid.addWidget(self.rbEMAk, 6, 4)
        grid.addWidget(self.rbEMMo, 6, 5)

        #NG
        self.rbNGAk = QtGui.QRadioButton("Ak")
        self.rbNGNa = QtGui.QRadioButton("Na")
        pr_gr_NG = QtGui.QButtonGroup(self)
        pr_gr_NG.addButton(self.rbNGAk, 1)
        pr_gr_NG.addButton(self.rbNGNa, 2)
        grid.addWidget(self.rbNGAk, 5, 7)
        grid.addWidget(self.rbNGNa, 6, 7)

        #NT
        self.rbNTBi = QtGui.QRadioButton("Bi")
        self.rbNTIn = QtGui.QRadioButton("In")
        pr_gr_NT = QtGui.QButtonGroup(self)
        pr_gr_NT.addButton(self.rbNTBi, 1)
        pr_gr_NT.addButton(self.rbNTIn, 2)
        grid.addWidget(self.rbNTBi, 5, 9)
        grid.addWidget(self.rbNTIn, 6, 9)

        # Vrije deel/extra vak
        #CM
        self.rbCMFa3 = QtGui.QCheckBox("Fa")
        self.rbCMDu3 = QtGui.QCheckBox("Du")
        self.rbCMAk2 = QtGui.QCheckBox("Ak")
        self.rbCMTe2 = QtGui.QCheckBox("Te")
        self.rbCMEc2 = QtGui.QCheckBox("Ec")
        self.rbCMMo = QtGui.QCheckBox("MO")
        self.rbCMIn = QtGui.QCheckBox("In")
        grid.addWidget(self.rbCMFa3, 8,1)
        grid.addWidget(self.rbCMDu3, 8,2)
        grid.addWidget(self.rbCMAk2, 9,1) 
        grid.addWidget(self.rbCMTe2, 9,2)
        grid.addWidget(self.rbCMEc2,10,1)
        grid.addWidget(self.rbCMMo, 10,2)
        grid.addWidget(self.rbCMIn, 11,1)

        #EM
        self.rbEMDu3 = QtGui.QCheckBox("Du")
        self.rbEMMo2 = QtGui.QCheckBox("MO")
        self.rbEMFa3 = QtGui.QCheckBox("Fa")
        self.rbEMIn = QtGui.QCheckBox("In")
        self.rbEMTe = QtGui.QCheckBox("Te")
        self.rbEMBi = QtGui.QCheckBox("Bi")
        self.rbEMAk2 = QtGui.QCheckBox("Ak")
        grid.addWidget(self.rbEMDu3, 7, 4)
        grid.addWidget(self.rbEMMo2, 7, 5)
        grid.addWidget(self.rbEMFa3, 8, 4)
        grid.addWidget(self.rbEMIn,  8, 5) 
        grid.addWidget(self.rbEMTe,  9, 4)
        grid.addWidget(self.rbEMBi,  9, 5)
        grid.addWidget(self.rbEMAk2, 10,4)

        #NG
        self.rbNGFa2 = QtGui.QCheckBox("Fa")
        self.rbNGEc = QtGui.QCheckBox("Ec")
        self.rbNGDu2 = QtGui.QCheckBox("Du")
        self.rbNGTe = QtGui.QCheckBox("Te")
        self.rbNGAk2 = QtGui.QCheckBox("Ak")
        self.rbNGIn = QtGui.QCheckBox("In")
        self.rbNGNa2 = QtGui.QCheckBox("Na")
        grid.addWidget(self.rbNGFa2, 7, 7)
        grid.addWidget(self.rbNGEc, 7, 8)
        grid.addWidget(self.rbNGDu2, 8, 7)
        grid.addWidget(self.rbNGTe, 8, 8)
        grid.addWidget(self.rbNGAk2,9, 7)
        grid.addWidget(self.rbNGIn, 9, 8)
        grid.addWidget(self.rbNGNa2,10,7)

        #NT
        self.rbNTFa2 = QtGui.QCheckBox("Fa")
        self.rbNTEc = QtGui.QCheckBox("Ec")
        self.rbNTDu2 = QtGui.QCheckBox("Du")
        self.rbNTTe = QtGui.QCheckBox("Te")
        self.rbNTAk = QtGui.QCheckBox("Ak")
        self.rbNTIn2 = QtGui.QCheckBox("In")
        self.rbNTBi2 = QtGui.QCheckBox("Bi")
        grid.addWidget(self.rbNTFa2, 7, 9)
        grid.addWidget(self.rbNTEc, 7, 10)
        grid.addWidget(self.rbNTDu2, 8, 9)
        grid.addWidget(self.rbNTTe, 8, 10)
        grid.addWidget(self.rbNTAk,9, 9)
        grid.addWidget(self.rbNTIn2, 9, 10)
        grid.addWidget(self.rbNTBi2,10,9)

        self.setLayout(grid)

        self.show()

def showVier():
    from vier import Fourth
    print('imported, showing Vier')
    Vier = Fourth()
    while Vier:
        lol

def showTwee():
    from twee import venster
    print('imported, showing Twee')
    Twee = venster()
    while Twee:
        lol        


def hideDrie():
    twee.Drie.hide()
