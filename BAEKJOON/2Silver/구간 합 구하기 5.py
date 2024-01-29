# 다이나믹 프로그래밍, 누적 합
# https://www.acmicpc.net/problem/11660

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    N,M = map(int, input().split())
    table = [list(map(int, input().split())) for _ in range(N)]

    X,Y = len(table), len(table[0])
    for x in range(X-1):
        for y in range(Y-1):
            if x == 0:
                table[x][y+1] = table[x][y]+table[x][y+1]
            if y == 0:
                table[x+1][y] = table[x][y]+table[x+1][y]
                
            table[x+1][y+1] = table[x+1][y+1] + table[x+1][y] + table[x][y+1] - table[x][y]

    def int_minus(x):
        return int(x)-1

    for _ in range(M):
        x1,y1,x2,y2 = map(int_minus, input().split())
        sums = table[x2][y2]
        if x1 > 0:
            sums -= table[x1-1][y2]
        if y1 > 0:
            sums -= table[x2][y1-1]
        if x1 >= 1 and y1 >= 1:
            sums += table[x1-1][y1-1]
        print(sums)