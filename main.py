from feeling import Feeling
from child import Child
from parent import Parent
from task import Task


def main():
    parent = Parent("pai", "123456", "email@gmail.com")
    filho = parent.create_child("filho", 5, 'male')
    tarefa = parent.create_task(filho, "Estudar", "Diariamente", "A noite", "Dificuldade", "Recompensa", "Descricao")
    sentimento = Feeling("Feliz", "Felicidade")

    filho.complete_task(tarefa)
    tarefa.edit_task("Tarefa editada", "Semanalmente", "De manha", "Dificuldade", "recompensa", "Descricaoo")
    tarefa.correlate_task(filho)

    # parent.show_login()
    filho.show_child()
    tarefa.show_task()

if __name__ == "__main__":
    main()