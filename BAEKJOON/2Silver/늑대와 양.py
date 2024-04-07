# 애드 혹, 해 구성하기
# https://www.acmicpc.net/problem/16956

"""
6 6
..S...
..S.W.
.S....
..W...
...W..
......
"""

# 울타리의 최소 갯수는 중요하지 않다.
# 그 의미는 그냥 양 근처는 무조건 울타리로 둘러버리면 된다는 의미.
# 하지만 양과 늑대가 붙어있는 경우는 분리할 수 없으니 0으로 처리해야 한다.

def setup_defence(Maps, R, C):
    arrow = ((-1,0), (1,0), (0,-1), (0,1))

    for x in range(R):
        for y in range(C):
            if Maps[x][y] == "S":
                for dx,dy in arrow:
                    nx = x+dx
                    ny = y+dy

                    if nx < 0 or nx >= R: continue
                    if ny < 0 or ny >= C: continue

                    if Maps[nx][ny] == ".":
                        Maps[nx][ny] = "D"
                    elif Maps[nx][ny] == "W":
                        return 0
    
    return 1

if __name__ == "__main__":
    input = __import__("sys").stdin.readline
    R, C = map(int, input().split())
    Maps = [list(input().strip()) for _ in range(R)]

    map_flag = setup_defence(Maps, R, C)
    print(map_flag)
    if map_flag:
        for m in Maps:
            print("".join(m))