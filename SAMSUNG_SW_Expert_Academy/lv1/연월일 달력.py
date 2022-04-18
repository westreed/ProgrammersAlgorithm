# 2056
# 연습문제

# 입력
'''
5
22220228
20150002
01010101
20140230
11111111
'''

days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

case = int(input())
for c in range(case):
    dateString = input()
    year,month,day = dateString[:4],dateString[4:6],dateString[6:]
    _month, _day = int(month), int(day)
    if _month == 0 or _month > 12:
        print(f'#{c+1} -1')
    elif _day == 0 or days[_month-1] < _day:
        print(f'#{c+1} -1')
    else:
        print(f'#{c+1} {year}/{month}/{day}')