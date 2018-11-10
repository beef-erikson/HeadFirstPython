from flask import session
from functools import wraps

"""Function decorator definition for checking if user is logged in"""


def check_logged_in(func):
    """Logic behind what happens if user if logged in or not."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'logged_in' in session:
            return func(*args, **kwargs)
        return 'You do not have permission to view this page.'
    return wrapper
