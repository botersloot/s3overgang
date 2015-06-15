import sys, time
from PyQt4 import QtGui
from twee import venster
resx = 600
resy = 400
# bovenstaande dingen niet aanraken pls

def main():
    # niet aanraken
    app = QtGui.QApplication(sys.argv)
    # maak een vensterinstantie (zie class venster() )
    ex = venster()
    # als voorgaande instantie(s) afgesloten is/zijn, sluit boel af
    sys.exit(app.exec_())

# draai enkel als programma opzich gedraaid wordt (dus niet indien geimporteerd)
# het programma begint hier, hier wordt main() opgeroepen
if __name__ == '__main__':
    main()


    # bij afsluiten
    def closeEvent(self, event):

        reply = QtGui.QMessageBox.question(self, 'Message',
            "Weet u zeker dat u wilt afsluiten?", QtGui.QMessageBox.Yes |
            QtGui.QMessageBox.No, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
