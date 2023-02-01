# 
# https://www.acmicpc.net/problem/17425

# 입력
'''
5
1
2
10
70
10000
'''

input = __import__('sys').stdin.readline

def divisor(N):
    R = set([1, N])
    for i in range(2, N//2+1):
        A,B = divmod(N, i)
        if B == 0: R.update([i, A])
    
    return sum(R)

Sums = [0, 1, 4, 8]

for _ in range(int(input())):
    N = int(input())
    for i in range(len(Sums), N+1):
        Sums.append(divisor(i)+Sums[-1])

    print(Sums[N])