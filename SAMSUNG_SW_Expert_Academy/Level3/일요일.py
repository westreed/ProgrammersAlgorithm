# 13229
# 연습문제

# 입력
'''
3
SUN
SAT
MON
'''

case = int(input())
week = {'SUN':0, 'MON':1, 'TUE':2, 'WED':3, 'THU':4, 'FRI':5, 'SAT':6}
for c in range(case):
    month = input().strip()
    print(f'#{c+1} {7-week[month]}')