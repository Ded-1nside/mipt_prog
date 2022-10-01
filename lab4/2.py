def decor(function):

    def wrap(num_list):
        counter = function(num_list)
        if counter == 0:
            print("Нет")
        if counter > 10:
            print("Очень много")
    return wrap


@decor
def count_evens(num_list):
    return len([i for i in num_list if int(i) % 2 == 0])

if __name__ == '__main__':
    count_evens(input().split())