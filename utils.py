from exceptions import InvalidTaskDataError
VALID_PERIODS = ['morning', 'afternoon', 'evening', 'night']
VALID_DIFFICULTIES = ['very ease', 'easy', 'moderate', 'intermediate', 'difficult']
VALID_FREQUENCIES = ['daily', 'weekly', 'biweekly', 'monthly', 'seasonal', 'as needed']


def validate_task_data(period, frequency, difficulty):
    period = period.strip().lower()
    frequency = frequency.strip().lower()
    difficulty = difficulty.strip().lower()

    if period not in VALID_PERIODS:
        raise InvalidTaskDataError(f"Invalid period: {period}")

    if frequency not in VALID_FREQUENCIES:
        raise InvalidTaskDataError(f"Invalid frequency: {frequency}")

    if difficulty not in VALID_DIFFICULTIES:
        raise InvalidTaskDataError(f"Invalid difficulty: {difficulty}")
            