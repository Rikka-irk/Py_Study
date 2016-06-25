import random


def num_list(l, r):  # создаем список из рандомных чисел
    lst = []
    i = 0
    while i < l:
        lst.append(random.randint(1, r))
        i += 1
    return lst
