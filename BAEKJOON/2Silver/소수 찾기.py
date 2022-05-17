# 수학, 정수론, 소수판정, 에라토스테네스의 체
# https://www.acmicpc.net/problem/1978

num = int(input())
lists = list(map(int, input().split()))
result = 0

def findPrimeNumber(n):
    if n <= 1: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

for l in lists:
    if findPrimeNumber(l):
        result += 1

print(result)