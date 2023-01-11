# 14413
# 연습문제

# 입력
'''
3
3 6
#.????
?#????
???.??
1 6
##????
3 3
.#.
#?#
.#.
'''

def CompareBoard(Board, SizeX, SizeY):
    # 어짜피 격자모양이 성립하냐 안하냐의 문제이기 때문에,
    # 나올 수 있는 격자무늬 2개의 경우만 따지면 해결된다.
    Check = [('#', '.'), ('.', '#')]
    for c in range(len(Check)):
        isLoop = True
        for x in range(SizeX):
            for y in range(SizeY):
                idx = (x+y) % 2
                # print(Board[x][y], Check[c][idx])
                if Check[c][idx] != Board[x][y] and Board[x][y] != '?':
                    isLoop = False
                    break
            if isLoop is False:
                break
        if isLoop is True:
            return True
    return False

tc = int(input())
answer = ""
for t in range(tc):
    SizeX, SizeY = list(map(int, input().strip().split()))
    Board = []
    for x in range(SizeX):
        Pieces = list(input().strip())
        Board.append(Pieces)

    Result = CompareBoard(Board, SizeX, SizeY)
    if Result is True:
        answer += f"#{t+1} possible\n"
    else:
        answer += f"#{t+1} impossible\n"

print(answer)