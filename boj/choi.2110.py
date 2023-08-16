"""D 이상의 배치가 가능? → last true를 찾는 문제
```
T T T T T T F F F F ...
          ^
```
"""

from dataclasses import dataclass
from typing import Callable, List

MAX_DIST = 1_000_000_000


def first_false(lo: int, hi: int, pred: Callable[[int], bool]) -> int:
    """
    ```
    T T T T F F F ...
            ^
    ```
    """
    while lo != hi:
        mid = lo + (hi - lo) // 2
        if pred(mid):
            lo = mid + 1
        else:
            hi = mid
    return lo


@dataclass
class MyPredicate:
    derivations: List[int]  # 정렬된 집들 사이의 거리를 저장한 배열
    c: int  # 공유기 개수

    def predicate(self, distance: int) -> bool:
        """distance 길이의 공유기 배치가 가능한지 여부를 판단"""
        remain = self.c - 1  # ∵ [0]번 포인트에는 무조건 공유기를 설치할 것이기 때문
        tmp_dist = 0
        for delta in self.derivations:
            tmp_dist += delta
            if distance <= tmp_dist:
                # 공유기 설치 가능
                tmp_dist = 0
                remain -= 1
        return remain <= 0


n, c = [int(x) for x in input().split()]
point_ls = sorted([int(input()) for _ in range(n)])
derivations = [0 for _ in range(len(point_ls) - 1)]
for i in range(len(point_ls) - 1):
    derivations[i] = point_ls[i + 1] - point_ls[i]

mypredicate = MyPredicate(derivations, c)

print(first_false(1, max(point_ls) - min(point_ls), mypredicate.predicate) - 1)
