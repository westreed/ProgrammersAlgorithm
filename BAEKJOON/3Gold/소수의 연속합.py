# 수학, 정수론, 투 포인터, 소수 판정, 에라토스테네스의 체
# https://www.acmicpc.net/problem/1644

N = int(input())
if N == 1:
    print(0)
    exit(0)

Limit = N+1
prime_table = [i for i in range(Limit)]

prime_table[1] = 0
for i in range(2, int(Limit**0.5)+1):
    if prime_table[i]:
        j = i+i
        while j < Limit:
            prime_table[j] = 0
            j += i

prime_table = [prime_table[i] for i in range(Limit) if prime_table[i]]
prime_len = len(prime_table)

print(prime_len)

start,end = 0,0
sums = prime_table[0]
answer = 0

while end < prime_len:
    if sums <= N:
        if sums == N:
            answer += 1
        end += 1
        if end == prime_len:
            break
        sums += prime_table[end]
    else:
        sums -= prime_table[start]
        start += 1

print(answer)