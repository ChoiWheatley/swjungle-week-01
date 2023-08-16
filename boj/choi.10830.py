from typing import List

MOD = 1000
Matrix = List[List[int]]


def modulo(base, mod: int):
    """단순 나머지 연산을 모든 행렬 원소에 대하여 수행하여 **수정**함"""
    for row in range(len(base)):
        for col in range(len(base[row])):
            base[row][col] %= mod


def mult(a: Matrix, b: Matrix, n: int):
    """두 개의 nXn 정사각행렬 a, b를 곱한 결과를 리턴"""
    ret = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                ret[i][j] += a[i][k] * b[k][j]
    return ret


def r_sol(exp: int, a: Matrix, mod: int) -> Matrix:
    if exp == 1:
        return a
    if exp % 2 == 0:
        interm = r_sol(exp // 2, a, mod)
        interm = mult(interm, interm, len(a))
        modulo(interm, mod)
    else:
        interm = r_sol(exp // 2, a, mod)
        interm = mult(interm, interm, len(a))
        modulo(interm, mod)
        interm = mult(interm, a, len(a))
        modulo(interm, mod)
    return interm


n, b = [int(x) for x in input().split()]
a = [[int(x) for x in input().split()] for _ in range(n)]

result = r_sol(b, a, MOD)

for line in result:
    print(" ".join([str(x) for x in line]))
