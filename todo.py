class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self):
        task = input("Enter the task you want to add: ")
        self.tasks.append(task)
        print("Task added successfully.")

    def delete_task(self):
        self.show_tasks()

        try:
            index = int(input("Enter task number to delete: "))
            if 1 <= index <= len(self.tasks):
                removed = self.tasks.pop(index - 1)
                print(f"Deleted: {removed}")
            else:
                print("Invalid number.")
        except ValueError:
            print("Please enter a number.")

    def update_task(self):
        self.show_tasks()

        try:
            index = int(input("Enter task number to update: "))
            if 1 <= index <= len(self.tasks):
                new_task = input("Enter new task: ")
                self.tasks[index - 1] = new_task
                print("Task updated successfully.")
            else:
                print("Invalid number.")
        except ValueError:
            print("Please enter a number.")

    def show_tasks(self):
        if not self.tasks:
            print("No tasks.")
        else:
            print("\nToDo List")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")


if __name__ == "__main__":
    todo = ToDoList()

    while True:
        print("\n===== MENU =====")
        print("1: Add Task")
        print("2: Delete Task")
        print("3: Update Task")
        print("4: Show Tasks")
        print("5: Exit")

        choice = input("Choose: ")

        if choice == "1":
            todo.add_task()
        elif choice == "2":
            todo.delete_task()
        elif choice == "3":
            todo.update_task()
        elif choice == "4":
            todo.show_tasks()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")
