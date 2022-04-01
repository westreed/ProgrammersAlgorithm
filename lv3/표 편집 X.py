# 2021 카카오 채용연계형 인턴십
# https://programmers.co.kr/learn/courses/30/lessons/81303

def solution(n, k, cmd):
    from collections import deque
    #n = 데이터갯수, k = 현재선택된 행, cmd = 명령어

    cmd = deque(cmd)
    data = {id:True for id in range(n)}
    remain = n
    # data = [id for id in range(n)]
    trash = deque()

    while cmd:
        command = cmd.popleft()
        print(k, command)
        # Up
        if command[0] == 'U':
            _, temp_v = command.split(" ")
            temp_v = int(temp_v)
            while temp_v:
                if k == 0:
                    k = n-1
                else:
                    k -= 1
                if data[k] is True:
                    temp_v -= 1
            print(f'Up {k}')

        # Down
        elif command[0] == 'D':
            _, temp_v = command.split(" ")
            temp_v = int(temp_v)
            while temp_v:
                if k+1 == n:
                    k = 0
                else:
                    k += 1
                if data[k] is True:
                    temp_v -= 1
            print(f'Down {k}')

        # Delete
        elif command[0] == 'C':
            trash.append(f'R {k}')
            data[k] = False
            remain -= 1
            # 가장 마지막 행인 경우
            if n-1 == k:
                cmd.appendleft(f'U 1')
            else:
                cmd.appendleft(f'D 1')
            
            print(f'Delete {k}')

        # Restore
        elif command[0] == 'R':
            _, temp_k = command.split(" ")
            temp_k = int(temp_k)
            remain += 1
            data[temp_k] = True
            print(f'Restore {k}')

        # Ctrl+Z
        elif command[0] == 'Z':
            command = trash.pop()
            cmd.appendleft(command)
            print(f'Ctrl+Z {k}')

    answer = ''
    for i in data:
        if data[i]:
            answer += 'O'
        else:
            answer += 'X'
    return answer

"""
def solution(n, k, cmd):
    from collections import deque
    #n = 데이터갯수, k = 현재선택된 행, cmd = 명령어

    cmd = deque(cmd)
    data = [id for id in range(n)]
    trash = deque()

    while cmd:
        command = cmd.popleft()

        # Up
        if command[0] == 'U':
            _, temp_v = command.split(" ")
            temp_v = int(temp_v)
            if k >= temp_v:
                k -= temp_v
            else:
                k = len(data)+k-temp_v

        # Down
        elif command[0] == 'D':
            _, temp_v = command.split(" ")
            temp_v = int(temp_v)
            if k+temp_v < len(data):
                k += temp_v
            else:
                k = k+temp_v-len(data)

        # Delete
        elif command[0] == 'C':
            trash.append(f'R {k} {data[k]}')
            del data[k]
            # 가장 마지막 행인 경우
            if len(data) == k:
                k -= 1

        # Restore
        elif command[0] == 'R':
            _, temp_k, temp_data = command.split(" ")
            temp_k, temp_data = int(temp_k), int(temp_data)
            if temp_k >= len(data):
                temp_k = len(data)-1
            if temp_k <= k:
                k += 1
            data.insert(temp_k, temp_data)

        # Ctrl+Z
        elif command[0] == 'Z':
            command = trash.pop()
            cmd.appendleft(command)

    answer = ''
    for id in range(n):
        if id in data:
            answer += 'O'
        else:
            answer += 'X'
    return answer
"""

n = [
    8,
    8
]

k = [
    2,
    2
]

cmd = [
    ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"],
    ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]
]

result = [
    "OOOOXOOO",
    "OOXOXOOO"
]

for q in [1]:
    qid = solution(n[q], k[q], cmd[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')