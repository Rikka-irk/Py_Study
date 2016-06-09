import random


def dict_maker(s):  # строку с ловарь и убираем лишние пробелы в начале и конце
    d = {}
    s = s.lower()
    s = s.strip(' ')
    i = 0
    while i < len(s):
        d = s.split(' ')
        i += 1
    return d


def list_maker():  # создаем список из рандомных чисел
    l = 20
    lst = []
    i = 0
    while i < l:
        lst.append(random.randint(1, 5))
        i += 1
    return lst


def counter(l):  # подсчитываем количество повторений каждого символа строки
    d = {}
    for i in l:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d


string = '                     В траве сидел кузнечик В траве сидел кузнечик Совсем как огуречик Зелененький он был   '

result_num = counter(list_maker())
result_str = counter(dict_maker(string))
print(result_str)
print(result_num)
