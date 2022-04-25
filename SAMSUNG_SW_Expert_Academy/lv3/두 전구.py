# 12741
# 연습문제

# 입력
'''
3
1 3 5 7
0 5 2 4
0 5 1 6
'''

case = int(input())
answer = []
for c in range(case):
    lights = list(map(int, input().split()))
    start = max(lights[0], lights[2])
    ends  = min(lights[1], lights[3])
    if start > ends: answer.append(0)
    else: answer.append(ends-start)

for c in range(case):
    print(f'#{c+1} {answer[c]}')