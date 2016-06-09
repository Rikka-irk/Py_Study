# задание 2
import random


def convert_str_to_dict(s):  # строку с ловарь и убираем лишние пробелы в начале и конце
    d = {}
    s = s.lower()
    s = s.strip(' ')
    i = 0
    while i < len(s):
        d = s.split(' ')
        i += 1
    return d


def generate_num_list():  # создаем список из рандомных чисел
    l = 20
    lst = []
    i = 0
    while i < l:
        lst.append(random.randint(1, 5))
        i += 1
    return lst


def count_repetition(l):  # подсчитываем количество повторений каждого символа строки
    d = {}
    for i in l:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d


string = '                     В траве сидел кузнечик В траве сидел кузнечик Совсем как огуречик Зелененький он был        '

result_num = count_repetition(generate_num_list())
result_str = count_repetition(convert_str_to_dict(string))
print(result_str)
print(result_num)
