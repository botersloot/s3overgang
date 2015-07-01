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
        from Hvier import VakkenS
        self.btnVorige = QtGui.QPushButton('Vorige', self)
        self.btnVorige.resize(self.btnVorige.sizeHint())
        self.btnVorige.move(350, 350)
        self.btnVorige.clicked.connect(showVier)
        self.btnVorige.clicked.connect(hideVijf)
        VakkenD = [float(i) for i in VakkenS]
        Avgvakken = sum(VakkenD)/len(VakkenD)
        self.avglbl = QtGui.QLabel(round(Avgvakken), self)
        self.avglbl.resize(self.lbl.sizeHint())
        self.avglbl.move(200, 50)

def showVier(self):
    from Hvier import Fourth
    print('imported, showing Drie')
    global Vier
    Vier = Fourth()


def hideVijf(self):
    print('Fifth, hidden')
    Hvier.Vijf.hide()
