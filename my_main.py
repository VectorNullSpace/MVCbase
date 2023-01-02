#start of my_main.py

import sys
from PyQt5 import QtWidgets
from my_model import Model
from my_view import View
from my_controller import Controller

def main():
    
    app = QtWidgets.QApplication(sys.argv)
    
    model = Model()
    view = View(model)
    print("view object is created")
    controller = Controller(model, view)
    view.show()
    
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

#end of my_main.py