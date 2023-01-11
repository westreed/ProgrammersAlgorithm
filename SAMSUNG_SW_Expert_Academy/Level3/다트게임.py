# 11285
# 연습문제

# 입력
'''
1
5
80 -14
117 12
98 -69
-86 21
-121 99
'''

import math

case = int(input())
for c in range(case):
    throws = int(input())
    record = 0
    for i in range(throws):
        x,y = map(int, input().split())
        radius = int(math.ceil(math.hypot(x,y)))

        if(0<=radius and radius<=20):
            radius = 20
        elif(20<radius and radius<=40):
            radius = 40
        elif(40<radius and radius<=60):
            radius = 60
        elif(60<radius and radius<=80):
            radius = 80
        elif(80<radius and radius<=100):
            radius = 100
        elif(100<radius and radius<=120):
            radius = 120
        elif(120<radius and radius<=140):
            radius = 140
        elif(140<radius and radius<=160):
            radius = 160
        elif(160<radius and radius<=180):
            radius = 180
        elif(180<radius and radius<=200):
            radius = 200
        else:
            radius = 220
        p = int((220-radius)/20)
        record += p
    
    print(f'#{c+1} {record}')