# 수학, 분할 정복을 이용한 거듭 제곱
# https://www.acmicpc.net/problem/11444

"""
왜 행렬제곱으로 피보나치 수 문제를 해결할 수 있는지 이해 못했음...
대신 백준님이 올리신 코드를 파이썬 코드로 구현하는 정도만 진행해봄.
https://www.acmicpc.net/blog/view/28
"""

class matrix(list):
    def __mul__(self, other):
        if isinstance(other, matrix):
            size = len(self)
            temp = [[0,0],[0,0]]
            for i in range(size):
                for j in range(size):
                    for k in range(size):
                        temp[i][j] += self[i][k] * other[k][j]
                    temp[i][j] %= 1000000007
            return matrix(temp)

if __name__ == "__main__":
    N = int(input())
    ans = matrix([[1,0],[0,1]])
    a = matrix([[1,1],[1,0]])
    
    while N > 0:
        if N % 2 == 1:
            ans = ans * a
        a = a * a
        N //= 2

    print(ans[0][1])