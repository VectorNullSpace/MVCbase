#start of page2.py

import sys
from PyQt5 import QtWidgets
from buttonBar import ButtonBar

class Page2(QtWidgets.QWidget):
    
    def __init__(self, model, view):
        super().__init__()
        
        self.model = model
        self.view = view
        
        self.initUI()
        
    def initUI(self):
        # create a vertical layout
        vbox = QtWidgets.QVBoxLayout()


        ##implement the buttonBar(must do for every page class)
        # add widgets to the layout
        vbox.addWidget(QtWidgets.QLabel('This is page 2'))
        # create an instance of the ButtonBar class
        button_bar = ButtonBar(self.view)
        # add the ButtonBar instance to the page layout
        vbox.addWidget(button_bar)
        ##end of implementing the buttonBar

        
        # create a label to display the text
        self.lbl = QtWidgets.QLabel('', self)
        vbox.addWidget(self.lbl)
        
        # create a line edit to input the text
        self.line_edit = QtWidgets.QLineEdit(self)
        vbox.addWidget(self.line_edit)
        
        # create a button to update the text
        btn = QtWidgets.QPushButton('Update Text', self)
        btn.clicked.connect(self.update_text)
        vbox.addWidget(btn)
        
        # set the layout of the page
        self.setLayout(vbox)

        self.setLayout(vbox)
        #self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('working with excel')    
        self.show()
        
    def update_text(self):
        text = self.line_edit.text()
        self.lbl.setText(f'Hello, {text}!')


#end of page2.py