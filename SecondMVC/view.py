import tkinter as tk
from tkinter import messagebox, font

class SignInView(tk.Frame):
    BACKGROUND_COLOR = "#f2f2f2"
    BUTTON_COLOR = "#4B89DC"
    BUTTON_FOREGROUND = "#FFFFFF"
    FONT_NAME = "Arial"
    FONT_SIZE_LABEL = 12
    FONT_SIZE_ENTRY = 14
    
    def __init__(self, master=None, controller=None):
        super().__init__(master, bg=self.BACKGROUND_COLOR)
        self.master = master
        self.controller = controller
        self.pack(pady=50, padx=50)
        self.create_widgets()

    def create_widgets(self):
        # Set the fonts
        label_font = font.Font(family=self.FONT_NAME, size=self.FONT_SIZE_LABEL)
        entry_font = font.Font(family=self.FONT_NAME, size=self.FONT_SIZE_ENTRY)
        
        # Username
        self.username_label = tk.Label(self, text="Username", bg=self.BACKGROUND_COLOR, font=label_font)
        self.username_label.pack(anchor=tk.W, pady=(0, 5))
        self.username_entry = tk.Entry(self, font=entry_font)
        self.username_entry.pack(fill=tk.X, pady=(0, 20))

        # Password
        self.password_label = tk.Label(self, text="Password", bg=self.BACKGROUND_COLOR, font=label_font)
        self.password_label.pack(anchor=tk.W, pady=(0, 5))
        self.password_entry = tk.Entry(self, show="*", font=entry_font)
        self.password_entry.pack(fill=tk.X, pady=(0, 20))

        # Sign in button
        self.sign_in_button = tk.Button(self, text="Sign In", command=self.authenticate, bg=self.BUTTON_COLOR, fg=self.BUTTON_FOREGROUND, font=entry_font)
        self.sign_in_button.pack(pady=15)

    def authenticate(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if self.controller.authenticate(username, password):
            self.controller.show_task_manager()
        else:
            messagebox.showerror("Error", "Invalid username or password!")



class TaskView(tk.Frame):

    def __init__(self, master=None, controller=None):
        super().__init__(master)
        self.master = master
        self.controller = controller
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.task_entry = tk.Entry(self)
        self.task_entry.grid(row=0, column=0)
        self.add_button = tk.Button(self, text="Add", command=self.add_task)
        self.add_button.grid(row=0, column=1)
        self.tasks_listbox = tk.Listbox(self)
        self.tasks_listbox.grid(row=1, column=0, columnspan=2)
        self.remove_button = tk.Button(self, text="Remove", command=self.remove_task)
        self.remove_button.grid(row=2, column=0, columnspan=2)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.controller.add_task(task)
            self.update_task_listbox()

    def remove_task(self):
        selected_task = self.tasks_listbox.get(tk.ACTIVE)
        if selected_task:
            self.controller.remove_task(selected_task)
            self.update_task_listbox()

    def update_task_listbox(self):
        self.tasks_listbox.delete(0, tk.END)
        for task in self.controller.get_tasks():
            self.tasks_listbox.insert(tk.END, task)
