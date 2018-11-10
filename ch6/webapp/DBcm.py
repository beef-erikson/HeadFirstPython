import mysql.connector

"""Class UseDatabase is a context manager for handling
   MySQL connectivity and cleanup
"""


class ConnError(Exception):
    """Custom exception error if connection fails
    """
    pass


class CredentialsError(Exception):
    """Custom exception if login credentials fail
    """
    pass


class SQLError(Exception):
    """Custom exception if query is not expressed properly.
    """
    pass


# Database connectivity
class UseDatabase:
    """Context Manager for database connection
    """
    def __init__(self, config: dict) -> None:
        """Initialization
        """
        self.configuration = config

    def __enter__(self) -> 'cursor':
        """Sets up connection and returns cursor
        """
        try:
            self.conn = mysql.connector.connect(**self.configuration)
            self.cursor = self.conn.cursor()
            return self.cursor
        # cannot connect
        except mysql.connector.errors.InterfaceError as err:
            raise ConnError(err)
        # credentials are wrong
        except mysql.connector.errors.ProgrammingError as err:
            raise CredentialsError(err)

    def __exit__(self, exc_type, exc_val, exc_trace) -> None:
        """Teardown
        """
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
        # error in query
        if exc_type is mysql.connector.errors.ProgrammingError:
            raise SQLError(exc_val)
        # anything unexpected
        elif exc_type:
            raise exc_type(exc_val)
