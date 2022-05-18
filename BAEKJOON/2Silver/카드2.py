# 자료구조, 큐
# https://www.acmicpc.net/problem/2164
from collections import deque

N = int(input())
Deck = deque([i+1 for i in range(N)])

Action = False
# False: 제일 위 카드를 버린다.
# True : 제일 위 카드를 제일 아래로 보낸다.
while len(Deck) > 1:
    card = Deck.popleft()

    if Action is True:
        Deck.append(card)
    Action = not Action

print(Deck[0])