#!/usr/bin/python
# -*- coding: utf-8 -*-
# Hoi, werkt dit?
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
        # self.profielen()


    def gridUI(self):


        grid = QtGui.QGridLayout(self)

        self.label1 = QtGui.QLabel("Profielen")
        self.label2 = QtGui.QLabel("Gemeenschappelijk deel")
        self.label3 = QtGui.QLabel("Profielvakken")
        self.label4 = QtGui.QLabel("Profielkeuzevakken \n(Bij CM 2 vakken bij de andere profielen 1 vak)")
        self.label5 = QtGui.QLabel("Vrije deel(verplicht 1 vak)/ \nExtra vak(optioneel) \n(Hooguit 2 aanvinken!)")

        self.btnVolgende = QtGui.QPushButton('Volgende', self)
        self.btnVolgende.resize(self.btnVolgende.sizeHint()) # schat grootte knop en pas die toe
        self.btnVolgende.clicked.connect(self.hide)
        self.btnVolgende.clicked.connect(showVier)
        self.btnVorige = QtGui.QPushButton('Vorige', self)
        self.btnVorige.resize(self.btnVorige.sizeHint())
        self.btnVorige.clicked.connect(self.hide)
        self.btnVorige.clicked.connect(showTwee)

        grid.addWidget(self.btnVolgende, 11, 0)
        grid.addWidget(self.btnVorige, 12, 0)
        grid.addWidget(self.label1, 0, 0)
        grid.addWidget(self.label2, 1, 0)
        grid.addWidget(self.label3, 2, 0)
        grid.addWidget(self.label4, 4, 0)
        grid.addWidget(self.label5, 7, 0)

        self.label6 = QtGui.QLabel(" Ne \n\n En \n\n Re \n\n Ma \n\n CKV \n\n Lo \n\n Gd")
        self.label7 = QtGui.QLabel(" Ne \n\n En \n\n Re \n\n Ma \n\n CKV \n\n Lo \n\n Gd")
        self.label8 = QtGui.QLabel(" Ne \n\n En \n\n Re \n\n Ma \n\n CKV \n\n Lo \n\n Gd")
        self.label9 = QtGui.QLabel(" Ne \n\n En \n\n Re \n\n Ma \n\n CKV \n\n Lo \n\n Gd")


        grid.addWidget(self.label6, 1, 1)
        grid.addWidget(self.label7, 1, 3)
        grid.addWidget(self.label8, 1, 5)
        grid.addWidget(self.label9, 1, 7)

        # profielen         nr_gr_1
        self.rb1 = QtGui.QRadioButton("CM")
        self.rb2 = QtGui.QRadioButton("EM")
        self.rb3 = QtGui.QRadioButton("NG")
        self.rb4 = QtGui.QRadioButton("NT")
        self.nr_gr_1 = QtGui.QButtonGroup()
        self.nr_gr_1.addButton(self.rb1, 1)
        self.nr_gr_1.addButton(self.rb2, 2)
        self.nr_gr_1.addButton(self.rb3, 3)
        self.nr_gr_1.addButton(self.rb4, 4)

        grid.addWidget(self.rb1, 0, 1)
        grid.addWidget(self.rb2, 0, 3)
        grid.addWidget(self.rb3, 0, 5)
        grid.addWidget(self.rb4, 0, 7)

        # indien gekozen

        self.rb1.clicked.connect(lambda: gekozen("PF", "CM"))
        self.rb2.clicked.connect(lambda: gekozen("PF", "EM"))
        self.rb3.clicked.connect(lambda: gekozen("PF", "NG"))
        self.rb4.clicked.connect(lambda: gekozen("PF", "NT"))

        # profielvakken     nr_gr_$PF
        #   behalve NT, daar kies je niks
            # CM
        self.rbCMFa = QtGui.QRadioButton("Fa")
        self.rbCMDu = QtGui.QRadioButton("Du")
        self.lblCMGs = QtGui.QLabel("Gs")

        #self.rbCMFa.clicked.connect(lambda: gekozen("PV", "Fa"))
        #self.rbCMDu.clicked.connect(lambda: gekozen("PV", "Du"))
            # EM
        self.rbEMWA = QtGui.QRadioButton("WA")
        self.rbEMWB = QtGui.QRadioButton("WB")
        self.lblEMEc = QtGui.QLabel("Ec")
        self.lblEMGs = QtGui.QLabel("Gs")

        #self.rbEMWA.clicked.connect(lambda: gekozen("PV", "WA"))
        #self.rbEMWB.clicked.connect(lambda: gekozen("PV", "WB"))
            # NG
        self.rbNGWA = QtGui.QRadioButton("WA")
        self.rbNGWB = QtGui.QRadioButton("WB")
        self.lblNGBi = QtGui.QLabel("Bi")
        self.lblNGSk = QtGui.QLabel("Sk")

        #self.rbNGWA.clicked.connect(lambda: gekozen("PV", "WA"))
        #self.rbNGWB.clicked.connect(lambda: gekozen("PV", "WB"))
            # NT
        self.lblNTWB = QtGui.QLabel("WB")
        self.lblNTNa = QtGui.QLabel("Na")
        self.lblNTSk = QtGui.QLabel("Sk")


            # CM
        self.nr_gr_CM = QtGui.QButtonGroup(self)
        self.nr_gr_CM.addButton(self.rbCMFa, 1)
        self.nr_gr_CM.addButton(self.rbCMDu, 2)
        grid.addWidget(self.rbCMFa,  2, 1)
        grid.addWidget(self.rbCMDu,  2, 2)
        grid.addWidget(self.lblCMGs, 3, 1)
            # EM
        self.nr_gr_EM = QtGui.QButtonGroup(self)
        self.nr_gr_EM.addButton(self.rbEMWA, 1)
        self.nr_gr_EM.addButton(self.rbEMWB, 2)
        grid.addWidget(self.lblEMEc, 3, 3)
        grid.addWidget(self.lblEMGs, 3, 4)
        grid.addWidget(self.rbEMWA,  2, 3)
        grid.addWidget(self.rbEMWB,  2, 4)
            # NG
        self.nr_gr_NG = QtGui.QButtonGroup(self)
        self.nr_gr_NG.addButton(self.rbNGWA, 1)
        self.nr_gr_NG.addButton(self.rbNGWB, 2)
        grid.addWidget(self.rbNGWA, 2,  5)
        grid.addWidget(self.rbNGWB, 2,  6)
        grid.addWidget(self.lblNGBi,3,  5)
        grid.addWidget(self.lblNGSk,3,  6)
            # NT
        grid.addWidget(self.lblNTWB, 2, 7)
        grid.addWidget(self.lblNTNa, 3, 7)
        grid.addWidget(self.lblNTSk, 3, 8)

        self.rbCMFa.clicked.connect(lambda: gekozen("PV", "Fa"))
        self.rbCMDu.clicked.connect(lambda: gekozen("PV", "Du"))
        self.rbEMWA.clicked.connect(lambda: gekozen("PV", "WA"))
        self.rbEMWB.clicked.connect(lambda: gekozen("PV", "WB"))
        self.rbNGWA.clicked.connect(lambda: gekozen("PV", "WA"))
        self.rbNGWB.clicked.connect(lambda: gekozen("PV", "WB"))



        # profielkeuzevakken    pr_gr_$PF
            # CM
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
        qr_gr_CM.addButton(self.rbCMTe,  3)
        grid.addWidget(self.rbCMAk, 4, 1)
        grid.addWidget(self.rbCMEc, 4, 2)
        grid.addWidget(self.rbCMFa2,5, 1)
        grid.addWidget(self.rbCMDu2,5, 2)
        grid.addWidget(self.rbCMTe, 6, 1)

            # EM
        self.rbEMDu = QtGui.QRadioButton("Du")
        self.rbEMFa = QtGui.QRadioButton("Fa")
        self.rbEMAk = QtGui.QRadioButton("Ak")
        self.rbEMMo = QtGui.QRadioButton("MO")
        pr_gr_EM = QtGui.QButtonGroup(self)
        pr_gr_EM.addButton(self.rbEMDu, 1)
        pr_gr_EM.addButton(self.rbEMFa, 2)
        pr_gr_EM.addButton(self.rbEMAk, 3)
        pr_gr_EM.addButton(self.rbEMMo, 4)
        grid.addWidget(self.rbEMDu, 4, 3)
        grid.addWidget(self.rbEMFa, 4, 4)
        grid.addWidget(self.rbEMAk, 5, 3)
        grid.addWidget(self.rbEMMo, 5, 4)

            # NG
        self.rbNGAk = QtGui.QRadioButton("Ak")
        self.rbNGNa = QtGui.QRadioButton("Na")
        pr_gr_NG = QtGui.QButtonGroup(self)
        pr_gr_NG.addButton(self.rbNGAk, 1)
        pr_gr_NG.addButton(self.rbNGNa, 2)
        grid.addWidget(self.rbNGAk, 4, 5)
        grid.addWidget(self.rbNGNa, 5, 5)

            # NT
        self.rbNTBi = QtGui.QRadioButton("Bi")
        self.rbNTIn = QtGui.QRadioButton("In")
        pr_gr_NT = QtGui.QButtonGroup(self)
        pr_gr_NT.addButton(self.rbNTBi, 1)
        pr_gr_NT.addButton(self.rbNTIn, 2)
        grid.addWidget(self.rbNTBi, 4, 7)
        grid.addWidget(self.rbNTIn, 5, 7)


        self.rbCMAk.clicked.connect(lambda: gekozen("PKV", "Ak"))
        self.rbCMEc.clicked.connect(lambda: gekozen("PKV", "Ec"))
        self.rbCMFa2.clicked.connect(lambda: gekozen("PKV", "Fa"))
        self.rbCMDu2.clicked.connect(lambda: gekozen("PKV", "Du"))
        self.rbCMTe.clicked.connect(lambda: gekozen("PKV", "Te"))
        self.rbEMDu.clicked.connect(lambda: gekozen("PKV", "Du"))
        self.rbEMFa.clicked.connect(lambda: gekozen("PKV", "Fa"))
        self.rbEMAk.clicked.connect(lambda: gekozen("PKV", "Ak"))
        self.rbEMMO.clicked.connect(lambda: gekozen("PKV", "MO"))
        self.rbNGAk.clicked.connect(lambda: gekozen("PKV", "Ak"))
        self.rbNGNa.clicked.connect(lambda: gekozen("PKV", "Na"))
        self.rbNTBi.clicked.connect(lambda: gekozen("PKV", "Bi"))
        self.rbNTIn.clicked.connect(lambda: gekozen("PKV", "In"))

        # self.rbEM.clicked.connect()



        # Vrije deel/extra vak
            # CM
        self.rbCMWA = QtGui.QCheckBox("WA")
        self.rbCMFa3 = QtGui.QCheckBox("Fa")
        self.rbCMDu3 = QtGui.QCheckBox("Du")
        self.rbCMAk2 = QtGui.QCheckBox("Ak")
        self.rbCMTe2 = QtGui.QCheckBox("Te")
        self.rbCMEc2 = QtGui.QCheckBox("Ec")
        self.rbCMMo = QtGui.QCheckBox("MO")
        self.rbCMIn = QtGui.QCheckBox("In")
        grid.addWidget(self.rbCMWA,  7,1)
        grid.addWidget(self.rbCMFa3, 7,2)
        grid.addWidget(self.rbCMDu3, 8,1)
        grid.addWidget(self.rbCMAk2, 8,2)
        grid.addWidget(self.rbCMTe2, 9,1)
        grid.addWidget(self.rbCMEc2, 9,2)
        grid.addWidget(self.rbCMMo, 10,1)
        grid.addWidget(self.rbCMIn, 10,2)

            # EM
        self.rbEMDu2 = QtGui.QCheckBox("Du")
        self.rbEMMo2 = QtGui.QCheckBox("MO")
        self.rbEMFa2 = QtGui.QCheckBox("Fa")
        self.rbEMIn = QtGui.QCheckBox("In")
        self.rbEMTe = QtGui.QCheckBox("Te")
        self.rbEMBi = QtGui.QCheckBox("Bi")
        self.rbEMAk2 = QtGui.QCheckBox("Ak")
        grid.addWidget(self.rbEMDu2, 7, 3)
        grid.addWidget(self.rbEMMo2, 7, 4)
        grid.addWidget(self.rbEMFa2, 8, 3)
        grid.addWidget(self.rbEMIn,  8, 4)
        grid.addWidget(self.rbEMTe,  9, 3)
        grid.addWidget(self.rbEMBi,  9, 4)
        grid.addWidget(self.rbEMAk2, 10,3)

            # NG
        self.rbNGFa = QtGui.QCheckBox("Fa")
        self.rbNGEc = QtGui.QCheckBox("Ec")
        self.rbNGDu = QtGui.QCheckBox("Du")
        self.rbNGTe = QtGui.QCheckBox("Te")
        self.rbNGAk2 = QtGui.QCheckBox("Ak")
        self.rbNGIn = QtGui.QCheckBox("In")
        self.rbNGNa2 = QtGui.QCheckBox("Na")
        grid.addWidget(self.rbNGFa, 7, 5)
        grid.addWidget(self.rbNGEc, 7, 6)
        grid.addWidget(self.rbNGDu, 8, 5)
        grid.addWidget(self.rbNGTe, 8, 6)
        grid.addWidget(self.rbNGAk2,9, 5)
        grid.addWidget(self.rbNGIn, 9, 6)
        grid.addWidget(self.rbNGNa2,10,5)

            # NT
        self.rbNTFa2 = QtGui.QCheckBox("Fa")
        self.rbNTEc = QtGui.QCheckBox("Ec")
        self.rbNTDu2 = QtGui.QCheckBox("Du")
        self.rbNTTe = QtGui.QCheckBox("Te")
        self.rbNTAk = QtGui.QCheckBox("Ak")
        self.rbNTIn2 = QtGui.QCheckBox("In")
        self.rbNTBi2 = QtGui.QCheckBox("Bi")
        grid.addWidget(self.rbNTFa2, 7, 7)
        grid.addWidget(self.rbNTEc, 7, 8)
        grid.addWidget(self.rbNTDu2, 8, 7)
        grid.addWidget(self.rbNTTe, 8, 8)
        grid.addWidget(self.rbNTAk,9, 7)
        grid.addWidget(self.rbNTIn2, 9, 8)
        grid.addWidget(self.rbNTBi2,10,7)
        self.setLayout(grid)
        self.show()
        self.btnVolgende.clicked.connect(self.hide)
        self.btnVolgende.clicked.connect(showVier)

    # def profielen(self):
    #
    #     sigma = self.nr_gr_1.checkedId()
    #     if sigma == -1:
    #         print("niks gekozen")
    #         return("niks")
    #     elif sigma == 1:
    #         print("CM gekozen")
    #         return("CM")
    #     elif sigma == 2:
    #         print("EM gekozen")
    #         return("EM")
    #     elif sigma == 3:
    #         print("NG gekozen")
    #         return("NG")
    #     elif sigma == 4:
    #         print("NT gekozen")
    #         return("NT")
    # #def PV (self):
    #
    #     #rho = self.nr_gr_CM


def gekozen(soort, antw):
    if not Geweest:
        global gekVKV
        gekVKV = []
        global Geweest
        Geweest = True
    if soort == "PV":
        global gekPV
        gekPV = antw
        print(gekPV)
    elif soort == "PKV":
        if gekPV == "CM":   #pretpakketters mogen er 2 kiezen
            if gekPKV2:
                pass    #je mag er maar 2
            elif gekPKV1:
                global gekPKV2
                gekPKV2 = antw
                print(gekPKV2)
        else:
            global gekPKV1
            gekPKV1 = antw
            print(gekPKV1)
    elif soort == "VKV":
        if antw in gekVKV:
            gekVKV.pop(antw)
        else:
            gekVKV.append(antw)



def showVier():
    # zie Readme.md
    vakGem = ["Ne", "En", "Re", "Ma", "CKV", "Lo", "Gd"]
    # profielvakken                     vakPV
    #vakPV  =
    from Hvier import Fourth
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
