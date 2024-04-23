# 
# https://www.acmicpc.net/problem/10830

"""
2 5
1 2
3 4
> 69 558
> 337 406
"""

class Matrix:
    def __init__(self, _matrix:list):
        self.size = len(_matrix)
        self.matrix = _matrix

    def multiply(self, other):
        if not isinstance(other, Matrix):
            raise TypeError("Only the Matrix Class can be multiplied.")

        res = [[0]*self.size for _ in range(self.size)]

        for i in range(self.size):
            for j in range(self.size):
                for k in range(self.size):
                    res[i][j] += self.matrix[i][k] * other.matrix[k][j]
                res[i][j] = res[i][j] % 1000
        return res
    
    def __mul__(self, other):
        return self.multiply(other)
    
    def __imul__(self, other):
        self.matrix = self.multiply(other)
        return self
    
    def print(self):
        for i in range(self.size):
            print(*self.matrix[i])

def power(matrix:Matrix, p) -> Matrix:
    identity_matrix = Matrix([[1 if i == j else 0 for j in range(matrix.size)] for i in range(matrix.size)])
    while p:
        if p % 2: # 홀수이면
            p -= 1
            identity_matrix *= matrix
        else:
            matrix *= matrix
            p //= 2
    
    return identity_matrix


if __name__ == "__main__":
    input = __import__("sys").stdin.readline
    N, B = map(int, input().split())
    matrix = Matrix([list(map(int, input().split())) for _ in range(N)])
    matrix = power(matrix, B)
    matrix.print()
