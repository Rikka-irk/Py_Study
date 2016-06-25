# сортировки вручную (quick sort, слиянием, и что то еще (асимптотическая сложность<n^2))
import random

import GenerateList


def qsort(A):
    if len(A) <= 1:
        return A
    else:
        a = random.choice(A)
        L = []
        M = []
        R = []
        for i in A:
            if i < a:
                L.append(i)
            elif i > a:
                R.append(i)
            else:
                M.append(i)
        return qsort(L) + M + qsort(R)


l1 = GenerateList.num_list(15, 99)
l2 = GenerateList.num_list(15, 99)
print(l1)
print(qsort(l1))
