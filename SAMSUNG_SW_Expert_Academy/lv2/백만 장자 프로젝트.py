# 1859
# 연습문제

# 입력
'''
4
3
10 7 6
3
3 5 9
5
1 1 3 1 2
6
1 1 3 1 4
'''

case = int(input())
for c in range(case):
    days    = int(input())
    prices  = list(map(int, input().split()))
    profit  = 0
    maxv    = prices[-1]
    buys    = [0,0] # cnt, sum

    for i in range(len(prices)-2,-1,-1):
        if prices[i] > maxv:
            profit += maxv*buys[0] - buys[1]
            maxv = prices[i]
            buys = [0,0]
            continue
        
        buys[0] += 1
        buys[1] += prices[i]

    profit += maxv*buys[0] - buys[1]
    print(f'#{c+1} {profit}')

