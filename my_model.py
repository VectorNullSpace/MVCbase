#start of my_model.py

import pandas as pd

class Model:

    def __init__(self):
        self.df = None
        self.columns = []
        self.selected_columns = []

    def open_excel(self, filepath):
        self.df = pd.read_excel(filepath)
        self.columns = self.df.columns.tolist()
        self.selected_columns = []

    def set_columns(self, columns):
        self.selected_columns = columns

    def save_excel(self, filepath):
        self.df[self.selected_columns].to_excel(filepath, index=False)

    def get_lbl_text(self):
        return ', '.join(self.selected_columns)

#end of my_model.py