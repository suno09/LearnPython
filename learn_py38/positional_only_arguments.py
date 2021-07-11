"""
/ to denote that all arguments before it must be specified by position (not write parameter name before /)
* Any argument after * must be specified using a keyword (write parameter name after *)
"""


def incr(x, /):
    return x + 1


def greet(name, /, greeting="Hello"):
    return f"{greeting}, {name}"


def to_fahrenheit(*, celsius):
    return 32 + celsius * 9 / 5


def headline(text, /, border="♦", *, width=50):
    return f" {text} ".center(width, border)


if __name__ == '__main__':
    print(incr(1))
    # print(incr(x=2))  # Error syntax
    print(greet("suno", greeting="hola"))
    # print(to_fahrenheit(10))  # Error syntax
    print(to_fahrenheit(celsius=10))
    print(headline("suno", '=', width=20))
    print(headline("Python", "🐍", width=38))
