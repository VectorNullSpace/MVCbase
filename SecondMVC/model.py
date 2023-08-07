# model.py

class TaskModel:

    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def get_tasks(self):
        return self.tasks

    def remove_task(self, task):
        self.tasks.remove(task)

    def authenticate(self, username, password):
        # This is a simplistic example. In a real-world application, you'd have a secure authentication system.
        if username == "admin" and password == "password":
            return True
        return False