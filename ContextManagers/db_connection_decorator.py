import contextlib

from ContextManagers.db_connection_example import stop_database, start_database, insert_data


class DbHandlerDecorator(contextlib.ContextDecorator):
    def __enter__(self):
        start_database()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        stop_database()


@DbHandlerDecorator()
def add_data():
    insert_data()


if __name__ == "__main__":
    add_data()

# OUTPUT:
# database started
# inserted data
# database stopped
