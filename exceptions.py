class ChildNotFoundError(Exception):
    """Raised when a child is not found."""
    pass

class TaskNotFoundError(Exception):
    """Raised when a task is not found in the child's tasks list."""
    pass

class InvalidTaskDataError(Exception):
    """Raised when any of the required fields are missing or empty."""
    pass

class InvalidParentData(Exception):
    """Raised when any of the required field are missing or empty."""
    pass

class InvalidEmail(Exception):
    """Raised when the email does not conform to the expected format: user_name123@example-domain.com."""
    pass

class InvalidPassword(Exception):
    """Raised when the password does not meet the required criteria: a minimum
      length of eight characters, at least one uppercase letter, one lowercase 
      letter, one number, and one special character 
      (such as #, ?, !, @, $, %, ^, &, *, or -)."""
    pass

class InvalidName(Exception):
    """Raised when the name is invalid. First and last names must contain at least
      3 letters and consist of letters, spaces, hyphens, or apostrophes. 
      Accented characters are also allowed."""
    pass