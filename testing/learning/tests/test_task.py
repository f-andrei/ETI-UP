from task import Task, tasks_list, InvalidTaskDataError, TaskNotFoundError
import unittest

class TestTask(unittest.TestCase):
    def setUp(self):
        self.task1 = Task("Task 1", "daily", "weekly", "easy", "10", "Do something", None)
        self.task2 = Task("Task 2", "evening", "2", "moderate", "20", "Do something else", None)
        tasks_list.append(self.task1)
        tasks_list.append(self.task2)

    def tearDown(self):
        tasks_list.clear()

    def test_init_with_invalid_data(self):
        with self.assertRaises(InvalidTaskDataError):
            Task("", "daily", "1", "easy", "10", "Do something", None)

    def test_edit_task_with_invalid_data(self):
        with self.assertRaises(InvalidTaskDataError):
            self.task1.edit_task(name="", period="weekly", frequency="3", difficulty="hard", reward="50", description="Do something different")

    def test_edit_task(self):
        self.task1.edit_task(name="New Task", period="morning", frequency="daily", difficulty="moderate", reward=2, description="New Description")
        self.assertEqual(self.task1.name, "New Task")
        self.assertEqual(self.task1.period, "morning")
        self.assertEqual(self.task1.frequency, "daily")
        self.assertEqual(self.task1.difficulty, "moderate")
        self.assertEqual(self.task1.reward, 2)
        self.assertEqual(self.task1.description, "New Description")

    def test_edit_task_with_invalid_period(self):
        with self.assertRaises(InvalidTaskDataError):
            self.task1.edit_task(period="invalid_period")

    def test_edit_task_with_invalid_frequency(self):
        with self.assertRaises(InvalidTaskDataError):
            self.task1.edit_task(frequency="invalid_frequency")

    def test_edit_task_with_invalid_difficulty(self):
        with self.assertRaises(InvalidTaskDataError):
            self.task1.edit_task(difficulty="invalid_difficulty")

    def test_delete_task_with_valid_task_index(self):
        self.assertTrue(self.task1.delete_task(0))
        self.assertNotIn(self.task1, tasks_list)

    def test_delete_task_with_invalid_task_index(self):
        with self.assertRaises(IndexError):
            self.task1.delete_task(10)
        # Ensure that the task list is not modified after an invalid index is provided
        self.assertEqual(len(tasks_list), 2)

    def test_delete_task_with_nonexistent_task_index(self):
        with self.assertRaises(IndexError):
            self.task1.delete_task(10)

    def test_delete_task_with_negative_task_index(self):
        with self.assertRaises(IndexError):
            self.task1.delete_task(-1)

    def test_get_task_by_name(self):
        task = Task.get_task_by_name("Task 1")
        self.assertEqual(task, self.task1)

    def test_get_task_info(self):
        expected_info = f"Task information:\n\
                Task name: {self.task1.name}\n\
                Period: {self.task1.period}\n\
                Frequency: {self.task1.frequency}\n\
                Difficulty: {self.task1.difficulty}\n\
                Reward: {self.task1.reward}\n\
                Description: {self.task1.description}\n"
        self.assertEqual(self.task1.get_task_info(), expected_info)

    def test_correlate_task(self):
        child = "Child 1"
        self.task1.correlate_task(child)
        self.assertEqual(self.task1.child, child)

    def test_edit_task_updates_child_attribute(self):
        child = "Child 1"
        self.task1.edit_task(child=child)
        self.assertEqual(self.task1.child, child)

    def test_delete_task_returns_false_with_invalid_task_index(self):
        with self.assertRaises(IndexError):
            self.task1.delete_task(10)
        # Ensure that the task list is not modified after an invalid index is provided
        self.assertEqual(len(tasks_list), 2)

    def test_delete_task_successful(self):
        initial_length = len(tasks_list)
        self.assertTrue(self.task1.delete_task(0))
        self.assertEqual(len(tasks_list), initial_length - 1)
        self.assertNotIn(self.task1, tasks_list)

    def test_delete_task_index_error(self):
        with self.assertRaises(IndexError):
            self.task1.delete_task(10)

    def test_get_task_by_name_error(self):
        with self.assertRaises(TaskNotFoundError):
            Task.get_task_by_name("Nonexistent Task")



if __name__ == "__main__":
    unittest.main()
