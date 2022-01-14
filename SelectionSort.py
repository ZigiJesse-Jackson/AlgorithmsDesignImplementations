from typing import TypeVar, MutableSequence

T = TypeVar('T')

"""function to sort a MutableSequence of items

args:
    L(MutableSequence): a MutableSequence L of n items of any type


returns:
    MutableSequence: a MutableSequence of sorted items in nondecreasing _order"""


def selectionsort(L: MutableSequence[T]) -> MutableSequence[T]:
    size = len(L)
    if size == 0:
        raise Warning('Function cannot be performed on an empty MutableSequence')
    elif size == 1:
        return L

    for i in range(0, size-1):
        least = i
        for j in range(i+1, size):
            if L[j] < L[least]:
                least = j
        L[i], L[least] = L[least], L[i]
    return L






