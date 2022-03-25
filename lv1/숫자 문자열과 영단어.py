# 2021 카카오 채용연계형 인턴십
# https://programmers.co.kr/learn/courses/30/lessons/81301

def solution(s):
    answer = ''
    slen = len(s)
    index = 0
    engNumber = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    while(1):
        if(index == slen):
            print(answer)
            return int(answer)
        for i in range(10):
            length = len(engNumber[i])
            if(engNumber[i] == s[index:index+length]):
                print(slen,index+length,s[index:index+length])
                index += length
                answer += str(i)
                break
        else:
            answer += s[index]
            index += 1
            print(slen,index,s[index-1])

s = [
    "one4seveneight",
    "23four5six7",
    "2three45sixseven",
    "123"
]

result = [
    1478,
    234567,
    234567,
    123
]

for q in [0,1,2,3]:
    qid = solution(s[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')