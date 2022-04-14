# 2017 팁스타운
# https://programmers.co.kr/learn/courses/30/lessons/12985

def solution(n,a,b):
    answer = 0
    table = [i for i in range(1, n+1)]
    maxH = n
    stage = 1
    index = 0
    while(1):
        if(index < maxH/2):
            if(table[index*2] == a or table[index*2] == b):
                if(table[index*2+1] == a or table[index*2+1] == b):
                    return stage
                else:
                    table[index] = table[index*2]
            elif(table[index*2+1] == a or table[index*2+1] == b):
                table[index] = table[index*2+1]
            else:
                table[index] = table[index*2]
            index += 1
        else:
            maxH = int(maxH/2)
            stage += 1
            index = 0

    return answer

n = [8]
a = [4]
b = [7]
result = [3]

for q in [0]:
    qid = solution(n[q], a[q], b[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')