# задание 2

import GenerateList


def convert_str_to_dict(s):  # конвертируем строку в словарь и убираем лишние пробелы в начале и конце
    d = {}
    s = s.lower()
    s = s.strip(' ')
    i = 0
    while i < len(s):
        d = s.split(' ')
        i += 1
    return d


def count_repetition(l):  # подсчитываем количество повторений каждого символа строки
    d = {}
    for i in l:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d


string = '                     В траве сидел кузнечик В траве сидел кузнечик Совсем как огуречик Зелененький он был        '

result_num = count_repetition(GenerateList.num_list(50, 15))
result_str = count_repetition(convert_str_to_dict(string))
print(result_str)
print(result_num)
