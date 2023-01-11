# 2019 카카오 개발자 겨울 인턴십
# https://programmers.co.kr/learn/courses/30/lessons/64064

def compare(id, cond):
    id_len,co_len = len(id),len(cond)

    if id_len != co_len:
        return False

    for i in range(id_len):
        if cond[i] == '*':
            continue
        if cond[i] != id[i]:
            return False

    return True

def solution(user_id, banned_id):
    import itertools
    length = len(banned_id)

    user_list = list(itertools.permutations(user_id, length))
    ban_list = []

    for id in user_list:
        for i in range(length):
            if not compare(id[i], banned_id[i]):
                break
        else:
            ban_list.append(sorted(id))
    
    return len(set(map(tuple, ban_list)))



user_id = [
    ["frodo", "fradi", "crodo", "abc123", "frodoc"],
    ["frodo", "fradi", "crodo", "abc123", "frodoc"],
    ["frodo", "fradi", "crodo", "abc123", "frodoc"]
]

banned_id = [
    ["fr*d*", "abc1**"],
    ["*rodo", "*rodo", "******"],
    ["fr*d*", "*rodo", "******", "******"]
]

result = [
    2,
    2,
    3
]

for q in [0,1,2]:
    qid = solution(user_id[q], banned_id[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')