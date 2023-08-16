import math

def prime(n):
    if n == 2: # 2는 소수에 포함 되므로 True로
        return True
    else:
        for i in range(2, int(math.sqrt(n))+1): # 2부터 n의 제곱근까지의 수로 n을 나누어 0인지 확인
            if n % i == 0: # 나누어 떨어지는 경우 소수가 아니므로 False 반환
                return False
        return True # 반복문의 모두 통과 시 소수이므로 True 반환

for _ in range(int(input())):
    n = int(input()) # 짝수 입력
    a = int(n//2) # a, b를 n의 절반으로 바꾼다(n은 항상 짝수)
    b = int(n//2)
    while True:
        if prime(a) and prime(b): # a와 b가 모두 소수인지 확인
            print(a, b) # 맞다면 출력
            break
        else: # a, b 중 하나가 소수가 아닐 시 a는 1 감소, b는 1 증가
            a -= 1
            b += 1