def line(n):
    line = ''

    for i in range(n):
        line += '#'

    return line + '\n'


def square(n):
    square = ''

    for i in range(n):
        square += line(n)

    return square


def rectangle(n, m):
    rectangle = ''

    for i in range(m):
        rectangle += line(n)

    return rectangle


print(line(7))
print(square(4))
print(rectangle(3,4))
