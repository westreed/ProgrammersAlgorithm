# 12368
# 연습문제

# 입력
'''
3
1 9
7 17
23 23
'''

case = int(input())
for c in range(case):
    time1, time2 = map(int, input().split())
    print(f'#{c+1} {(time1+time2) % 24}')