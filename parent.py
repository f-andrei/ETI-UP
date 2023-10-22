from child import Child
from task import Task
from exceptions import ParentNotFoundError, ChildNotFoundError, InvalidParentData, InvalidTaskDataError, InvalidEmail, InvalidName, InvalidPassword
from validations import is_invalid_name, validate_task_data
from database.insert import save_parent_to_database, save_child_to_database
from database.select import get_parent_by_email, get_parent_id_by_email, get_child_info_by_parent_id
class Parent:
    def __init__(self, name=None, age=None, gender=None, email=None, password=None, id=None):
        """
        Initialize a Parent object.

        Args:
            name (str, optional): The name of the parent.
            age (int, optional): The age of the parent.
            gender (str, optional): The gender of the parent.
            email (str, optional): The email address of the parent.
            password (str, optional): The password for the parent's account.
            id (int, optional): The ID of the parent in the database.

        Raises:
            InvalidParentData: If any of the required fields are missing or empty and no id is provided.

        Attributes:
            name (str): The name of the parent.
            age (int): The age of the parent.
            gender (str): The gender of the parent.
            email (str): The email address of the parent.
            password (str): The password for the parent's account.
            children (list): A list to store child objects associated with the parent.
        """
        if id is None and not all([name, age, gender, email, password]):
            raise InvalidParentData("Parent data is incomplete.")
        
        if name:
            self.name = name.title()
        else:
            self.name = None

        if age:
            try:
                self.age = int(age)
            except ValueError:
                raise ValueError("Invalid age input. Age must be a positive integer.")
        else:
            self.age = None

        if gender:
            self.gender = gender.title()
        else:
            self.gender = None

        self.email = email
        self.password = password
        if id is None:
            self.id = None
        else:
            self.id = id
        self.children = []

        self.save_to_database()

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

        child_object = get_child_info_by_parent_id(self.id)
        if any(self._is_same_child(child, db_child) for db_child in child_object):
            print("Child already exists in database.")
        else:
            save_child_to_database(child, self.id)
            print("Child added to database.")
        self.children.append(child)
        child.parent_id = self.id
        return child
    
    def create_task(self, child: Child, name: str, period: str, frequency: str,
                    difficulty: str, reward: str, description: str) -> Task:
        """
        Create a task for the given child.

        Args:
            child_name (str): The name of the child for whom the task is created.
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

        # if child not in self.children:
        #     raise ChildNotFoundError("Child not found.")
        
        try:
            validate_task_data(period, frequency, difficulty)
        except InvalidTaskDataError as e:
            raise InvalidTaskDataError(str(e))
        
        task = Task(name, period, frequency, difficulty, reward, description, child, child.child_id)
        return task
        
    def save_to_database(self):
        """Check if the parent's object already exists in db, if not it saves it"""
        existing_parent_email = get_parent_by_email(self.email)
        if existing_parent_email:
            existing_parent_id = get_parent_id_by_email(self.email)
            self.id = existing_parent_id
        else:
            save_parent_to_database(self)
            print("Parent added to database.")

    def _is_same_child(self, new_child: str, db_child: str) -> bool:
        """Compare child in current parent object to all children related to them"""
        return (new_child.name == db_child[1] and
                new_child.age == db_child[2] and
                new_child.gender == db_child[3])