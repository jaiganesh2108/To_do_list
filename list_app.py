class TodoApp:
    def __init__(self):
        self.tasks = []

    def show_tasks(self):
        if not self.tasks:
            print("No tasks available.\n")
            return
        print("\nTo-Do List:")
        for idx, task in enumerate(self.tasks, start=1):
            status = "✅ Completed" if task['completed'] else "❌ Pending" # remove this stuff if don't wanted
            print(f"{idx}. {task['name']} - {status}")
        print()

    def add_task(self, task_name):
        if task_name.strip():
            task = {"name": task_name.strip(), "completed": False}
            self.tasks.append(task)
            print(f"Added task: '{task_name.strip()}'\n")
        else:
            print("Task name cannot be empty.\n")

    def delete_task(self, task_index):
        try:
            removed_task = self.tasks.pop(task_index)
            print(f"Deleted task: '{removed_task['name']}'\n")
        except IndexError:
            print("Invalid task number. Please try again.\n")

    def mark_task_completed(self, task_index):
        try:
            self.tasks[task_index]['completed'] = True
            print(f"Marked task as completed: '{self.tasks[task_index]['name']}'\n")
        except IndexError:
            print("Invalid task number. Please try again.\n")

    def run(self):
        while True:
            print("Options:")
            print("1. Show Tasks")
            print("2. Add Task")
            print("3. Delete Task")
            print("4. Mark Task Completed")
            print("5. Exit")

            choice = input("Choose an option (1-5): ").strip()

            if choice == "1":
                self.show_tasks()
            elif choice == "2":
                task_name = input("Enter the task name: ")
                self.add_task(task_name)
            elif choice == "3":
                self.show_tasks()
                try:
                    task_index = int(input("Enter the task number to delete: ")) - 1
                    self.delete_task(task_index)
                except ValueError:
                    print("Invalid input. Please enter a valid task number.\n")
            elif choice == "4":
                self.show_tasks()
                try:
                    task_index = int(input("Enter the task number to mark as completed: ")) - 1
                    self.mark_task_completed(task_index)
                except ValueError:
                    print("Invalid input. Please enter a valid task number.\n")
            elif choice == "5":
                print("Exiting the To-Do list app. Goodbye!")
                break
            else:
                print("Invalid choice. Please choose a number between 1 and 5.\n")



if __name__ == "__main__":
    app = TodoApp()
    app.run()
