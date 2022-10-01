import sys
import argparse

def create_pars():
    pars = argparse.ArgumentParser()
    pars.add_argument("-n", type=int)
    pars.add_argument("number", nargs="?", type=int)
    return pars


def fib(num):
    if num == 1 or num == 2:
        return num
    return fib(num - 1) + fib(num - 2)


if __name__ == '__main__':
    if len(sys.argv) > 3 or len(sys.argv) < 1:
        sys.exit("Введите правильное количество аргументов")
    parser = create_pars()

    args = parser.parse_args()
    num = args.n
    if num is None:
        num = args.number
    print(fib(num))