import sys
import Hvier
from PyQt4 import QtGui
from PyQt4  import QtCore

resx = 600
resy = 400

class Fifth(QtGui.QMainWindow):
    def __init__(self):
        super(Fifth, self).__init__()
        self.initUI()

    def initUI(self):
        self.lbl = QtGui.QLabel(self)
        self.lbl.move(200, 50)
        self.statusBar().showMessage('Gereed')
        exitAction = QtGui.QAction('Exit' , self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('GEWOON OPTIEFTEN BEN ER HELEMAAL KLAAR MEE')
        exitAction.triggered.connect(QtGui.qApp.quit)
        self.btnVorige = QtGui.QPushButton('Vorige', self)
        self.btnVorige.resize(self.btnVorige.sizeHint())
        self.btnVorige.move(350, 350)
        self.btnVorige.clicked.connect(hideVijf)
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)
        self.resize(resx, resy)
        self.center()
        self.setWindowTitle('Overgang SLC')
        self.setWindowIcon(QtGui.QIcon('3.png'))
        self.listCijfer()
        self.show()

    def listCijfer(self):
        from Hvier import *
        cijfersD = [float(i.text()) for i in cijfers4]
        b = sum(cijfersD)/len(cijfersD)
        if b < 6.0:
                self.lbl.setText("Helaas, je blijft zitten")


        # for x in cijfers:
        #     print x.text()

    def center(self):

        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

def hideVijf(self):
    print('Fifth, hidden')
    Hvier.Vijf.hide()
