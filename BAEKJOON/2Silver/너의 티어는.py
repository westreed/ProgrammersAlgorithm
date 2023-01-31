# 수학, 다이나믹 프로그래밍, 브루트포스 알고리즘, 확률론
# https://www.acmicpc.net/problem/14613

# 0.5 0.5 0

W,L,D = map(float, input().split())

Board = [[0 for _ in range(2500)] for _ in range(21)]
Board[0][1000] = 1

for i in range(1, 21):
    for j in range(2500):
        if (Board[i-1][j] > 0):
            per = Board[i-1][j]
            if j >= 50: Board[i][j-50] += per*L
            if j <= 2450: Board[i][j+50] += per*W
            Board[i][j] += per*D

Percent = [0, 0, 0, 0, 0]
for j in range(2500):
    p = Board[20][j]
    if j < 500: Percent[0] += p
    elif j < 1000: Percent[1] += p
    elif j < 1500: Percent[2] += p
    elif j < 2000: Percent[3] += p
    else: Percent[4] += p

for k in range(5):
    Percent[k] = round(Percent[k], 8)
    print(f"{round(Percent[k], 8):0.8f}")