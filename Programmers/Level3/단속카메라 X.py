# 탐욕법(Greedy)
# https://school.programmers.co.kr/learn/courses/30/lessons/42884

def search(car, routes, visits):
    cs,ce = routes[car]
    for idx, route in enumerate(routes):
        if car == idx: continue
        ps,pe = route
        if cs <= pe <= ce and cs < ps:
            visits.append((cs,pe))
        elif cs <= ps <= ce and ce < pe:
            visits.append((ce,ps))
        elif cs <= ps and pe <= ce:
            visits.append((ps,pe))
        elif ps <= cs and ce <= pe:
            visits.append((cs,ce))


def solution(routes):
    number = len(routes)
    visits = []

    for idx in range(number):
        search(idx, routes, visits)
    
    print(visits)

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

for q in [0]:
    qid = solution(routes[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')