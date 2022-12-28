# 4698
# 연습문제

# 입력
'''
2
3 10 30
7 1 1000000

답
#1 2
#2 43506
'''

testcase = int(input())
answer = ""

MAX = 10**6
table = [i for i in range(MAX + 1)]
table[1] = 0
for k in range(2,MAX):
    if table[k]:
        idx = 2*k
        while idx <= MAX:
            table[idx] = 0
            idx += k

primes = [2]
for k in range(3, MAX, 2):
    if table[k]:
        primes.append(k)

def findStartIdx(A):
    _f = 0
    _r = len(primes)
    if A <= 2: return 0

    while True:
        _m = (_f + _r) // 2
        if A < primes[_m]:
            _r = _m
        elif A > primes[_m+1]:
            _f = _m
        else:
            return _m

for tc in range(testcase):
    D,A,B = map(int, input().split())
    D = str(D)
    rng = len(primes)
    
    ans = 0
    idx = findStartIdx(A)
    while rng > idx:
        prime = primes[idx]
        if prime > B: break

        if prime >= A:
            string_prime = str(prime)
            if D in string_prime:
                ans += 1

        idx += 1
    
    answer += f"#{tc+1} {ans}\n"

print(answer)