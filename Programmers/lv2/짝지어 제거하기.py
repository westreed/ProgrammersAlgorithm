# 2017 팁스타운
# https://programmers.co.kr/learn/courses/30/lessons/12973

def solution(s):
    from collections import deque

    length = len(s)
    if length < 2: return 0
    String = deque(s)
    Space  = deque()
    index  = 0

    while String:
        c = String.popleft()
        Space.append(c)
        index += 1

        if index > 1 and Space[index-1] == Space[index-2]:
            Space.pop()
            Space.pop()
            index -= 2
        
    if Space: return 0
    else:     return 1

    # index = 0
    # length = len(s)
    # stack = []
    # if(length < 2): return 0
    # string = deque(s)
    # while(1):
    #     if(string):
    #         stack.append(string.popleft())
    #         index += 1
    #         if(index > 1):
    #             if(stack[index-2] == stack[index-1]):
    #                 stack.pop()
    #                 stack.pop()
    #                 index -= 2
    #     else:
    #         if(stack):
    #             return 0
    #         else:
    #             return 1

s = [
    "baabaa",
    "cdcd"
]

result = [
    1,
    0
]

for q in [0,1]:
    qid = solution(s[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')