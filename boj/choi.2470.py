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
    """F F F F T T T T"""
    while lo != hi:
        mid = lo + (hi - lo) // 2
        if pred(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo


def first_false(lo: int, hi: int, pred: Callable[[int], bool]) -> int:
    """T T T T F F F"""
    return first_true(lo, hi, lambda idx: not pred(idx))


@dataclass
class VPredicate:
    liquids: List[int]  # 정렬이 되어있는 용액 리스트
    comb: Tuple[int, int] | None = None

    def predicate(self, v: int) -> bool:
        """두 용액을 섞어 그 특성값의 절댓값을 v 이하로 만들 수 있는가?"""
        for i, liquid in enumerate(self.liquids):
            first_positive = first_true(
                i + 1, len(self.liquids), lambda idx: liquid + self.liquids[idx] >= 0
            )

            # 음수의 영역
            idx = first_true(
                i + 1, first_positive, lambda idx: abs(liquid + self.liquids[idx]) <= v
            )
            if idx < first_positive:
                self.comb = (liquid, self.liquids[idx])
                return True

            # 양수의 영역
            idx = (
                first_false(
                    first_positive,
                    len(self.liquids),
                    lambda idx: abs(liquid + self.liquids[idx]) <= v,
                )
                - 1
            )
            if idx >= first_positive:
                self.comb = (liquid, self.liquids[idx])
                return True

        return False


def solve(liquids: List[int]):
    liquids.sort()

    vpredicate = VPredicate(liquids)
    optimal_v = first_true(0, DIFFMAX, vpredicate.predicate)

    if vpredicate.comb:
        return vpredicate.comb


if __name__ == "__main__":
    n = int(input())
    liquids = [int(x) for x in stdin.readline().split()]
    result = solve(liquids)
    if result is not None:
        print([str(x) for x in result])
