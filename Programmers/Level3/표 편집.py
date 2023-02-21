# 2021 카카오 채용연계형 인턴십
# https://programmers.co.kr/learn/courses/30/lessons/81303

# Try1 정확성 및 효율성 테스트 실패
def solution1(n, k, cmd):
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

# Try 2 정확성 테스트 통과 / 효율성 테스트 10% 통과
def solution2(n, k, cmd):
    from collections import deque
    #n = 데이터갯수, k = 현재선택된 행, cmd = 명령어

    data = [id for id in range(n)]
    count = n
    trash = deque()

    for trg in cmd:
        if trg[0] == 'U':
            move = int(trg[2:])
            if k < move: k = count-(move-k)
            else: k -= move
            print(f"k={k} move u-{move}\tdata:{data}")
        elif trg[0] == 'D':
            move = int(trg[2:])
            if k+move >= count:k = k+move-count
            else: k += move
            print(f"k={k} move d-{move}\tdata:{data}")
        elif trg[0] == 'C':
            v = data[k]
            del data[k]
            trash.append((k,v))
            count -= 1
            if k == count: k -= 1
            print(f"k={k} delete {k},{v}\tdata:{data}")
        elif trg[0] == 'Z':
            idx,val = trash.pop()
            data.insert(idx, val)
            if k >= idx: k += 1
            count += 1
            print(f"k={k} restore {idx},{val}\tdata:{data}")
    
    answer = ['O' for _ in range(n)]
    for _, val in trash:
        answer[val] = 'X'
    # while trash:
    #     _, val = trash.pop()
    #     answer[val] = 'X'
    return "".join(answer)


# Try 3 정확성 및 효율성 테스트 통과
# 힌트를 받고, 연결리스트로 재구현

def solution(n, k, cmd):
    from collections import deque

    class Node:
        def __init__(self, prev, next):
            self.prev = prev if prev >= 0 else None
            self.next = next if next < n else None

    header = 0
    data = [Node(i-1, i+1) for i in range(n)]
    trash = deque()

    for trg in cmd:
        if trg[0] == 'U':
            move = int(trg[2:])
            for _ in range(move):
                k = data[k].prev
        elif trg[0] == 'D':
            move = int(trg[2:])
            for _ in range(move):
                k = data[k].next
        elif trg[0] == 'C':
            trash.append(k)
            if data[k].prev == None:
                # 삭제된 원소가 첫행인 경우, 내 다음원소의 prev값을 None으로 하기
                data[data[k].next].prev = None
                header = data[k].next
                k = data[k].next
            elif data[k].next == None:
                # 삭제된 원소가 마지막인 경우, 내 이전원소의 next값을 None으로 하기
                data[data[k].prev].next = None
                k = data[k].prev
            else:
                data[data[k].prev].next = data[k].next
                data[data[k].next].prev = data[k].prev
                k = data[k].next
        elif trg[0] == 'Z':
            idx = trash.pop()
            if data[idx].prev == None:
                # 추가된 원소가 첫행인 경우, 내 다음원소의 prev값 수정하기
                data[data[idx].next].prev = idx
                header = idx
            elif data[idx].next == None:
                # 추가된 원소가 마지막인 경우, 내 이전원소의 next값 수정하기
                data[data[idx].prev].next = idx
            else:
                data[data[idx].prev].next = idx
                data[data[idx].next].prev = idx
    
    answer = ["X"] * n
    node = data[header]
    while True:
        answer[header] = "O"
        if not node.next: break
        header = node.next
        node = data[header]

    return "".join(answer)


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

for q in [0,1]:
    qid = solution(n[q], k[q], cmd[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')