class ToDoList:
    def __init__(self):
        self.shown = []
        self.i = 1

    def addtasks(self):
        task = input("Enter the task you want to add: ")
        self.shown.append(f"{self.i}. {task}")
        self.i += 1
        print("Task added successfully.")

    def deletetasks(self):
        task = input("Enter the task you want to delete: ")

        for item in self.shown:
            if item.endswith(task):
                self.shown.remove(item)
                print("Task deleted successfully.")
                return

        print("Task not found.")

    def updatetasks(self):
        old_task = input("Enter the task you want to update: ")

        for index, item in enumerate(self.shown):
            if item.endswith(old_task):
                new_task = input("Enter the new task: ")
                self.shown[index] = f"{index + 1}. {new_task}"
                print("Task updated successfully.")
                return

        print("Task not found.")

    def showtasks(self):
        if not self.shown:
            print("No tasks.")
        else:
            print("\nToDo List")
            for task in self.shown:
                print(task)
