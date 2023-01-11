# 수학
# https://www.acmicpc.net/problem/2869

A, B, V = map(int, input().split())
H, D = 0, 0

C = A-B
D = (V-A) // C
H += D*C

while H < V:
    D += 1
    H += A
    if H >= V: break
    H -= B

print(D)