def stop_database():
    print("database stopped")


def start_database():
    print("database started")


def insert_data():
    print("inserting data")


class SimpleContextManager:
    def __enter__(self):
        """
        This will be run after the 'with' statement
        """
        start_database()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        This is responsible for handling any exceptions that occur within the context manager 'with'. When all the code
        in the 'with' has finished running __exit__ will be run.
        """
        stop_database()


if __name__ == "__main__":
    with SimpleContextManager():
        insert_data()

# OUTPUT:
# database started
# inserted data
# database stopped
