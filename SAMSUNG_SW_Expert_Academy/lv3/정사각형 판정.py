# 13732
# 연습문제

# 입력
'''
4
3
...
.##
.##
4
#..#
....
....
#..#
5
.....
.###.
.###.
.###.
.....
5
.....
..###
..###
..###
.....
'''

case = int(input())
for c in range(case):
    N = int(input())
    array = []
    for i in range(N):
        array.append(list(input().rstrip()))
    
    left, right = -1, -1
    start, down = -1, -1

    exitLoop = False
    for y in range(N):
        if exitLoop is True: break
        check = '탐색' # 0 탐색 1 발견 2 종료
        for x in range(N):
            if exitLoop is True: break

            
            if check == '발견':
                if x == N-1 or array[y][x+1] == '.':
                    check = '종료'

                    down = y # 지속적으로 갱신

                    if right == -1: right = x
                    elif right != x:
                        print(f'#{c+1} no') # width 종료점이 안맞음
                        exitLoop = True

            elif array[y][x] == '#':
                if check == '탐색':
                    check = '발견'
                    if start == -1: start = y
                    if left == -1:  left = x
                    elif left != x:
                        print(f'#{c+1} no') # width 시작점이 안맞음
                        exitLoop = True

                if check == '종료':
                    print(f'#{c+1} no') # 중간에 .이 있음
                    exitLoop = True

    if exitLoop is False:
        if down-start != right-left: # 정사각형이 아닌 경우
            print(f'#{c+1} no')
        else:
            print(f'#{c+1} yes')