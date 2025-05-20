class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added.")

    def show_tasks(self):
        if not self.tasks:
            print("No tasks.")
        else:
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")

def main():
    todo = TodoList()
    
    while True:
        print("\nOptions:")
        print("1. Add task")
        print("2. Show tasks")
        print("3. Quit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            task = input("Enter the task: ")
            todo.add_task(task)
        elif choice == "2":
            todo.show_tasks()
        elif choice == "3":
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
