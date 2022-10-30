def my_zip(*iterables):
    its = [iter(i) for i in iterables]
    while True:
        try:
            yield tuple([next(i) for i in its])
        except StopIteration:
            return


def my_map(function, iterable):
    for elem in iterable:
        yield function(elem)


def my_enumerate(iterable, start = 0):
    num = start
    for elem in iterable:
        yield num, elem
        num += 1