#start of my_model.py
"""
Model class for a data manipulation application.

Attributes:
    df (pd.DataFrame): DataFrame containing the data.
    columns (list): List of column names in the data.
    selected_columns (list): List of column names selected by the user.

Methods:
    open_excel(filepath): Load an Excel file and store its data in the df attribute.
    set_columns(columns): Set the selected_columns attribute to the given list of columns.
    save_excel(filepath): Save the data in the selected_columns to an Excel file at the given filepath.
    get_lbl_text(): Return a string with a comma-separated list of the selected column names.
"""

from typing import List
import pandas as pd

class DataFrameModel:

    def __init__(self):
        self.df: pd.DataFrame = None
        self.columns: List[str] = []
        self.selected_columns: List[str] = []
        #self.dfinfo: str
        #self.dfdescription: str

    def open_excel(self, filepath: str) -> None:
        try:
            self.df = pd.read_excel(filepath)
            self.columns = self.df.columns.tolist()
            self.selected_columns = []
        except FileNotFoundError:
            # handle the exception here
            print("FileNotFoundError exception caught while attempting to run the function open_excel")
            pass
        except IOError:
            # handle the exception here
            print("IOError exception caught while attempting to run the function open_excel")
            pass
        except:
            # handle the exception here
            print("an exception was caught while attempting to run the function open_excel")
            pass

    def set_columns(self, columns: List[str]) -> None:
        self.selected_columns = columns

    def save_excel(self, filepath: str) -> None:
        try:
            self.df[self.selected_columns].to_excel(filepath, index=False)
        except PermissionError:
            # handle the exception here
            print("PermissionError exception caught while the user does not have the necessary permissions to write to the specified filepath.")
            pass
        except:
            # handle the exception here
            print("exception caught while attempting to run the function save_excel")
            pass

    def get_lbl_text(self):
        return ', '.join(self.selected_columns)

    #functions to display information about the dataframe 
    def analyze_df(self):

        self.dfdescription = self.df.describe().to_string()
        print(self.dfdescription)
        return self.dfdescription


     
#end of my_model.py