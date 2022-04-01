# 동적계획법 (Dynamic Programming)
# https://programmers.co.kr/learn/courses/30/lessons/42897

sum = 0
num = 0
caches = []
moneys = []

def dp(id):
    global sum, num, moneys, caches
    if id >= num:
        return 0
    
    sum = caches[id]
    if sum != -1: return sum
    
    if id == 0:
        sum = max(sum, moneys[id]+dp(id+2))
    return sum


def solution(money):
    # 현재위치에서 가져가야할 집 우선순위
    # 1. 양옆으로 0인 경우
    # 2. 양옆 집의 합평균이 현재위치보다 낮거나 같은 경우
    # 3. 양옆의 합평균보다 작지만 두칸 떨어진 집의 합평균이 더 큰 경우
    global num, sum, moneys, caches
    num = len(money)
    moneys = money
    caches = [-1 for _ in range(num)]
    return dp(0)


money = [
    [1,2,3,1],
    [1,0,0,4,4,2,1,4],
    [0,0,4,4,2,1,4],
    [999,1000,999,999,0]
]
result = [
    4,
    10,
    10,
    1999
]

for q in [2,3]:
    qid = solution(money[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')


"""
sum = 0
    num = len(money)
    vit = [False for _ in range(num)]
    for pos in range(num):
        if money[pos] == 0:
            continue
        pre_pos = pos-1 if pos >= 1 else num-1
        nxt_pos = pos+1 if pos < num-1 else 0
        # print(f'{pre_pos} {pos} {nxt_pos}')
        pre_money = money[pre_pos]
        nxt_money = money[nxt_pos]

        if vit[pre_pos] or vit[nxt_pos]:
            continue
        if pre_money == 0 and nxt_money == 0:
            sum += money[pos]
            vit[pos] = True
            continue
        if (pre_money+nxt_money) <= money[pos]:
            sum += money[pos]
            vit[pos] = True
            continue
        # ppre_pos = pos-2 if pos >= 2 else num+pos-2
        # nnxt_pos = pos+2 if pos < num-2 else pos-num+2
        # if (money[ppre_pos]+money[nnxt_pos] > money[pos]):
        #     sum += money[pos]
        #     vit[pos] = True
    
    print(money)
    print(vit)
    return sum
    """