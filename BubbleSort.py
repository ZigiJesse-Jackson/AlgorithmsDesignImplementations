from typing import TypeVar, MutableSequence
T = TypeVar('T')

"""function to sort a MutableSequence of items

args:
    L(MutableSequence): a MutableSequence L of n items of any type


returns:
    MutableSequence: a MutableSequence of sorted items in nondecreasing _order"""


def bubblesort(L: MutableSequence[T]) -> MutableSequence[T]:
    size = len(L)
    if size == 0:
        raise Warning('Function cannot be performed on an empty MutableSequence')
    elif size == 1:
        return L
    for i in range(0, size-1):
        for j in range(0, size-1-i):
            if L[j+1] < L[j]:
                L[j], L[j+1] = L[j+1], L[j]
    return L





