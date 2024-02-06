class Task:
    def __init__(self, title, status=False):
        self.title = title
        self.status = status

    def __str__(self):
        return f"{self.title} - {'Done' if self.status else 'Not Done'}"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        self.tasks.append(Task(title))

    def mark_done(self, title):
        for task in self.tasks:
            if task.title == title:
                task.status = True
                return
        print("Task not found.")

    def view_tasks(self):
        for task in self.tasks:
            print(task)

def main():
    todo_list = ToDoList()

    while True:
        print("\n1. Add Task\n2. Mark Task as Done\n3. View Tasks\n4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter task title: ")
            todo_list.add_task(title)
        elif choice == '2':
            title = input("Enter task title: ")
            todo_list.mark_done(title)
        elif choice == '3':
            todo_list.view_tasks()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()