## Context Managers:
Context managers are used whenever a process needs an initial start and end clause.
Imagine we open up a connection to a database do some work in the database and then 
forget to close the connection. This could cause lots of issues, luckily context 
managers exist in python. Context managers use objects that have both `__enter__` and 
`__exit__` dunder methods.

**`__enter__`**: This is run whenever a object is paired with the `with` python statement,
 and run right after instantiation. Its used for any tear up process e.g. open db connection 
open files, etc.

**`__exit__`**: This is used to tear down or clean up after the desired processes have
been run. This is run if an exception is encountered inside the `with` statement or after
all the code inside the `with` statement has finished running.

See `db_connection_example.py` for code examples.

### Contextlib:
Contextlib is built into pythons standard library and can be used as a decorator to
add context manager functionality dynamically to existing code. If we had an existing db generator
like the one seen in my fastapi-blogs app, we could wrap a decorator around this adding context manager
functionality. See `db_connection_with_contextlib.py`.

### Custom Context Manager Decorators:
It is also possible to extend normal functions to include context managers by building custom context 
managers that inherit from the contextlib library. We can then add context managers to any existing code
without having to significantly change it. See `db_connection_decorator.py`.
