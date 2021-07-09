def explain_how_with_statement_work():
    class ManagedFile:
        def __init__(self, name):
            self.name = name

        # context manager
        def __enter__(self):
            self.file = open(self.name, 'w')
            return self.file

        def __exit__(self, exc_type, exc_val, exc_tb):
            if self.file:
                self.file.close()

    with ManagedFile('hello.txt') as f:
        f.write('hello, world!')
        f.write('bye now')


def explain_how_with_statement_work2():
    from contextlib import contextmanager

    @contextmanager
    def managed_file(name):
        try:
            f = open(name, 'w')
            yield f
        finally:
            f.close()

    with managed_file('hello.txt') as f:
        f.write('hello, world!')
        f.write('bye now')


def explain_how_with_statement_work3():
    class Indenter:
        def __init__(self):
            self.level = 0

        def __enter__(self):
            self.level += 1
            return self

        def __exit__(self, exc_type, exc_val, exc_tb):
            self.level -= 1

        def print(self, text):
            print(' ' * self.level + text)

    with Indenter() as indent:
        indent.print('hi!')
    with indent:
        indent.print('hello')
    with indent:
        indent.print('bonjour')
    indent.print('hey')


def decorator():
    import functools

    def null_decorator(func):
        print(1)
        return func

    def uppercase(func):
        @functools.wraps(func)  # for dubbuging best practise take metadata
        def wrapper():
            original_result = func()
            modified_result = original_result.upper()
            return modified_result
        return wrapper

    def strong(func):
        def wrapper():
            return '<strong>' + func() + '</strong>'
        return wrapper

    def emphasis(func):
        def wrapper():
            return '<em>' + func() + '</em>'
        return wrapper

    def proxy(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper

    def greet():
        """ dddddddddddd """
        return 'Hello!'

    def trace(func):
        def wrapper(*args, **kwargs):
            print(f'TRACE: calling {func.__name__}() '
                  f'with {args}, {kwargs}')

            original_result = func(*args, **kwargs)
            print(f'TRACE: {func.__name__}() '
                  f'returned {original_result!r}')
            return original_result
        return wrapper

    @trace
    def say(name, line):
        return f'{name}: {line}'

    print(say('suno', 'hello'))


def class_():
    class MyClass:
        def method(self):
            return 'instance method called', self

        @classmethod
        def classmethod(cls):
            return 'class method called', cls

        @staticmethod
        def staticmethod():
            return 'static method called'

    obj = MyClass()
    print(obj.method())
    print(obj.classmethod())
    print(obj.staticmethod())
