# 해시
# https://programmers.co.kr/learn/courses/30/lessons/42576

def solution(participant, completion):
    part_temp = set(participant) #set은 집합형으로 중복을 제거함
    comp_temp = set(completion)
    answer = list(part_temp - comp_temp) #집합의 차를 이용 후 리스트로 변환
    if answer: #answer에 값이 있는 경우
        return answer[0]
    else: #answer에 값이 없는 경우 (선수 중복)
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