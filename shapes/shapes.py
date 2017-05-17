def line(n):
    line_str = ''
    for i in range(n):
        line_str = line_str + '#'

    return line_str


def square(n):
    return rectangle(n, n)


def rectangle(width, height):
    rectangle_str = ''
    for i in range(height):
        rectangle_str += (line(width) + '\n')

    return rectangle_str


def stairs(n):
    stair_str = ''
    for level_len in range(n):
        stair_str += (line(level_len+1) + '\n')

    return stair_str


def space_line(spaces, hashes):
    return spaces * ' ' + hashes * '#'


def stairs_reverse(n):
    stair_str = ''
    for level_len in range(n):
        stair_str += (space_line(n-level_len-1, level_len+1) + '\n')

    return stair_str

if __name__ == '__main__':
    print(stairs_reverse(13))