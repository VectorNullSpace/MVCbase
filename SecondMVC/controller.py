# controller.py
from model import TaskModel
from view import SignInView, TaskView
import tkinter as tk

class TaskController:

    def __init__(self, root):
        self.model = TaskModel()
        self.root = root

        # Initializing with SignInView
        self.signin_view = SignInView(master=root, controller=self)

    def authenticate(self, username, password):
        if self.model.authenticate(username, password):
            self.show_task_manager()
            return True
        return False


    def show_task_manager(self):
        # Destroy sign-in view and show task manager
        self.signin_view.destroy()
        self.view = TaskView(master=self.root, controller=self)


    def add_task(self, task):
        if task and task not in self.model.get_tasks():
            self.model.add_task(task)
            self.view.update_task_listbox()

    def remove_task(self, task):
        self.model.remove_task(task)
        self.view.update_task_listbox()

    def get_tasks(self):
        return self.model.get_tasks()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Task Manager MVC with tkinter")
    app = TaskController(root)
    root.mainloop()
