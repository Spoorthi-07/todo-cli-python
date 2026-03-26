todo_list = []

def add_task():
    task = input("Enter the task: ")
    todo_list.append({"Task": task, "Status":"Pending"})
    print("Task added\n")

def view_task():
    print("Your ToDo List: ")
    if len(todo_list) == 0:
        print("No pending task")
    else:
        for index, task in enumerate(todo_list, 1):
            print(f"{index} : {task['Task']} - {task['Status']}")
        print("\n")

def delete_task():
    if len(todo_list) == 0:
        print("List is empty")
    else:
        try:
            search_index = int(input("Enter the task number to be removed: "))-1
            if 0 <= search_index <len(todo_list):
                removed_task = todo_list.pop(search_index)
                print(f"Task removed: {removed_task['Task']}")
            else:
                print("Invalid task number")
        except ValueError:
            print("Please enter the valid number")
    print("\n")

def mark_done():
    if len(todo_list) == 0:
        print("List is empty")
    else:
        try:
            search_index = int(input("Enter the task number to be marked done: "))-1
            if 0 <= search_index <len(todo_list):
                todo_list[search_index]['Status']="Completed"
                print(f"Task {todo_list[search_index]['Task']} has been marked done")
            else:
                print("Invalid task number")
        except ValueError:
            print("Please enter the valid number\n")

def Task():
    while(True):
        print("\n===== To-Do List Menu =====")
        print("1.Add task")
        print("2.View task")
        print("3.Delete task")
        print("4.Mark as done")
        print("5.Exit")

        try:
            choice =int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid choice\n")
            continue

        if choice == 1:
            add_task()
        elif choice == 2:
            view_task()
        elif choice == 3:
            delete_task()
        elif choice == 4:
            mark_done()
        elif choice == 5:
            print("Exiting the application...")
            break
        else:
            print("Invalid choice")
if __name__ == "__main__":
    Task()



