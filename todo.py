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


# 実行例
todo = ToDoList()

while True:
    print("\n1. Add Task")
    print("2. Delete Task")
    print("3. Update Task")
    print("4. Show Tasks")
    print("5. Exit")

    choice = input("Choose: ")

    if choice == "1":
        todo.addtasks()
    elif choice == "2":
        todo.deletetasks()
    elif choice == "3":
        todo.updatetasks()
    elif choice == "4":
        todo.showtasks()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
