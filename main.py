from parent import Parent
from task import tasks_list


parents_list = []
children_list = []


def register_parent():
    parent = Parent(
                str(input("Name: ")),
                int(input("Age: ")),
                str(input("Gender: ")),
                str(input("Email: ")),
                str(input("Password: "))
            )
    parents_list.append(parent)
    parent.save_to_database()

def add_child(parent):
    child = parent.create_child(
                input("Name: "),
                input("Age: "),
                input("Gender: ")
            )
    children_list.append(child)
    child.save_to_database()

def create_task(parent, child, tasks_list):
    try:
        attributes = ["name", "period", "frequency", "difficulty", "reward", "description"]
        values = [input(f"Task {attr}: ") for attr in attributes]
        task = parent.create_task(child, *values)  # This line was modified to use parent.create_task
        tasks_list.append(task)
        child.add_task(task)
        task.save_to_database()
        print("Task created successfully.")
    except Exception as e:
        print(f"Error creating task: {e}")


def edit_task():
    try:
        parent_index = int(input("Enter the parent number (starting from 1) to edit a task: ")) - 1
        if 0 <= parent_index < len(parents_list):
            parent = parents_list[parent_index]
            print(f"Tasks created by {parent.name}'s children: ")

            for idx, task in enumerate(tasks_list):
                if task.child.parent == parent:
                    print(f"{idx + 1}. {task.name} [{task.child.name}]")

            task_index = int(input("Enter the task number you want to edit: ")) - 1

            if 0 <= task_index < len(tasks_list):
                print("If you don't want to change a field, leave it blank.")
                new_values = [
                    input(f"New task {attr} (current: {getattr(tasks_list[task_index], attr)}): ")
                    or getattr(tasks_list[task_index], attr) for attr in
                    ["name", "period", "frequency", "difficulty", "reward", "description"]
                ]

                tasks_list[task_index].edit_task(*new_values)
                print("Task edited successfully.")
            else:
                print("Invalid task number.")
        else:
            print("Invalid parent number.")
    except ValueError:
        print("Invalid input. Please enter a number.")


def delete_task():
    try:
        parent_index = int(input("Enter the parent number (starting from 1) to delete a task: ")) - 1
        if 0 <= parent_index < len(parents_list):
            parent = parents_list[parent_index]
            print(f"Tasks created by {parent.name}'s children: ")

            for idx, task in enumerate(tasks_list):
                if task.child.parent == parent:
                    print(f"{idx + 1}. {task.name} [{task.child.name}]")
            task_index = int(input("Enter the task number to delete: ")) - 1

            if 0 <= task_index < len(tasks_list):
                task_to_delete = tasks_list.pop(task_index)
                print(f"Task '{task_to_delete.name}' deleted successfully.")
            else:
                print("Invalid task number.")
        else:
            print("Invalid parent number.")
    except ValueError:
        print("Invalid input. Please enter a number.")


def show_registrations():
    print("Showing registrations.\n")
    for parent in parents_list:
        print(parent.get_parent_info())
    for child in children_list:
        print(child.get_child_info())
    for task in tasks_list:
        print(task.get_task_info())


def main():
    while True:
        option = int(input(
            """
                Please choose an option:
                1. Register Parent
                2. Add Child
                3. Create Task
                4. Edit Task
                5. Delete Task
                6. Show All Registrations
                7. Finish Program

                Enter your choice: """
            
        ))
        if option == 1:
            register_parent()
            
        elif option == 2:
            if parents_list: 
                parent_index = int(input("Enter the parent number to add child: ")) - 1
                if 0 <= parent_index < len(parents_list):
                    add_child(parents_list[parent_index])
                else:
                    print("Invalid parent number.")
            else:
                print("No registered parents. Please register a parent first.")
        elif option == 3:
            if parents_list and children_list:
                parent_index = int(input("Enter the parent number to assign the task: ")) - 1
                child_index = int(input("Enter the child number to assign the task: ")) - 1
                if 0 <= parent_index < len(parents_list) and 0 <= child_index < len(children_list):
                    create_task(parents_list[parent_index], children_list[child_index], tasks_list)
                else:
                    print("Invalid parent or child number.")
            else:
                print("No registered parents or children. Please register a parent and a child first.")
        elif option == 4:
            edit_task()
        elif option == 5:
            delete_task()
        elif option == 6:
            show_registrations()
        elif option == 7:
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
