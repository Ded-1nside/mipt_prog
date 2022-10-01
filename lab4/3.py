def decor(function):
    def wrap(*args, **kwargs):
        args = args[::-1]
        function(*args, **kwargs)
    return wrap

@decor
def power(x, y, show=False): #просто функция для проверки декоратора, захотел поменять
    res = x ** y
    if show:
        print(res)
    return res

power(3, 4, show=True)