# 구현
# https://www.acmicpc.net/problem/1308

'''
2008 12 27
2009 1 22

2007 12 27
2008 12 27

2008 2 27
3008 2 27

3000 2 26
3000 3 1
'''

start_date  = list(map(int, input().split()))
end_date    = list(map(int, input().split()))
month_day   = [0,31,28,31,30,31,30,31,31,30,31,30,31]

def isLeapMonth(year):
    isLeap = False
    if not year % 4: isLeap = True
    if not year % 100: isLeap = False
    if not year % 400: isLeap = True
    return isLeap

def returnDays(year, month):
    if month == 2 and isLeapMonth(year): return 29
    else: return month_day[month]

def isOver1000Year(date1, date2):
    cy,cm,cd = date1
    ey,em,ed = date2
    if ey-cy >= 1000:
        if em > cm: return True
        elif em == cm and ed >= cd: return True
        else: return False
    else:
        return False

if isOver1000Year(start_date, end_date):
    print('gg')
else:
    D_Day = 0
    while True:
        cy,cm,cd = start_date
        ey,em,ed = end_date
        if cy == ey and cm == em:
            D_Day += ed-cd
            break
        else:
            today = returnDays(cy, cm)
            D_Day += today-cd+1
            
            if cm < 12:
                start_date[1] += 1
                start_date[2] = 1
            else:
                start_date[0] += 1
                start_date[1] = 1
                start_date[2] = 1
            continue
        
        
    print(f'D-{D_Day}')
