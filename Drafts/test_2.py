from PyQt4.QtCore import * 
from PyQt4.QtGui import * 
import sys

class MyButtonGroup(QButtonGroup):
      
  @pyqtSlot(int)
  def buttonClickedSlot(self,index):
    QMessageBox.information(None,
			    "QButtonGroup Button Click!",
			    "Clicked Button Index: "+ QString.number(index))
				  
def main():    
    app 	 = QApplication(sys.argv)
    window 	 = QWidget()
    buttonGroup	 = MyButtonGroup()
    layout	 = QHBoxLayout()

    button1	 = QRadioButton("Button 1")
    button2	 = QRadioButton("Button 2")
    button3	 = QRadioButton("Button 3")

    buttonGroup.addButton(button1,1)
    buttonGroup.addButton(button2,2)
    buttonGroup.addButton(button3,3)
    
    window.setLayout(layout)
    layout.addWidget(button1)
    layout.addWidget(button2)
    layout.addWidget(button3)
    
    window.resize(250,50)    
    window.setWindowTitle('PyQt QButtonGroup Clicked Example')  
    
    QObject.connect(buttonGroup,SIGNAL("buttonClicked(int)"),
		    buttonGroup,SLOT("buttonClickedSlot(int)"))

    window.show()    
    sys.exit(app.exec_())
 
if __name__ == '__main__':
    main()