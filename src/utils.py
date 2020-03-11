# Don Utilities


def pretty_print(fn):
    def wrapper(*args):
        top_line = ''
        for i in range(60):
            top_line = top_line + '*'
        print(top_line)
        fn(args[0])
        print(top_line)

    return wrapper


