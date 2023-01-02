#start of reduceTablePage.py
import sys
from PyQt5 import QtWidgets
from myButtonLogic import ButtonLogic
from buttonBar import ButtonBar

class reduceTablePage(QtWidgets.QWidget):
    
    def __init__(self, model, view):
        super().__init__()
        
        self.model = model
        self.view = view
        self.initUI()
        
    def initUI(self):
        print("page1 is being called")
        # create a vertical layout
        vbox = QtWidgets.QVBoxLayout()
        
        # create an instance of the ButtonLogic class
        self.button_logic = ButtonLogic(self.model, self)


        ##implement the buttonBar(must do for every page class)
        # add widgets to the layout
        vbox.addWidget(QtWidgets.QLabel('This is page 1'))
        # create an instance of the ButtonBar class
        button_bar = ButtonBar(self.view)
        # add the ButtonBar instance to the page layout
        vbox.addWidget(button_bar)
        ##end of implementing the buttonBar


        # create a dictionary to store the buttons
        self.buttons = {}
        
        # create a label to display the selected columns
        self.lbl = QtWidgets.QLabel('', self)
        vbox.addWidget(self.lbl)

        # create a button to open the file dialog
        self.buttons['open'] = QtWidgets.QPushButton('Open', self)
        self.buttons['open'].clicked.connect(self.button_logic.open_file)
        vbox.addWidget(self.buttons['open'])

        # create a list widget to display the available columns
        self.list_columns = QtWidgets.QListWidget(self)
        self.list_columns.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        vbox.addWidget(self.list_columns)

        # create a button to select the columns
        self.buttons['select'] = QtWidgets.QPushButton('Select', self)
        self.buttons['select'].clicked.connect(self.button_logic.select_columns)
        vbox.addWidget(self.buttons['select'])

        # create a button to save the file
        self.buttons['save'] = QtWidgets.QPushButton('Save', self)
        self.buttons['save'].clicked.connect(self.button_logic.save_file)
        vbox.addWidget(self.buttons['save'])

        self.setLayout(vbox)
        #self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('working with excel')    
        self.show()


    def update_lbl_text(self):
        self.lbl.setText(self.model.get_lbl_text())    
        
    def get_selected_columns(self):
        selected_items = self.list_columns.selectedItems()
        selected_columns = [item.text() for item in selected_items]
        return selected_columns
        


#end of reduceTablePage.py