"""
# 이분탐색을 묻고 더블로

1. 특성값을 | V | 보다 작게 만들 수 있는가?
2. 용액의 리스트 중 하나를 선택한 뒤, 그 차이를 | V | 이하로 만들 수 있게 만드는 다른 용액을 찾아라

시간복잡도는 O(N * log(N, 2) ** 2) 가 된다.
"""

from dataclasses import dataclass
from typing import Callable, List, Tuple
from sys import stdin

DIFFMAX = 2000000000


def first_true(lo: int, hi: int, pred: Callable[[int], bool]) -> int:
    while lo != hi:
        mid = lo + (hi - lo) // 2
        if pred(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo


@dataclass
class VPredicate:
    liquids: List[int]  # 정렬이 되어있는 용액 리스트
    possible_combination: Tuple[int, int] | None = None

    def predicate(self, v: int) -> bool:
        """두 용액을 섞어 그 특성값을 abs(v) 이하로 만들 수 있는가?"""
        for i, liquid in enumerate(self.liquids):
            # ge <= liquid + x <= le 를 만족하는 x가 liquids 안에 있는가?
            ge = -v - liquid  # greater than or equal
            le = v - liquid  # less than or equal

            idx = first_true(
                i + 1, len(self.liquids), lambda idx: abs(liquid + liquids[idx]) <= v
            )

            if idx < len(self.liquids):
                self.possible_combination = (liquid, self.liquids[idx])
                return True

        return False


n = int(input())
liquids = sorted([int(x) for x in stdin.readline().split()])

vpredicate = VPredicate(liquids)
optimal_v = first_true(1, DIFFMAX, vpredicate.predicate)

if vpredicate.possible_combination:
    print(" ".join([str(x) for x in vpredicate.possible_combination]))
