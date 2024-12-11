import csv
import os

def display_menu():
    print("\n====== TO-DO LIST MENU ======")
    print("1. View To-Do List")
    print("2. Add New Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")
    print("============================")

def load_tasks(filename='tasks.csv'):
    tasks = []
    if os.path.exists(filename):
        with open(filename, mode='r', newline='') as file:
            reader = csv.reader(file)
            tasks = [row[0] for row in reader]
    return tasks

def save_tasks(tasks, filename='tasks.csv'):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        for task in tasks:
            writer.writerow([task])

def view_tasks(tasks):
    if len(tasks) == 0:
        print("\nNo tasks in the to-do list!")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task(tasks):
    task = input("\nEnter the new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{task}' added!")

def update_task(tasks):
    if len(tasks) == 0:
        print("\nNo tasks to update!")
    else:
        view_tasks(tasks)
        task_num = int(input("\nEnter the task number to update: ")) - 1
        if 0 <= task_num < len(tasks):
            new_task = input("Enter the updated task: ")
            tasks[task_num] = new_task
            save_tasks(tasks)
            print("Task updated!")
        else:
            print("Invalid task number!")

def delete_task(tasks):
    if len(tasks) == 0:
        print("\nNo tasks to delete!")
    else:
        view_tasks(tasks)
        task_num = int(input("\nEnter the task number to delete: ")) - 1
        if 0 <= task_num < len(tasks):
            removed_task = tasks.pop(task_num)
            save_tasks(tasks)
            print(f"Task '{removed_task}' deleted!")
        else:
            print("Invalid task number!")

def main():
    tasks = load_tasks()
    
    while True:
        display_menu()
        choice = input("\nChoose an option (1-5): ")

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            update_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Exiting the To-Do List program. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()
