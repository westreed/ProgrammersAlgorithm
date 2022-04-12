# 2020 KAKAO BLIND RECRUITMENT
# https://programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    from math import ceil
    length = len(s)

    answer = []
    for i in range(1, length+1):
        # i길이만큼 자른 단어를 분석하기
        header = s[0:i]
        cnt    = 1
        string = ''
        loop   = ceil(length/i)
        # 길이단위로 문장을 나눠서 체크하기
        for j in range(1,loop):
            index = j*i
            temp  = s[index:index+i]

            if header == temp: cnt += 1
            else:
                string += f'{header}' if cnt == 1 else f'{cnt}{header}'
                cnt = 1
                header = temp

        string += f'{header}' if cnt == 1 else f'{cnt}{header}'
        answer.append(len(string))
    
    return min(answer)

s = [
    "aabbaccc",
    "ababcdcdababcdcd",
    "abcabcdede",
    "abcabcabcabcdededededede",
    "xababcdcdababcdcd"
]

result = [
    7,
    9,
    8,
    14,
    17
]

for q in [0,1,2,3,4]:
    qid = solution(s[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')