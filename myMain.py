import sys
from PyQt5 import QtWidgets
from myModel import Model
from myView import View
from myController import Controller

def main():
    
    app = QtWidgets.QApplication(sys.argv)
    
    model = Model()
    view = View(model)
    print("view object is created")
    controller = Controller(model, view)
    
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
