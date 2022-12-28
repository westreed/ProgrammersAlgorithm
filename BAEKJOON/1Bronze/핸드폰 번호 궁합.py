# 구현, 다이나믹 프로그래밍, 문자열
# https://www.acmicpc.net/problem/17202

# 입력
'''
74759336
36195974

01234567
12345678

답
26
02
'''

input = __import__("sys").stdin.readline
Phone1 = input().strip()
Phone2 = input().strip()
mixPhone = [int(Phone1[i//2]) if i % 2 == 0 else int(Phone2[i//2]) for i in range(len(Phone1)+len(Phone2))]

while len(mixPhone) > 2:
    temp = []
    for i in range(len(mixPhone)-1):
        temp.append((mixPhone[i]+mixPhone[i+1]) % 10)
    mixPhone = temp

print(f"{mixPhone[0]}{mixPhone[1]}")