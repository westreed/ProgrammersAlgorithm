# 13038
# 연습문제

# 입력
'''
6
2
0 1 0 0 0 0 0
100000
1 0 0 0 1 0 1
1
1 0 0 0 0 0 0
4
1 0 0 0 0 0 1
4
0 0 0 0 0 0 1
7
0 1 0 0 1 1 0
6
1 0 0 0 0 1 1
'''

# 결과
'''
8
233332
1
14
22
15
10
'''

case = int(input())
for c in range(case):
    goal = int(input())
    lessons = list(map(int, input().split()))
    cnt = lessons.count(1)
    answer = []
    for i,l in enumerate(lessons):
        if l == 0: continue
        days = 0
        _goal  = goal
        lesson = lessons[i:] + lessons[:i]

        while True:
            for le in lesson:
                if _goal == 0: break
                elif le == 1: _goal -= 1
                days += 1
            else: continue
            break
            
        answer.append(days)

        # week, _goal = divmod(_goal, cnt)
        # if cnt == 1: week, _goal = week - 1, _goal + 1
        # days += week*7
        
        # for le in lesson:
        #     if _goal == 0: break
        #     elif le == 1: _goal -= 1
        #     days += 1
    
    print(answer)
    print(f'#{c+1} {min(answer)}')