#start of button_bar.py
import sys
from PyQt5 import QtWidgets

class ButtonBar(QtWidgets.QWidget):
    
    def __init__(self, view):
        super().__init__()
        
        self.view = view
        self.initUI()
        
    def initUI(self):
        # create a horizontal layout to hold the buttons
        hbox = QtWidgets.QHBoxLayout()
        
        # create a dictionary to store the buttons
        self.buttons = {}


        # create two buttons to switch between pages
        self.buttons['Page1'] = QtWidgets.QPushButton('Page 1')
        self.buttons['Page1'].clicked.connect(lambda: self.view.stack.setCurrentIndex(0))
        hbox.addWidget(self.buttons['Page1'])

        self.buttons['Page2'] = QtWidgets.QPushButton('Page 2')
        self.buttons['Page2'].clicked.connect(lambda: self.view.stack.setCurrentIndex(1))
        hbox.addWidget(self.buttons['Page2'])
        
        # add a quit button
        self.buttons['quit'] = QtWidgets.QPushButton('Quit', self)
        self.buttons['quit'].clicked.connect(QtWidgets.QApplication.instance().quit)
        hbox.addWidget(self.buttons['quit'])

        self.setLayout(hbox)

#end of button_bar.py