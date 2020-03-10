# Don Utilities


def pretty_print(fn):
    def wrapper(cur_room):
        middle_line = len(f'{cur_room}')
        if middle_line > 60:
            middle_line = 60
        top_line = ''
        for letter in range(middle_line):
            top_line = top_line + '*'

        print(top_line)
        print(f'{cur_room}')
        print(top_line)

    return wrapper
