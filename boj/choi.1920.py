from sys import stdin
from typing import Callable


def first_true(begin: int, end: int, pred: Callable) -> int:
    """
    find index of first true in which located binary condition, such as

    ```
    F F F F F T T T
              ^
    ```
    """
    l = begin
    r = end
    while l != r:
        m = l + (r - l) // 2  # overflow 방지
        if pred(m):
            # next range is [l, m)
            r = m
        else:
            # next range is [m, r), m inclusive
            l = m + 1
    return l


n = int(input())
ls = sorted([int(x.strip()) for x in stdin.readline().split()])
m = int(input())
queries = [int(x.strip()) for x in stdin.readline().split()]

for query in queries:
    try:
        print(int(query == ls[first_true(0, len(ls), lambda idx: query <= ls[idx])]))
    except IndexError as e:
        print(0)
