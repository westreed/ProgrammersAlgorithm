# 6019
# 연습문제

'''
1
250 10 15 20
'''

testcase = int(input())
answer = []

# 파리는 기차A에서 출발한다.
# A는 좌표를 0으로 고정하면, B는 A+B속도로 A에 접근한다.
# D = T*S

for tc in range(testcase):
    D,A,B,F = map(int, input().split())

    # 기차가 만날때까지 걸리는 시간
    T = D/(A+B)

    # T시간동안 파리가 이동하는 거리
    F_D = T*F

    answer.append(f'#{tc+1} {F_D}')

for ans in answer:
    print(ans)