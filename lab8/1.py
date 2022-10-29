def print_map(func, it):
    while True:
        try:
            print(func(next(it)))
        except StopIteration:
            return
