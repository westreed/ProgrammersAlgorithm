# 구현, 브루트포스 알고리즘
# https://www.acmicpc.net/problem/7568

input = __import__('sys').stdin.readline
N, Human = int(input()), []

for _ in range(N):
    x,y = map(int, input().split())
    Human.append((x,y))

for h1 in range(N):
    Rank = 1
    for h2 in range(N):
        if h1 != h2:
            Info1, Info2 = Human[h1], Human[h2]
            if Info1[0] < Info2[0] and Info1[1] < Info2[1]:
                Rank += 1
    print(Rank, end=' ')