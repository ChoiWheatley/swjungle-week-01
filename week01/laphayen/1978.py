def find_prime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

n = int(input())

num_list = list(map(int, input().split()))

cnt = 0

for num in num_list:
    if num > 1:
        if find_prime(num) == True:
            cnt += 1

print(cnt)
