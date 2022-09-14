

def solution(rectangle, characterX, characterY, itemX, itemY):
    from collections import deque
    MapData = [[0 for _ in range(101)] for _ in range(101)]

    characterX = characterX*2
    characterY = characterY*2
    itemX = itemX*2
    itemY = itemY*2
    
    # Drawing Line
    for rect in rectangle:
        # 좌표 *2
        for i in range(4): rect[i] = rect[i]*2
        
        for lr in range(rect[3]-rect[1]+1):
            # y축 x축
            MapData[lr+rect[1]][rect[0]] = 1
            MapData[lr+rect[1]][rect[2]] = 1

        for ud in range(rect[2]-rect[0]+1):
            # y축 x축
            MapData[rect[1]][ud+rect[0]] = 1
            MapData[rect[3]][ud+rect[0]] = 1
    
    # Remove Inner
    for rect in rectangle:
        for lr in range(rect[3]-rect[1]-1):
            for ud in range(rect[2]-rect[0]-1):
                MapData[lr+rect[1]+1][ud+rect[0]+1] = 0
    
    

    # DFS (길찾기)
    result = []
    queue = deque()
    queue.append(((characterX,characterY)))
    # MapData[characterY][characterX] = 2
    dx = (0,0,-1,1)
    dy = (1,-1,0,0)

    while queue:
        cx,cy = queue.popleft()
        cnt = MapData[cy][cx]

        if cx == itemX and cy == itemY:
            return (cnt-1)//2

        for d in range(4):
            
            nx = cx+dx[d]
            ny = cy+dy[d]
            if nx > 0 and nx < 101 and ny > 0 and ny < 101:
                if MapData[ny][nx] == 1:
                    MapData[ny][nx] = cnt+1
                    queue.append((nx,ny))

rectangle = [
    [[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]],
    [[1,1,8,4],[2,2,4,9],[3,6,9,8],[6,3,7,7]],
    [[1,1,5,7]],
    [[2,1,7,5],[6,4,10,10]],
    [[2,2,5,5],[1,3,6,4],[3,1,4,6]]
]

characterX = [
    1,
    9,
    1,
    3,
    1
]

characterY = [
    3,
    7,
    1,
    1,
    4
]

itemX = [
    7,
    6,
    4,
    7,
    6
]

itemY = [
    8,
    1,
    7,
    10,
    3
]

result = [
    17,
    11,
    9,
    15,
    10
]

for q in [0,1,2,3,4]:
    qid = solution(rectangle[q], characterX[q], characterY[q], itemX[q], itemY[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')