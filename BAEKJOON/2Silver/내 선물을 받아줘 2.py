# 그래프 이론, 문자열
# https://www.acmicpc.net/problem/15886

'''
6
EEWWEW
'''

input = __import__('sys').stdin.readline
input() # 첫번째 버리기
Strings = input().strip()

Puts = 0
prel, firt, flag = Strings[0], Strings[0], False

for let in Strings:
    if flag is False:
        if let == firt:
            flag = True
    elif let != prel:
            Puts, flag = Puts+1, False
    prel = let

print(Puts)