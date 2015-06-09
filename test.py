import sys
from PyQt4 import QtGui
from PyQt4 import QtCore



class gridlayout_example(QtGui.QWidget):
    def __init__(self):
        super(gridlayout_example, self).__init__()
    def func(self):
        layout=QtGui.QHBoxLayout()  # layout for the central widget
        widget=QtGui.QWidget(self)  # central widget
        widget.setLayout(layout)

        number_group=QtGui.QButtonGroup(widget) # Number group
        r0=QtGui.QRadioButton("0")
        number_group.addButton(r0)
        r1=QtGui.QRadioButton("1")
        number_group.addButton(r1)
        layout.addWidget(r0)
        layout.addWidget(r1)

        letter_group=QtGui.QButtonGroup(widget) # Letter group
        ra=QtGui.QRadioButton("a")
        letter_group.addButton(ra)
        rb=QtGui.QRadioButton("b")
        letter_group.addButton(rb)
        layout.addWidget(ra)
        layout.addWidget(rb)

        # assign the widget to the main window
        self.setCentralWidget(widget)
        self.show()
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