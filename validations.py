import re
from exceptions import InvalidEmail, InvalidPassword, InvalidName, InvalidTaskDataError

VALID_PERIODS = ['morning', 'afternoon', 'evening', 'night']
VALID_DIFFICULTIES = ['very easy', 'easy', 'moderate', 'intermediate', 'difficult']  # Fixed typo: 'very ease' to 'very easy'
VALID_FREQUENCIES = ['daily', 'weekly', 'biweekly', 'monthly', 'seasonal', 'as needed']

EMAIL_PATTERN = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
PW_PATTERN = re.compile(r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$')
NAME_PATTERN = re.compile(r"^[A-Za-zÀ-ÖØ-öø-ÿ\- ']{7,}$")


def is_invalid_email(email):
    """Validate email format."""
    if not re.fullmatch(EMAIL_PATTERN, email):
        raise InvalidEmail("Invalid email format: Email address must adhere to the standard format, such as user@example.com.")

def is_invalid_password(password):
    """Validate password format."""
    if not re.fullmatch(PW_PATTERN, password):
        raise InvalidPassword("Password must be a minimum of eight characters long and include at least one uppercase letter, one lowercase letter, one number, and one special character (such as #, ?, !, @, $, %, ^, &, *, or -).")

def is_invalid_name(name):
    """Validate name format."""
    if not re.fullmatch(NAME_PATTERN, name):
        raise InvalidName("Invalid name. First and last names must contain at least 3 letters and consist of letters, spaces, hyphens, or apostrophes. Accented characters are also allowed.")

def validate_task_data(period, frequency, difficulty):
    """Validate task data."""
    period = period.strip().lower()
    frequency = frequency.strip().lower()
    difficulty = difficulty.strip().lower()

    if period not in VALID_PERIODS:
        raise InvalidTaskDataError(f"Invalid period: {period}")

    if frequency not in VALID_FREQUENCIES:
        raise InvalidTaskDataError(f"Invalid frequency: {frequency}")

    if difficulty not in VALID_DIFFICULTIES:
        raise InvalidTaskDataError(f"Invalid difficulty: {difficulty}")