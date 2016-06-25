# сортировки вручную (quick sort, слиянием, и что то еще (асимптотическая сложность<n^2))
import random

import GenerateList  # импортируем модуль генерации массива арндомных символов


def qsort(a):  # функция быстрой сортировки
    if len(a) <= 1:  # если массив состоит из одного элемента или менее, то просто возвращаем массив
        return a
    else:
        rn = random.choice(a)  # выбираем рандомный элемент массива
        l = []
        m = []
        r = []
        for i in a:  # перебираем все элементы массива
            if i < rn:  # если он меньше выбранного элемента а, то вносим его в массив l
                l.append(i)
            elif i > rn:
                r.append(i)  # если больше, то вносим его в массив r
            else:
                m.append(i)  # все элементы, равные выбранному, вносим в массив m
        return qsort(l) + m + qsort(r)  # собираем получившиеся массивы


def merge(a, b):
    c = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    c += a[i:] + b[j:]
    return c


def merge_sort(a):
    if len(a) <= 1:
        return a
    else:
        l = a[:len(a) // 2]
        r = a[len(a) // 2:]
    return merge(merge_sort(l), merge_sort(r))


l = GenerateList.num_list(15, 99)
print(l)
print(qsort(l))
print(merge_sort(l))
