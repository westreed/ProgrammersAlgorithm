# 2021 KAKAO BLIND RECRUITMENT
# https://programmers.co.kr/learn/courses/30/lessons/72410

# 정규표현식 활용해서 다시 풀어보기..

def solution(new_id):
    copy_id = new_id.lower()
    answer_id = []
    for l in copy_id:
        letter = ord(l)
        if(letter == 45): #-
            answer_id.append(l)
        elif(letter == 46): #.
            answer_id.append(l)
        elif(letter == 95): #_
            answer_id.append(l)
        elif(96 < letter < 123): #a~z
            answer_id.append(l)
        elif(47 < letter < 58): #0~9
            answer_id.append(l)
    
    period = 0
    for l in range(len(answer_id)):
        if(answer_id[l] == '.'):
            period += 1
            if(l == 0 or len(answer_id)-1 == l or period > 1):
                answer_id[l] = ''
        else:
            period = 0
    
    answer_id = "".join(answer_id)
    answer_id = list(answer_id)
    
    if(not answer_id or answer_id[0] == ''):
        answer_id.append('a')
        
    while(len(answer_id) > 15):
        answer_id.pop()
        
    if(answer_id[-1] == '.'):
        answer_id.pop()
    
    while(len(answer_id) < 3):
        answer_id.append(answer_id[-1])
    
    return "".join(answer_id)

new_id = [
    "...!@BaT#*..y.abcdefghijklm",
    "z-+.^.",
    "=.=",
    "123_.def",
    "abcdefghijklmn.p"
]

result = [
    "bat.y.abcdefghi",
    "z--",
    "aaa",
    "123_.def",
    "abcdefghijklmn"
]

for q in [0,1,2,3,4]:
    qid = solution(new_id[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')