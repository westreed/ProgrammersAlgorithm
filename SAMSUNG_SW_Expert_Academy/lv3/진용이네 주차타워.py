# 9280
# 연습문제

# 입력
'''
2
3 4
2
3
5
2
1
3
8
3
2
-3
1
4
-4
-2
-1
2 4
5
2
100
500
1000
2000
3
1
2
4
-1
-3
-2
-4
'''

testcase = int(input())
answer = ""

for tc in range(testcase):
    import heapq
    n, m = map(int, input().split())
    park_Index  = [o for o in range(n)]
    park_Place  = {}
    park_Cost   = []
    car_Weight  = []
    car_Waiting = []
    car_Order   = []
    Money = 0
    heapq.heapify(park_Index)

    for _ in range(n):
        park_Cost.append(int(input()))
    for _ in range(m):
        car_Weight.append(int(input()))
    for _ in range(m*2):
        car_Order.append(int(input()))
    
    # print(park_Place, park_Cost, car_Weight, car_Waiting)
    isExit = False
    while car_Order or car_Waiting:
        car = 0
        if isExit is False or not car_Waiting:
            car = car_Order.pop(0)
        else:
            car = car_Waiting.pop(0)
        car_State = True if car > 0 else False
        car_Num = abs(car)
        if car_State is True: # 입장
            isExit = False
            if len(park_Place) < n:
                idx = heapq.heappop(park_Index)
                park_Place[car_Num] = idx
                Money += park_Cost[idx]*car_Weight[car_Num-1]
            else:
                car_Waiting.append(car)
        else: # 나감
            idx = park_Place[car_Num]
            del park_Place[car_Num]
            heapq.heappush(park_Index, idx)
            isExit = True
    
    answer += f"#{tc+1} {Money}\n"

print(answer)