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


def merge(A, B):
    C = []
    i = 0
    j = 0
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1
    C += A[i:] + B[j:]
    return C


def merge_sort(A):
    if len(A) <= 1:
        return A
    else:
        L = A[:len(A) // 2]
        R = A[len(A) // 2:]
    return merge(merge_sort(L), merge_sort(R))

l1 = GenerateList.num_list(15, 99)
print(l1)
print(qsort(l1))
print(merge_sort(l1))
