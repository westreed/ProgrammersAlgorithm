# 12221
# 연습문제

# 입력
'''
4
2 5
5 10
10 10
9 9
'''

case = int(input())
for c in range(case):
    number = list(map(int, input().split()))
    if number[0] > 9 or number[1] > 9: print(f'#{c+1} -1')
    else: print(f'#{c+1} {number[0]*number[1]}')