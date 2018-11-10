from flask import session
from functools import wraps


def check_logged_in(func: object) -> object:
    """"Determines whether user is logged in or not.
        Uses decorator.
    """
    # defines and returns decorated function
    @wraps(func)
    def wrapper(*args, **kwargs) -> object:
        if 'logged_in' in session:
            return func(*args, **kwargs)
        return 'You are not logged in.'
    return wrapper
