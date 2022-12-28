# 수학, 구현, 사칙연산
# https://www.acmicpc.net/problem/10250

input = __import__('sys').stdin.readline
testcase = int(input())

for _ in range(testcase):
    H,W,N = list(map(int, input().split()))

    def find():
        index = 0
        for w in range(W):
            for h in range(H):
                index += 1
                if index == N:
                    return f'{h+1}{w+1:02}'
    
    print(find())