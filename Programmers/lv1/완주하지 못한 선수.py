# 해시
# https://programmers.co.kr/learn/courses/30/lessons/42576

def solution(participant, completion):
    start  = set(tuple(participant))
    finish = set(tuple(completion))
    answer = list(start-finish)
    if answer:
        return answer[0]
    else:
        for lap in completion:
            a = completion.count(lap)
            b = participant.count(lap)
            if (a != b):
                return lap

participant = [
    ["leo", "kiki", "eden"],
    ["marina", "josipa", "nikola", "vinko", "filipa"],
    ["mislav", "stanko", "mislav", "ana"]
]

completion = [
    ["eden", "kiki"],
    ["josipa", "filipa", "marina", "nikola"],
    ["stanko", "ana", "mislav"]
]

result = [
    "leo",
    "vinko",
    "mislav"
]

for q in [0,1,2]:
    qid = solution(participant[q], completion[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')