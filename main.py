from parent import Parent
from database.select import get_parent_id_by_email, get_child_info_by_parent_id, get_parent_object, get_child_id_by_parent_email, get_tasks_for_child_by_child_id, get_tasks_for_child
from utils import get_child_index
from database.update import update_task_in_database
from database.delete import delete_task_from_database
from validations import validate_task_data
parents_list = []
children_list = []


def register_parent():
    name = input("Name: ")
    age = int(input("Age: "))
    gender = input("Gender: ")
    email = input("Email: ")
    password = input("Password: ")

    parent_id = get_parent_id_by_email(email)
    if parent_id:
        print("Parent already exists with this email.")
    else:
        parent = Parent(name, age, gender, email, password, id=None)
        parents_list.append(parent)

def add_child():
    parent_email = input("Parent's email: ")
    parent_data = get_parent_object(parent_email)
    
    if parent_data:
        existing_parent = Parent(*parent_data)
        child_name = input("Child's Name: ")
        child_age = int(input("Child's Age: "))
        child_gender = input("Child's Gender: ")

        try:
            existing_parent.create_child(child_name, child_age, child_gender)
            print(f"Child '{child_name}' successfully added to parent '{parent_email}'.")
        except (ValueError) as e:
            print(f"Error creating child: {e}")
        
        existing_parent.save_to_database()
    else:
        print("Parent not found.")

def create_task():
    parent_email = input("Parent's email: ")
    parent_id = get_parent_id_by_email(parent_email)
    parent_data = get_parent_object(parent_email)
    child_object = get_child_info_by_parent_id(parent_id)
    if child_object is None:
        print("Child not found for the provided parent's email.")
        return
    child_index, _ = get_child_index(child_object, allow_selection=False)
    if len(child_object) > 1:
        print(child_index)
        _, child_name, child_age, child_gender = child_object[child_index]

    if len(child_object) == 1:
        _, child_name, child_age, child_gender = child_object[child_index]
    
    parent = Parent(*parent_data)
    child = parent.create_child(child_name, child_age, child_gender)

    attributes = ["name", "period", "frequency", "difficulty", "reward", "description"]
    values = [input(f"Task {attr}: ") for attr in attributes]
    parent.create_task(child, *values)
    print("Task saved successfully.")
    
def edit_task():
    try:
        parent_email = input("Parent's email: ")
        child_id = get_child_id_by_parent_email(parent_email)
        tasks = get_tasks_for_child_by_child_id(child_id)
        task_index = 0
        if len(tasks) > 1:
            print("Tasks created by the parent's children: ")
            for idx, task in enumerate(tasks):
                print(f"{idx + 1}. {task['name']}")
            task_index = int(input("Enter the task number you want to edit: ")) - 1
        elif len(tasks) == 1:
            print(f"Editing task '{tasks[0]['name']}'")
            task_index = 0
        else:
            print("Selected child doesn't have any tasks.")

    
        if 0 <= task_index < len(tasks):
            existing_task = tasks[task_index]
            print("If you don't want to change a field, leave it blank.")

            new_values = []
            for attr in ["name", "period", "frequency", "difficulty", "reward", "description"]:
                user_input = input(f"New task {attr} (current: {existing_task[attr]}): ")
                new_values.append(user_input if user_input else existing_task[attr])

            _, period, frequency, difficulty, _, _ = new_values
            validate_task_data(period, frequency, difficulty)
            update_task_in_database(*new_values, child_id)
            print("Task edited successfully.")
        
    except ValueError:
        print("Invalid input. Please enter a number.")



def delete_task():
    parent_email = input("Parent's email: ")
    child_id = get_child_id_by_parent_email(parent_email)
    child_tasks = get_tasks_for_child_by_child_id(child_id)
    if len(child_tasks) > 1:
        print("Which task do you want to delete? ")
        for idx, task in enumerate(child_tasks):
            print(f"{idx + 1}. {task['name']}")
        task_index = int(input("Task index: ")) - 1
        delete_task_from_database(child_tasks[task_index]['id'])
    elif len(child_tasks) == 1:
        print(f"Task: {child_tasks[0]['name']} will be deleted.")
        proceed = str(input("Do you want to delete? yes/no ")).strip().lower()
        if proceed == 'yes':
            task_index = 0
            delete_task_from_database(child_tasks[task_index]['id'])
        else:
            print("You chose to not delete.")
    else:
        print("No tasks found for selected child.")


def main():
    print("parent")
    # register_parent()
    print("child")
    # add_child()
    print("child")
    # add_child()
    
   
    print("task")
    create_task()
    create_task()
    
    
    print("edit task")
    edit_task()
    print("delete task")
    delete_task()

if __name__ == "__main__":
    main()