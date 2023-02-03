# 탐욕법(Greedy)
# https://school.programmers.co.kr/learn/courses/30/lessons/42884


def solution(routes):
    routes.sort()
    answer = 0
    while routes:
        end_point = routes.pop(0)[1]
        while routes:
            nxt_node = routes[0]
            if nxt_node[1] <= end_point:
                end_point = nxt_node[1]
                routes.pop(0)
            elif nxt_node[0] <= end_point:
                routes.pop(0)
            else:
                break
        answer += 1
    
    return answer

routes = [
    [[-20,-15], [-14,-5], [-18,-13], [-5,-3]],
    [[0,1], [2,3], [4,5], [6,7]],
    [[-20,15], [-20,-15], [-14,-5], [-18,-13], [-5,-3]],
    [[-20,15], [-14,-5], [-18,-13], [-5,-3]]
]

result = [
    2,
    4,
    2,
    2
]

for q in [0,1,2,3]:
    qid = solution(routes[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')