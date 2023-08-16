"""parametric search"""

from typing import Callable
from sys import stdin

MAXN = 1_000_000
MAXM = 2_000_000_000
MAXH = 1_000_000_000


def first_true(lo: int, hi: int, pred: Callable[[int], bool]):
    while lo != hi:
        mid = lo + (hi - lo) // 2
        if pred(mid):
            # next range is [lo, mid)
            hi = mid
        else:
            # next range is [mid, hi)
            lo = mid + 1
    return lo


n, m = [int(x) for x in input().split()]
tree_ls = [int(x.strip()) for x in stdin.readline().split()]

# last false, not first true
print(
    first_true(1, MAXH, lambda h: sum([max(0, tree_h - h) for tree_h in tree_ls]) < m)
    - 1
)
