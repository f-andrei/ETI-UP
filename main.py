from parent import Parent
from child import Child
from task import Task
from exceptions import *
from feeling import Feeling

def main():
    parent = Parent("pai", "123456", "email@gmail.com")
    child_1 = parent.create_child("filho1", 8, 'male')
    child_2 = parent.create_child("filho2", 10, 'female')

    try:
        task1 = parent.create_task(child_1, "Study", "Daily", "Evening", "Medium", "Reward", "Description")
    except ChildNotFoundError as e:
        print(f"Error: Child not found - {e}")

    task2 = parent.create_task(child_2, "Homework", "Daily", "Night", "High", "Extra Reward", "Math Problems")

    print("Child 1 Info:")
    print(child_1.get_child_info())

    print("\nTask 1 Info:")
    print(task1.get_task_info())

    print("\nChild 2 Info:")
    print(child_2.get_child_info())

    print("\nTask 2 Info:")
    print(task2.get_task_info())

    parent.edit_child(name="New Name", age=9, gender="female")

    try:
        parent.edit_child(name="New Name", age=9, gender="female")
    except ChildNotFoundError as e:
        print(f"Error: Child not found - {e}")

    print("\nUpdated Child 1 Info:")
    print(child_1.get_child_info())

    try:
        child_1.complete_task("Non-existent Task")
    except TaskNotFoundError as e:
        print(f"Error: Task not found - {e}")

    child_2.complete_task(task2.name)

    print("\nUpdated Task 2 Info:")
    print(task2.get_task_info())

    task_name = "Non-existent Task"
    if task2.delete_task(child_2, task_name):
        print(f'Task "{task_name}" deleted successfully.')
    else:
        print(f'Task "{task_name}" not found for child {child_2.name}.')

    task_name = "Homework"
    if task2.delete_task(child_2, task_name):
        print(f'Task "{task_name}" deleted successfully.')
    else:
        print(f'Task "{task_name}" not found for child {child_2.name}.')


if __name__ == "__main__":
    main()
