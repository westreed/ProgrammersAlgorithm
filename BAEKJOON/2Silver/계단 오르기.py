# 다이나믹 프로그래밍
# https://www.acmicpc.net/problem/2579

# 입력
'''
6
10
20
15
25
10
20
'''

def UpStair(N, Stair):
    if N == 1:
        print(Stair[0])
        return True
    
    # 첫번째는 연속점프, 두번째는 건너점프
    Stair[0] = [Stair[0], Stair[0]]
    Stair[1] = [Stair[0][0] + Stair[1], Stair[1]]

    for i in range(2, N):
        Stair[i] = [Stair[i-1][1] + Stair[i], Stair[i]+max(Stair[i-2])]

    print(max(Stair[-1]))


input = __import__('sys').stdin.readline
N = int(input())
UpStair(N, [int(input()) for _ in range(N)])