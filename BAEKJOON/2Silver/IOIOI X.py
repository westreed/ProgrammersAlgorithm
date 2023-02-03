# 문자열
# https://www.acmicpc.net/problem/5525

# 입력
'''
1
13
OOIOIOIOIIIOI
'''

N = int(input())
M = int(input())
String = input().rstrip()

A = 0
P = "I" + "OI"*N
L = 2*N + 1

for i in range(M-N):
    if String[i] == "I" and String[i:i+L] == P:
        A += 1

print(A)