from parent import Parent
from child import Child
from task import Task
from exceptions import *
from feeling import Feeling

parents_list = []
children_list = []
tasks_list = []
i = 0
def main():
    global i
    while True:
        option = int(input(
            """
                Selecione a opção desejada:\n
                1. Cadastrar pai\n
                2. Adicionar filho\n
                3. Criar tarefa\n
                4. Editar tarefa\n
                5. Deletar tarefa\n
                6. Exibir todos os dados cadastrados.\n
                7. Finalizar programa.\n
            """
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
            if len(tasks_list) > 1:
                print("Which task do you want to edit? ")
                for task in tasks_list:
                    print(f'{i+1}. {task.name}')
                    i += 1
                task_search = int(input("Task number: "))
                try:
                    print("If you don't want to change a field, leave it blank.")
                    task = tasks_list[task_search - 1]
                    task.edit_task(
                        input("New task name: "),
                        input("New task period: "),
                        input("New task frequency: "),
                        input("New task difficulty: "),
                        input("New task reward: "),
                        input("New task description: ")
                    )
                    print("Task edited successfully.")
                except IndexError:
                    print("Error: Task not found.")
                except TaskNotFoundError as e:
                    print(f"Error: {e}")
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
