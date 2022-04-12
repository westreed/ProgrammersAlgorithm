# 2019 KAKAO BLIND RECRUITMENT
# https://programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):
    chatRoom = {}
    chatMsg = []
    for user in record:
        info = user.split(" ")
        if info[0] == 'Enter':
            chatRoom[info[1]] = info[2]
        elif info[0] == 'Change':
            chatRoom[info[1]] = info[2]
    for user in record:
        info = user.split(" ")
        if info[0] == 'Enter':
            nickName = chatRoom[info[1]]
            chatMsg.append(nickName + '님이 들어왔습니다.')
        elif info[0] == 'Leave':
            nickName = chatRoom[info[1]]
            chatMsg.append(nickName + '님이 나갔습니다.')
    return chatMsg

record = [
    ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
]

result = [
    ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]
]

for q in [0]:
    qid = solution(record[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')