from child import Child
from task import Task
from exceptions import ChildNotFoundError, InvalidParentData, InvalidTaskDataError, InvalidEmail, InvalidName, InvalidPassword
from validations import is_invalid_name, is_invalid_email, is_invalid_password, validate_task_data
from database.insert import save_parent_to_database, save_child_to_database, save_task_to_database

class Parent:
    def __init__(self, name: str, age: int, gender: str, email: str, password: str):
        """
        Initialize a Parent object.

        Args:
            name (str): The name of the parent.
            age (int): The age of the parent.
            gender (str): The gender of the parent.
            email (str): The email address of the parent.
            password (str): The password for the parent's account.

        Raises:
            InvalidParentData: If any of the required fields are missing or empty.
            ValueError: If the age input is not a positive integer.

        Attributes:
            name (str): The name of the parent.
            age (int): The age of the parent.
            gender (str): The gender of the parent.
            email (str): The email address of the parent.
            password (str): The password for the parent's account.
            children (list): A list to store child objects associated with the parent.
        """
        if not all([name, age > 0, gender, email, password]):
            raise InvalidParentData("Parent data is incomplete.")
        
        if not is_invalid_name(name): 
            self.name = name.title()

        try:
            age = int(age)
        except ValueError:
            raise ValueError("Invalid age input. Age must be a positive integer.")
        self.age = age

        self.gender = gender.title()

        if not is_invalid_email(email):
            self.email = email

        if not is_invalid_password(password): 
            self.password = password

        self.children: list[Child] = []

    def create_child(self, name: str, age: int, gender: str) -> Child:
        """
        Create a new child and add it to the parent's children list.

        Args:
            name (str): The name of the child.
            age (int): The age of the child.
            gender (str): The gender of the child.

        Returns:
            Child: The newly created Child object.

        Raises:
            ValueError: If any of the required child data is missing or invalid.
            InvalidName: If the child's name is not valid.
        """
        if not name or not gender or int(age) <= 0:
            raise ValueError("Invalid child data. Name, age, and gender are required, and age must be a positive integer.")
        try:
            age = int(age)
        except ValueError:
            raise ValueError("Invalid age input. Age must be a positive integer.")
        
        if is_invalid_name(name):
            raise InvalidName("Invalid name. First and last names must contain at least 3 letters and consist of letters, spaces, hyphens, or apostrophes. Accented characters are also allowed.")
       
        child = Child(name, age, gender, self)
        child.parent = self
        self.children.append(child)
        return child
    
    def create_task(self, child: Child, name: str, period: str, frequency: str,
                    difficulty: str, reward: str, description: str) -> Task:
        """
        Create a task for the given child.

        Args:
            child (Child): The Child object for whom the task is created.
            name (str): The name of the task.
            period (str): The period of the task (e.g., morning, afternoon).
            frequency (str): The frequency of the task (e.g., daily, weekly).
            difficulty (str): The difficulty level of the task.
            reward (str): The reward associated with the task.
            description (str): Description of the task.

        Returns:
            Task: The newly created Task object.

        Raises:
            ChildNotFoundError: If the specified child is not found in the parent's children list.
            InvalidTaskDataError: If any of the task data is invalid.
        """
        if child not in self.children:
            raise ChildNotFoundError("Child not found.")
        
        try:
            validate_task_data(period, frequency, difficulty)
        except InvalidTaskDataError as e:
            raise InvalidTaskDataError(str(e))
        
        task = Task(name, period, frequency, difficulty, reward, description, child)
        child.add_task(task)
        return task
    
    def get_parent_info(self) -> str:
        """
        Get a formatted string containing parent's information.

        Returns:
            str: A formatted string containing parent's information.
        """
        children_names = ", ".join(child.name for child in self.children)
        return f"Parent's info:\n\
                Name: {self.name.title()}\n\
                Age: {self.age}\n\
                Gender: {self.gender}\n\
                E-mail: {self.email}\n\
                Children: {children_names}"
    
    def save_to_database(self):
        save_parent_to_database(self)
