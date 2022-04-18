# 2070
# 연습문제

# 입력
'''
3
3 8
7 7
369 123
'''

# 문제풀이
case = int(input())
for c in range(case):
    a,b = (map(int, input().split()))
    if   a > b: result = '>'
    elif a < b: result = '<'
    else:       result = '='
    print(f'#{c+1} {result}')