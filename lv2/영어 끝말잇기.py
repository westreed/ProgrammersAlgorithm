# Summer/Winter Coding(~2018)
# https://programmers.co.kr/learn/courses/30/lessons/12981

class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}

class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        current_node = self.head

        for char in string:
            if char not in current_node.children:
                current_node.children[char] = Node(char)
            current_node = current_node.children[char]
        current_node.data = string

    def search(self, string):
        current_node = self.head

        for char in string:
            if char in current_node.children:
                current_node = current_node.children[char]
            else:
                return False

        if current_node.data:
            return True
        else:
            return False

    def starts_with(self, prefix):
        current_node = self.head
        words = []

        for p in prefix:
            if p in current_node.children:
                current_node = current_node.children[p]
            else:
                return None

        current_node = [current_node]
        next_node = []
        while True:
            for node in current_node:
                if node.data:
                    words.append(node.data)
                next_node.extend(list(node.children.values()))
            if len(next_node) != 0:
                current_node = next_node
                next_node = []
            else:
                break

        return words

def solution(n, words):
    from collections import deque

    # 사람순서, 차례순서
    order, loop = 1, 1
    Dict = Trie()
    words = deque(words)
    preLetter = words[0][0]
    while words:
        word = words.popleft()
        
        # 끝말잇기 규칙을 어긴 경우
        if word[0] != preLetter[-1]:
            return [order, loop]

        # 사전에 단어가 있는지 검색
        if Dict.search(word): return [order, loop]
        else: Dict.insert(word) #사전에 단어 넣기

        # 사람,차례 순서 설정
        preLetter = word
        if order < n: order += 1
        else:
            order = 1
            loop += 1
    return [0, 0]

n = [
    3,
    5,
    2
]

words = [
    ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"],
    ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"],
    ["hello", "one", "even", "never", "now", "world", "draw"]
]

result = [
    [3,3],
    [0,0],
    [1,3]
]

for q in [0,1,2]:
    qid = solution(n[q], words[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')