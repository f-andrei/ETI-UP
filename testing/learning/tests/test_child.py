import unittest
from child import Child
from feeling import Feeling
from task import Task
from exceptions import TaskNotFoundError
from parent import Parent

class TestChild(unittest.TestCase):
    def setUp(self):
        parent = Parent("Bob", 40, "male", "bob@example.com", "12313")
        self.child = Child("Alice", 8, "female", parent)

    def test_add_task(self):
        task = Task("Do homework", "morning", "daily", "moderate", 10, "Math homework due on Friday", self.child)
        self.child.add_task(task)
        self.assertIn(task, self.child.tasks)

    def test_complete_task(self):
        task = Task("Do homework", "morning", "daily", "moderate", 10, "Math homework due on Friday", self.child)
        self.child.add_task(task)
        self.assertEqual(self.child.complete_task("Do homework"), 'Task "Do homework" completed successfully.')

    def test_complete_task_not_found(self):
        with self.assertRaises(TaskNotFoundError):
            self.child.complete_task("Do laundry")

    def test_add_feeling(self):
        feeling = Feeling("Happy", "I got an A on my math test!")
        self.child.add_feeling(feeling)
        self.assertIn(feeling, self.child.feelings)

    def test_get_child_info(self):
        expected_output = f"Child info:\n\
            Name: Alice\n\
            Age: 8\n\
            Gender: female\n\
            Parent: Bob\n\
            Age: 40\n\
            Gender: male\n\
            E-mail: bob@example.com"
        self.assertEqual(self.child.get_child_info(), expected_output)

if __name__ == '__main__':
    unittest.main()