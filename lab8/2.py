def my_fib(num):
    _current = 0
    _next= 1
    for _ in range(num):
        yield _current
        _current, _next = _next, _current + _next


if __name__ == "__main__":
    for i in my_fib(int(input())):
        print(i)