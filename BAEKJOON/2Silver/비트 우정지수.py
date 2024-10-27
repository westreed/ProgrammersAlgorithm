# 그리디 알고리즘
# https://www.acmicpc.net/problem/12782

import sys

input = sys.stdin.readline
T = int(input())
Q = []

for _ in range(T):
    A,B = input().split()
    Q_ = 0
    A_ = {"0":0, "1":0}
    B_ = {"0":0, "1":0}
    for i in range(len(A)):
        if A[i] != B[i]:
            Q_ += 1
            A_[A[i]] += 1
            B_[B[i]] += 1
    
    if A_["0"] and B_["0"]:
        # 비트의 숫자를 바꿔서 해결하려면 2번이 필요하고, 교환은 1번이면 되므로
        # swap 횟수만큼 답에서 빼주면 된다.
        swap = min(A_["0"], B_["0"])
        Q_ -= swap

    Q.append(str(Q_))

print("\n".join(Q))