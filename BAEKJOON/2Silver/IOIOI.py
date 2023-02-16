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
Idx = 1
Pat = 0
while Idx < M:
    if Idx < M-1 and String[Idx-1] == "I" and \
    String[Idx] == "O" and String[Idx+1] == "I":
        Pat += 1
        Idx += 1
    else:
        if Pat >= N: A += Pat + 1 - N
        Pat = 0
    Idx += 1

if Pat >= N: A += Pat + 1 - N
print(A)