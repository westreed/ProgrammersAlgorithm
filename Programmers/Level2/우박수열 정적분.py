# 연습문제
# https://school.programmers.co.kr/learn/courses/30/lessons/134239

def collatz(_list, v, is_rec):
    if v & 1: v = v*3 + 1
    else: v = v // 2

    if v > 1:
        _list.append(v)
        collatz(_list, v, True)
    
    if is_rec is False:
        _list.append(1)
        return _list

def integral(_list):
    length = len(_list)
    volume = []
    for i in range(length-1): # i~i+1
        y1, y2 = _list[i], _list[i+1]
        if y1 < y2: y1, y2 = y2, y1
        volume.append(y1-(y1-y2)/2)

    return volume

def sum_value(volume, _range):
    if _range == [0,0]:
        return sum(volume)
    
    start = _range[0]
    end = len(volume)+_range[1]
    if start > end: return -1.0
    sums = 0
    for i in range(_range[0], len(volume)+_range[1]):
        sums += volume[i]

    return sums

def solution(k, ranges):
    _list = collatz([k], k, False)
    volume = integral(_list)
    return [sum_value(volume, _range) for _range in ranges]



k = [5, 3]
ranges = [
    [[0,0],[0,-1],[2,-3],[3,-3]],
    [[0,0], [1,-2], [3,-3]]
]
result = [
    [33.0,31.5,0.0,-1.0],
    [47.0,36.0,12.0]
]

for q in [0, 1]:
    qid = solution(k[q], ranges[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')