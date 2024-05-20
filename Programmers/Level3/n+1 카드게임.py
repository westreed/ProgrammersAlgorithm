# 2024 KAKAO WINTER INTERNSHIP
# https://school.programmers.co.kr/learn/courses/30/lessons/258707


def solution(coin, cards):
    n = len(cards)
    target = n+1
    hands = set([cards.pop(0) for _ in range(n//3)])
    coin_cards = set()
    max_round = 1

    while len(cards) > 0:
        coin_cards.add(cards.pop(0))
        coin_cards.add(cards.pop(0))

        max_round += 1
        is_play = False
        # coin 0
        for i in list(hands):
            other = target-i

            if i != other and other in hands:
                is_play = True
                hands.remove(i)
                hands.remove(other)
                break
        
        if is_play is True:
            continue

        # coin 1
        if coin > 0:
            for i in list(hands):
                other = target-i

                if i != other and other in coin_cards:
                    is_play = True
                    hands.remove(i)
                    coin_cards.remove(other)
                    coin -= 1
                    break
        
        if is_play is True:
            continue

        # coin 2
        if coin > 1:
            for i in list(coin_cards):
                other = target-i

                if i != other and other in coin_cards:
                    is_play = True
                    coin_cards.remove(i)
                    coin_cards.remove(other)
                    coin -= 2
                    break
                
        if is_play is True:
            continue

        max_round -= 1
        break
        
    return max_round


coin = [4, 3, 2, 10]
cards = [
    [3, 6, 7, 2, 1, 10, 5, 9, 8, 12, 11, 4],
    [1, 2, 3, 4, 5, 8, 6, 7, 9, 10, 11, 12],
    [5, 8, 1, 2, 9, 4, 12, 11, 3, 10, 6, 7],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
]
result = [5,2,4,1]


for q in [0,1,2,3]:
    qid = solution(coin[q], cards[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')