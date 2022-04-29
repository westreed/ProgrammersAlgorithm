# 11387
# 연습문제

# 입력
'''
3
100 0 1
200 12 10
10000 100 100
'''

case = int(input())
for c in range(case):
    D,L,N = map(int, input().split())

    total = 0
    for i in range(N):
        total += D*(1+(i*L/100))
    
    print(f'#{c+1} {int(total)}')