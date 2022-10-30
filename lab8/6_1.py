from itertools import starmap


def maximize(lists, m):
    return sum(i ** 2 for i in starmap(max, lists)) % m


"""lists = [
    [5, 4],
    [7, 8, 9],
    [5, 7, 8, 9, 10]
]
print(maximize(lists, m=1000))"""