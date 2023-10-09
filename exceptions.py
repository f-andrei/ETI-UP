class ChildNotFoundError(Exception):
    """Raised when a child is not found."""
    pass

class TaskNotFoundError(Exception):
    """Raised when a task is not found in the child's tasks list."""
    pass

class InvalidTaskDataError(Exception):
    """Raised when any of the required fields are missing or empty."""
    pass