import sys
from PyQt5 import QtWidgets

class ButtonLogic:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def open_file(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.ReadOnly
        filepath, _ = QtWidgets.QFileDialog.getOpenFileName(self.view, 'Open file', '', 'Excel Files (*.xlsx);;All Files (*)', options=options)
        if filepath:
            self.model.open_excel(filepath)
            self.view.list_columns.clear()
            self.view.list_columns.addItems(self.model.columns)

    def select_columns(self):
        selected_items = self.view.list_columns.selectedItems()
        selected_columns = [item.text() for item in selected_items]
        self.model.set_columns(selected_columns)
        self.update_view()

    def save_file(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.ReadOnly
        filepath, _ = QtWidgets.QFileDialog.getSaveFileName(self.view, 'Save file', '', 'Excel Files (*.xlsx);;All Files (*)', options=options)
        if filepath:
            self.model.save_excel(filepath)

    def update_view(self):
        self.view.update_lbl_text()