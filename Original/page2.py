#start of page2.py

import sys
from PyQt5 import QtWidgets
from Original.button_bar import ButtonBar
from my_button_logic import ButtonLogic

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


        # create an instance of the ButtonLogic class
        self.button_logic = ButtonLogic(self.model, self)
        
        # create a dictionary to store the buttons
        self.buttons = {}

        # create a label to display the text
        self.lbl = QtWidgets.QLabel('', self)
        vbox.addWidget(self.lbl)
        self.text_edit = QtWidgets.QTextEdit(self)
        vbox.addWidget(self.text_edit)



        # create a line edit to input the text
        self.line_edit = QtWidgets.QLineEdit(self)
        vbox.addWidget(self.line_edit)
        
        # create a button to update the text
        self.buttons['Update Text'] = QtWidgets.QPushButton('Update Text', self)
        self.buttons['Update Text'].clicked.connect(self.update_text)
        vbox.addWidget(self.buttons['Update Text'])
        
        # create button to analyze data frame
        self.buttons['Analyze Frame'] = QtWidgets.QPushButton('Analyze Frame', self)
        self.buttons['Analyze Frame'].clicked.connect(self.analyze_df)
        vbox.addWidget(self.buttons['Analyze Frame'])
        

        # set the layout of the page
        self.setLayout(vbox)
        #self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('working with excel')    
        self.show()
        
    def update_text(self):
        text = self.line_edit.text()
        self.lbl.setText(f'Hello, {text}!')
    
    #functions to display information about the dataframe 
    def analyze_df(self):
        dfdescription = self.model.analyze_df()
        # display dfdescription in a text edit
        self.text_edit.setText(dfdescription)


#end of page2.py