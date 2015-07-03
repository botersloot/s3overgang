#!/usr/bin/python
# -*- coding: utf-8 -*-

# dit bovenstaande niet aanraken, het is nodig

# let op: importeer enkel het nodige, schoolpc's zijn sceer
import sys
import Hdrie
from PyQt4 import *


resx = 600
resy = 400

class Fourth(QtGui.QMainWindow):
    def __init__(self):
        super(Fourth, self).__init__()
        self.initUI()
    def initUI(self):

        #message

        self.lbl = QtGui.QLabel('Hier kunt u de rapportcijfers voor elk vak specifiek invullen', self)
        self.lbl.resize(self.lbl.sizeHint())
        self.lbl.move(200, 50)

        #labels

        self.lbl1 = QtGui.QLabel('Godsdienst', self)
        self.lbl1.resize(self.lbl1.sizeHint())
        self.lbl1.move(50, 100)

        self.lbl2 = QtGui.QLabel('Handvaardigheid', self)
        self.lbl2.resize(self.lbl2.sizeHint())
        self.lbl2.move(50, 120)

        self.lbl3 = QtGui.QLabel('Lichamelijke opvoeding', self)
        self.lbl3.resize(self.lbl3.sizeHint())
        self.lbl3.move(50, 140)

        self.lbl4 = QtGui.QLabel('Muziek', self)
        self.lbl4.resize(self.lbl4.sizeHint())
        self.lbl4.move(50, 160)

        self.lbl5 = QtGui.QLabel('Nederlands', self)
        self.lbl5.resize(self.lbl5.sizeHint())
        self.lbl5.move(50, 180)

        self.lbl6 = QtGui.QLabel('Engels', self)
        self.lbl6.resize(self.lbl6.sizeHint())
        self.lbl6.move(50, 200)

        self.lbl7 = QtGui.QLabel('Wiskunde', self)
        self.lbl7.resize(self.lbl7.sizeHint())
        self.lbl7.move(50, 220)

        self.lbl8 = QtGui.QLabel('Rekenen', self)
        self.lbl8.resize(self.lbl8.sizeHint())
        self.lbl8.move(50, 240)

        self.lbl9 = QtGui.QLabel('Frans', self)
        self.lbl9.resize(self.lbl9.sizeHint())
        self.lbl9.move(350, 100)

        self.lbl10 = QtGui.QLabel('Duits', self)
        self.lbl10.resize(self.lbl10.sizeHint())
        self.lbl10.move(350, 120)

        self.lbl11 = QtGui.QLabel('Natuurkunde', self)
        self.lbl11.resize(self.lbl11.sizeHint())
        self.lbl11.move(350, 140)

        self.lbl12 = QtGui.QLabel('Scheikunde', self)
        self.lbl12.resize(self.lbl12.sizeHint())
        self.lbl12.move(350, 160)

        self.lbl13 = QtGui.QLabel('Aardrijkskunde', self)
        self.lbl13.resize(self.lbl13.sizeHint())
        self.lbl13.move(350, 180)

        self.lbl14 = QtGui.QLabel('Economie', self)
        self.lbl14.resize(self.lbl14.sizeHint())
        self.lbl14.move(350, 200)

        self.lbl15 = QtGui.QLabel('Tekenen', self)
        self.lbl15.resize(self.lbl15.sizeHint())
        self.lbl15.move(350, 220)

        self.lbl16 = QtGui.QLabel('Geschiedenis', self)
        self.lbl16.resize(self.lbl16.sizeHint())
        self.lbl16.move(350, 240)

        #textbalkjes

        self.qle1 = QtGui.QLineEdit(self)
        self.qle1.resize(self.qle1.sizeHint())
        self.qle1.move(170, 100)

        self.qle2 = QtGui.QLineEdit(self)
        self.qle2.resize(self.qle2.sizeHint())
        self.qle2.move(170, 120)


        self.qle3 = QtGui.QLineEdit(self)
        self.qle3.resize(self.qle3.sizeHint())
        self.qle3.move(170, 140)


        self.qle4 = QtGui.QLineEdit(self)
        self.qle4.resize(self.qle4.sizeHint())
        self.qle4.move(170, 160)


        self.qle5 = QtGui.QLineEdit(self)
        self.qle5.resize(self.qle5.sizeHint())
        self.qle5.move(170, 180)


        self.qle6 = QtGui.QLineEdit(self)
        self.qle6.resize(self.qle6.sizeHint())
        self.qle6.move(170, 200)


        self.qle7 = QtGui.QLineEdit(self)
        self.qle7.resize(self.qle7.sizeHint())
        self.qle7.move(170, 220)


        self.qle8 = QtGui.QLineEdit(self)
        self.qle8.resize(self.qle8.sizeHint())
        self.qle8.move(170, 240)


        self.qle9 = QtGui.QLineEdit(self)
        self.qle9.resize(self.qle9.sizeHint())
        self.qle9.move(430, 100)


        self.qle10 = QtGui.QLineEdit(self)
        self.qle10.resize(self.qle10.sizeHint())
        self.qle10.move(430, 120)


        self.qle11 = QtGui.QLineEdit(self)
        self.qle11.resize(self.qle11.sizeHint())
        self.qle11.move(430, 140)


        self.qle12 = QtGui.QLineEdit(self)
        self.qle12.resize(self.qle12.sizeHint())
        self.qle12.move(430, 160)


        self.qle13 = QtGui.QLineEdit(self)
        self.qle13.resize(self.qle13.sizeHint())
        self.qle13.move(430, 180)


        self.qle14 = QtGui.QLineEdit(self)
        self.qle14.resize(self.qle14.sizeHint())
        self.qle14.move(430, 200)


        self.qle15 = QtGui.QLineEdit(self)
        self.qle15.resize(self.qle15.sizeHint())
        self.qle15.move(430, 220)


        self.qle16 = QtGui.QLineEdit(self)
        self.qle16.resize(self.qle16.sizeHint())
        self.qle16.move(430, 240)


        Godsdienst = self.qle1
        Handvaardigheid = self.qle2
        LO = self.qle3
        Muziek = self.qle4
        Nederlands = self.qle5
        Engels = self.qle6
        Wiskunde = self.qle7
        Rekenen = self.qle8
        Frans = self.qle9
        Duits = self.qle10
        Natuurkunde = self.qle11
        Scheikunde = self.qle12
        Aardrijkskunde = self.qle13
        Economie = self.qle14
        Tekenen = self.qle15
        Geschiedenis = self.qle16



        #berekenknop
        self.btnBereken = QtGui.QPushButton('Bereken', self)
        self.btnBereken.setToolTip('Berekenen')
        # schat grootte knop en pas die toe
        self.btnBereken.resize(self.btnBereken.sizeHint())
        self.btnBereken.move(450, 350)
        self.btnBereken.clicked.connect(showVijf)
        self.btnBereken.clicked.connect(hideVier)
        self.btnVorige = QtGui.QPushButton('Vorige', self)
        self.btnVorige.resize(self.btnVorige.sizeHint())
        self.btnVorige.move(350, 350)
        self.btnVorige.clicked.connect(showDrie)
        self.btnVorige.clicked.connect(hideVier)

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
        self.show()

        vakken = ['Godsdienst', 'Handvaardigheid', 'LO', 'Muziek',
        'Nederlands', 'Engels', 'Wiskunde', 'Rekenen', 'Frans', 'Duits', 'Natuurkunde',
        'Scheikunde', 'Aardrijkskunde', 'Economie',
        'Tekenen', 'Geschiedenis']
        global cijfers
        cijfers = [Godsdienst, Handvaardigheid, LO, Muziek,
        Nederlands, Engels, Wiskunde, Rekenen, Frans, Duits, Natuurkunde,
        Scheikunde, Aardrijkskunde, Economie,
        Tekenen, Geschiedenis]
        global cijfers4
        cijfers4 = [Godsdienst, Handvaardigheid, LO, Muziek]

    def center(self):

        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

def showVijf(self):

    from Hvijf import Fifth
    print('imported, showing Fifth')
    global Vijf
    Vijf = Fifth()

def showDrie(self):
    from Hdrie import Third
    print('imported, showing Drie')
    global Drie
    Drie = Third()


def hideVier(self):
    print('Fourth, hidden')
    Hdrie.Vier.hide()
