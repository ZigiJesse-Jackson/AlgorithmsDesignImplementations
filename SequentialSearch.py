from typing import Sequence, TypeVar

T = TypeVar('T')


def sequentialsearch(l: Sequence[T], k: T) -> int:
    size = len(l)
    if size == 0:
        return -1

    for i in range(0, size):
        if l[i] == k:
            return i
    return -1
