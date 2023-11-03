# 수학, 분할 정복을 이용한 거듭제곱
# https://www.acmicpc.net/problem/1629

# A ^ B % C
# 지수의 분배법칙을 이용해야 함. A^m * A^n = A^(m+n)

A,B,C = map(int, input().split())

def power(a,b,c):
    if b == 1:
        return a % c
    elif b == 2:
        return a**2 % c
    else:
        if b % 2:
            return (power(a, (b//2), c)**2)*a%c
        else:
            return (power(a, (b//2), c)**2)%c

print(power(A,B,C))