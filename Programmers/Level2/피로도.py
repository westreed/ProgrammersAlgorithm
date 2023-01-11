# 위클리 챌린지
# https://programmers.co.kr/learn/courses/30/lessons/87946

answer = []

def dfs(k, dungeons, depth):
    temp = True
    for i in range(len(dungeons)):
        dungeon = dungeons[i]
        if dungeon[0] <= k and dungeon[1] <= k:
            _dungeons = dungeons[:]
            del _dungeons[i]
            dfs(k-dungeon[1], _dungeons, depth+1)
            temp = False
    if temp:
        global answer
        answer.append(depth)

def solution(k, dungeons):
    dfs(k, dungeons, 0)
    return max(answer)

k = [80]
dungeons = [
    [[80,20],[50,40],[30,10]]
]
result = [3]

for q in [0]:
    qid = solution(k[q], dungeons[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')