# 브루트포스 알고리즘
# https://www.acmicpc.net/problem/1107

# 입력
'''
5457
3
6 7 8

500000
4
4 5 7 8 9

14
2
1 5
>> 6

10
9
0 1 2 3 4 5 6 7 8
>> 2

9
9
0 2 3 4 5 6 7 8 9
>> 4
'''
Number = int(input()) # 대상채널
Broken = int(input())
Keypad = []
if Broken > 0:
    Keypad = list(map(int, input().split()))

def check(num): # 제일 가까우면서 직접 누를 수 있는 번호 찾기
    for e in str(num):
        if int(e) in Keypad: return False
    return True

def count():
    up_num = Number
    dn_num = Number
    up_sel = 0xFFFFFFFF
    dn_sel = 0xFFFFFFFF
    only_move = abs(Number-100)
    while up_num != 100 and dn_num != 100:
        if check(dn_num):
            dn_sel = len(str(dn_num)) + abs(Number-dn_num)
            break
        if check(up_num):
            up_sel = len(str(up_num)) + abs(Number-up_num)
            break
        up_num += 1
        if dn_num > 0: dn_num -= 1
    return min([up_sel, dn_sel, only_move])

print(count())