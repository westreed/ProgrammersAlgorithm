# 월간 코드 챌린지 시즌2
# https://programmers.co.kr/learn/courses/30/lessons/76502

def solution(s):
    from collections import deque
    length = len(s)
    answer = 0
    s = list(s)
    set1 = {'(':1, '[':2, '{':3}
    set2 = {')':1, ']':2, '}':3}
    for _ in range(length): #스트링 회전 반복문
        string = deque(s)
        index = -1
        stack = deque()
        check = False
        parentheses = 0 #괄호상태
        while string:
            if check: break
            temp = string.popleft()
            stack.append(temp)
            index += 1
            
            k = 0
            while index != -1:
                if stack[index] in set1:
                    parentheses = set1[stack[index]]
                    break
                else:
                    if 0 < parentheses: #열린 상태일때
                        if parentheses == set2[stack[index]]:
                            parentheses = 0
                            index -= 2
                            stack.pop()
                            stack.pop()
                        else:
                            check = True
                            break
                    else:
                        check = True
                        break
            if not string:
                if parentheses > 0 or check: break
                else: answer += 1
            
        
        #회전시키기
        s.insert(0, s.pop())
        
    return answer

s = [
    "[](){}",
    "}]()[{",
    "[)(]",
    "}}}"
]

result = [
    3,
    2,
    0,
    0
]

for q in [0,1,2,3]:
    qid = solution(s[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')