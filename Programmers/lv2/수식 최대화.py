# 2020 카카오 인턴십
# https://programmers.co.kr/learn/courses/30/lessons/67257

def solution(expression):
    from collections import deque
    import itertools
    global order_opr
    answer = []
    temp_queue = deque()
    queue_num = deque()
    queue_num2 = deque()
    operation = ['*', '+', '-']
    temp_opr = set()
    order_opr = []
    front = 0
    rear = 0
    for e in expression:
        if e in operation:
            temp_opr.add(e)
            temp_queue.append(int(expression[front:rear]))
            temp_queue.append(e)
            front = rear+1
        rear += 1
    temp_queue.append(int(expression[front:rear]))
    order_opr = list(itertools.permutations(list(temp_opr),len(temp_opr)))
    step = 0 #int, str, int이면 계산
    front = 0
    rear = len(temp_queue)
    next_op = 0
    queue_num = temp_queue.copy()
    while queue_num:
        n2 = queue_num.popleft() #가장 왼쪽요소 가져오기
        queue_num2.append(n2)
        front += 1
        if step == 0 and type(n2) == int:
            step = 1
        elif step == 1 and type(n2) == str:
            step = 2
        elif step == 2 and type(n2) == int:
            step = 1
            n2 = queue_num2.pop()
            op = queue_num2.pop()
            n1 = queue_num2.pop()
            re = 0
            if order_opr[0][next_op] == op:
                queue_num2.append(eval(str(n1)+op+str(n2)))
            else:
                queue_num2.append(n1)
                queue_num2.append(op)
                queue_num2.append(n2)
        if front > rear-1:
            next_op += 1
            if len(temp_opr) < next_op:
                next_op = 0
                del order_opr[0]
                answer.append(abs(queue_num2.pop()))
                if order_opr == []:
                    maxt = 0
                    for i in answer:
                        if maxt < i:
                            maxt = i
                    return maxt
                queue_num = temp_queue.copy()
                queue_num2 = deque()
                front = 0
                rear = len(queue_num)
                step = 0
                continue
            queue_num = queue_num2.copy()
            queue_num2 = deque()
            front = 0
            rear = len(queue_num)
            step = 0
    return answer

expression = [
    "100-200*300-500+20",
    "50*6-3*2"
]

result = [
    60420,
    300
]

for q in [0,1]:
    qid = solution(expression[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')