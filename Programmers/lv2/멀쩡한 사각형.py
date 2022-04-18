# Summer/Winter Coding(2019)
# https://programmers.co.kr/learn/courses/30/lessons/62048

def solution(w,h):
    eachb = 0
    if w == h: return w*h - w
    if w <= 1 or h <= 1: return 0
    for x in range(w):
        eachb += (((x+1)*h+w-1) // w) - (x*h // w)
    return w*h-eachb

w = [
    8
]

h = [
    12
]

result = [
    80
]

for q in [0]:
    qid = solution(w[q], h[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')