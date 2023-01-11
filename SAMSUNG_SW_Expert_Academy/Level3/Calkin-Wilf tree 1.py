# 11688
# 연습문제

# 입력
'''
15
L
R
LL
LR
RL
RR
LLL
LRL
LRR
RLR
RRL
LLRLLRLRLLRRRRLRLRLLRLLRLRLLRR
LLLLLLLLLLLLLLLLLLLLLLLLLLLLLL
LLLLLLLLLLRLLLLLLLLLLLLLLLLLLL
RRRRRRRRRRRRRRRRRRRRRRRRRRLRRR
'''

case = int(input())
for c in range(case):
    cmd = input().strip()
    a,b = 1,1
    for i in cmd:
        if i == 'L': b = a + b
        elif i == 'R': a = a + b
    
    print(f'#{c+1} {a} {b}')