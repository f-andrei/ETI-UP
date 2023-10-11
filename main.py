from parent import Parent
from child import Child
from exceptions import *
from feeling import Feeling
from task import Task, tasks_list

parents_list = []
children_list = []


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
            parent = Parent(
                input("Nome: "),
                input("Idade: "),
                input("Gênero: "),
                input("E-mail: "),
                input("Senha: ")
            )
            parents_list.append(parent)
        elif option == 2:
            child = (parent.create_child(
                input("Nome: "),
                input("Idade: "),
                input("Gênero: ")
            ))
            children_list.append(child)
        elif option == 3:
            try:
                task = (parent.create_task(
                child,
                input("Task name: "),
                input("Task period: "),
                input("Task frequency: "),
                input("Task difficulty: "),
                input("Task reward: "),
                input("Task description: ")
            ))
                tasks_list.append(task)
            except ChildNotFoundError as e:
                print(f"Error: Child not found - {e}")
            
        elif option == 4:
            if len(tasks_list) >= 1:
                print("Which task do you want to edit? ")
                task.task_search()
            else:
                task.task_search()
        elif option == 5:
            ... # delete task
        elif option == 6: # show all data
            print("Exibindo informações cadastradas.\n")
            for parent in parents_list:
                print(parent.get_parent_info())
            for child in children_list:
                print(child.get_child_info())
            for task in tasks_list:
                print(task.get_task_info())
        elif option == 7:
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
