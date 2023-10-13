import unittest
from parent import Parent
from child import Child
from task import Task
from exceptions import ChildNotFoundError

class TestParent(unittest.TestCase):
    def setUp(self):
        self.parent = Parent("JohnDoe", 35, "Male", "johndoe@example.com", "password")
        self.child = self.parent.create_child("JaneDoe", 8, "Female")
        self.task = self.parent.create_task(self.child, "Clean room", "Morning", "Monthly", "Easy", "Ice cream", "Clean your room")

    def test_create_child(self):
        self.assertIsInstance(self.child, Child)
        self.assertEqual(self.child.name, "JaneDoe")
        self.assertEqual(self.child.age, 8)
        self.assertEqual(self.child.gender, "Female")

    def test_create_task(self):
        self.assertIsInstance(self.task, Task)
        self.assertEqual(self.task.name, "Clean room")
        self.assertEqual(self.task.period, "Morning")
        self.assertEqual(self.task.frequency, "Monthly")
        self.assertEqual(self.task.difficulty, "Easy")
        self.assertEqual(self.task.reward, "Ice cream")
        self.assertEqual(self.task.description, "Clean your room")
        self.assertEqual(self.task.child, self.child)

    def test_get_parent_info(self):
        parent_info = self.parent.get_parent_info()
        self.assertIn("JohnDoe", parent_info)
        self.assertIn("35", parent_info)
        self.assertIn("Male", parent_info)
        self.assertIn("johndoe@example.com", parent_info)
        self.assertIn("JaneDoe", parent_info)  # Ensure child's name is in parent info

    def test_create_task_with_invalid_child(self):
        with self.assertRaises(ChildNotFoundError):
            invalid_child = Child("InvalidChild", 0, "", self.parent)
            self.parent.create_task(invalid_child, "InvalidTask", "Daily", "Everyday", "Easy", "Ice cream", "Invalid task")

    def test_create_task_without_child(self):
        parent = Parent("AliceDoe", 30, "Female", "alicedoe@example.com", "password")
        with self.assertRaises(ChildNotFoundError):
            parent.create_task(None, "InvalidTask", "Daily", "Everyday", "Easy", "Ice cream", "Invalid task")

    def test_create_child_with_invalid_data(self):
        with self.assertRaises(ValueError):
            self.parent.create_child("", -5, "InvalidGender")

if __name__ == '__main__':
    unittest.main()
