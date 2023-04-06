import contextlib

from ContextManagers.db_connection_example import stop_database, start_database, insert_data


@contextlib.contextmanager
def db_handler():
    try:
        start_database()
        yield
    finally:
        stop_database()


if __name__ == "__main__":
    with db_handler():
        insert_data()

# OUTPUT:
# database started
# inserted data
# database stopped
