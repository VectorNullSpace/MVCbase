class Controller:
    
    def __init__(self, model, view):
        self.model = model
        self.view = view
    
    def set_columns(self, columns):
        self.model.set_columns(columns)
        self.view.update_lbl_text()

    def select_columns(self):
        selected_columns = self.view.get_selected_columns()
        self.model.set_columns(selected_columns)