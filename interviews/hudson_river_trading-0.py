"""
Decorators are one of the most powerful tools that can be used by Python programmers.
A decorator can change a decorated class or function, e.g. to validate arguments, inject
an argument or register a function somewhere (functools.singledispatch/pytest.fixture).
Argument injection could be leveraged to make functions shorter: instead of burdening
them with the explicit creation of required resources, one could just write a decorator to
inject a handle to a temporary file or database connection.
Requirements

Write a decorator that satisfies the following requirements:
1. The decorator should provide the decorated function with all keyword arguments
passed to the decorator
2. The decorator should preserve the functions positional arguments and their order
3. The decorator should leave the possibility to explicitly pass the arguments to a
a decorated function
4. the decorated function should retain the same name, docstring and other features =
that it had before it was decorated
5. In a case where the decorated function does not accept an argument with a given
name, and does not use **kwargs, ignore that argument and do not pass it (see
example 5).
"""