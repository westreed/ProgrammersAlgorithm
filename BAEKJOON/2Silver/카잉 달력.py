# 
# https://www.acmicpc.net/problem/6064

# 입력
'''
3
10 12 3 9
10 12 7 2
13 11 5 6
'''

# Try 1
# 시간초과 (답이 -1인 경우에는 모든 경우를 순환하게 되는데, 최악의 경우 1599840003번 순회)

# input = __import__('sys').stdin.readline
# T = int(input())

# for _ in range(T):
#     M,N,x,y = map(int, input().split())

#     i,a,b, = 1,1,1
#     if x == y == 1:
#         print(1)
#         continue

#     while True:
#         i += 1
#         a += 1
#         b += 1
#         if a > M: a = 1
#         if b > N: b = 1

#         if a == b == 1:
#             print(-1)
#             break
#         if a == x and b == y:
#             print(i)
#             break

# Try 2
# 34204 KB	3308 ms

input = __import__('sys').stdin.readline
T = int(input())

def getLCM(M,N):
    cnt = 2
    divisior = [1]
    while cnt <= M and cnt <= N:
        if M % cnt == 0 and N % cnt == 0:
            M //= cnt
            N //= cnt
            divisior.append(cnt)
        cnt += 1
    return __import__('functools').reduce(lambda a,b:a*b, divisior+[M,N])

for _ in range(T):
    M,N,x,y = map(int, input().split())
    idx,a,b = x,x,x % N
    MAX = getLCM(M,N)

    while True:
        if b == 0: b = N

        if idx > MAX:
            print(-1)
            break

        if b == y:
            print(idx)
            break

        b = (b+M) % N
        idx += M

# Try 3
# 34200 KB	2528 ms

input = __import__('sys').stdin.readline
T = int(input())

def getLCM(M,N):
    cnt = 2
    divisior = [1]
    K = min(M,N)
    while cnt <= K:
        if M % cnt == 0 and N % cnt == 0:
            M //= cnt
            N //= cnt
            divisior.append(cnt)
        cnt += 1
    return __import__('functools').reduce(lambda a,b:a*b, divisior+[M,N])

for _ in range(T):
    M,N,x,y = map(int, input().split())
    if M < N: M,N,x,y = N,M,y,x
    
    idx,a,b = x,x,x % N
    MAX = getLCM(M,N)

    while True:
        if b == 0: b = N

        if idx > MAX:
            print(-1)
            break

        if b == y:
            print(idx)
            break

        b = (b+M) % N
        idx += M