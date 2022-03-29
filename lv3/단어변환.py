# 깊이/너비 우선 탐색(DFS/BFS)
# https://programmers.co.kr/learn/courses/30/lessons/43163

def similarity(word, target):
    diff = 0 
    for i in range(len(word)):
        if word[i] != target[i]:
            diff += 1
    return diff

def bfs(start, target, wordDict, visit):
    from collections import deque
    answer = []
    queue = deque()
    queue.append([start, 1])
    visit[start] = True
    while queue:
        node, path = queue.pop()
        for word in wordDict[node]:
            if word == target:
                answer.append(path)
            if not visit[word]:
                queue.append([word, path+1])
                visit[word] = True
    return answer

def solution(begin, target, words):
    if target not in words: return 0
    _words = [begin] + words
    visit = {word:False for word in _words}
    wordDict = {word:[] for word in _words}

    for i in range(len(_words)):
        for j in range(len(_words)):
            if i != j and similarity(_words[i], _words[j]) == 1:
                wordDict[_words[i]].append(_words[j])

    answer = bfs(begin, target, wordDict, visit)
    return min(answer)

begin = [
    "hit",
    "hit"
]
target = [
    "cog",
    "cog"
]
words = [
    ["hot", "dot", "dog", "lot", "log", "cog"],
    ["hot", "dot", "dog", "lot", "log"]
]
result = [
    4,
    0
]

for q in [0,1]:
    qid = solution(begin[q], target[q], words[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')