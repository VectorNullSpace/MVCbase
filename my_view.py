#start of my_view.py
import sys
from PyQt5 import QtWidgets
from my_model import Model
from reduce_table_page import reduceTablePage
from page2 import Page2

class View(QtWidgets.QWidget):
    
    def __init__(self, model):
        super().__init__()
        
        self.model = model
        self.initUI()
        
    def initUI(self):
        # create a QStackedWidget
        self.stack = QtWidgets.QStackedWidget(self)
        
        # create instances of the Page1 and Page2 classes
        page1 = reduceTablePage(self.model, self)
        page2 = Page2(self.model, self)
        
        # add the pages to the stacked widget
        self.stack.addWidget(page1)
        self.stack.addWidget(page2)
        
        # make page one the current page displayed
        self.stack.setCurrentIndex(0)
        
        # create a vertical layout for the window
        vbox = QtWidgets.QVBoxLayout()
        
        # add the stacked widget to the layout
        vbox.addWidget(self.stack)
        
        self.setLayout(vbox)
        self.setWindowTitle('Working with Excel')    
        self.show()


#end of myView.py