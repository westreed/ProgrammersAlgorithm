# 13547
# 연습문제

# 입력
'''
3
oxoxoxoxoxoxoxo
x
xxxxxxxxxxxx
'''

case = int(input())
for c in range(case):
    game = input().rstrip()

    win  = game.count('o')
    lose = game.count('x')
    cnt  = 15-len(game)

    if win+cnt >= 8:
        print(f'#{c+1} YES')
    else:
        print(f'#{c+1} NO')
