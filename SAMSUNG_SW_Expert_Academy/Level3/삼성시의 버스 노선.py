# 6485
# 연습문제

'''
1
2
1 3
2 5
5
1
2
3
4
5
'''

testcase = int(input())
answer = []

for tc in range(testcase):
    N = int(input())
    N_route = [] # 버스 노선
    for _ in range(N):
        N_route.append(tuple(map(int, input().split())))
    
    P = int(input())
    P_bus = [] # 버스 정류소
    for _ in range(P):
        P_bus.append(int(input()))
    
    R_res = [0 for _ in range(P)]

    for idx, bus in enumerate(P_bus):
        print(idx,bus)
        for ra, rb in N_route:
            if ra <= bus <= rb:
                R_res[idx] += 1
            if rb < bus:
                continue
    
    answer.append(f'#{tc+1} {" ".join(map(str, R_res))}')

for ans in answer:
    print(ans)