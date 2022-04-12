# 2021 카카오 채용연계형 인턴십
# https://programmers.co.kr/learn/courses/30/lessons/81302#fn1
class Seat:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def manhattanDistance(T1, T2):
    lx = abs(T1.x-T2.x)
    ly = abs(T1.y-T2.y)
    dist = lx+ly
    return dist, lx, ly

def keepDistance(maps):
    user = []
    for y in range(5):
        for x in range(5):
            if maps[y][x] == 'P':
                user.append(Seat(x,y))
    
    user_len = len(user)
    for u1 in range(user_len):
        for u2 in range(user_len):
            if u1 != u2:
                user1, user2 = user[u1], user[u2]
                dist, lx, ly = manhattanDistance(user1, user2)
                if dist > 2:  continue
                if dist != 2: return 0
                
                # 대각선에 있는 경우
                if lx == 1 and ly == 1:
                    min_x = min(user1.x, user2.x)
                    min_y = min(user1.y, user2.y)
                    for y in range(2):
                        for x in range(2):
                            if(maps[min_y+y][min_x+x] == 'O'):
                                return 0
                
                # 직선인 경우
                if ly == 0:
                    min_x = min(user1.x, user2.x)
                    y = user1.y
                    if(maps[y][min_x+1] != 'X'):
                        return 0
                if lx == 0:
                    min_y = min(user1.y, user2.y)
                    x = user1.x
                    if(maps[min_y+1][x] != 'X'):
                        return 0
    return 1

def solution(places):
    answer = []
    for p in places:
        answer.append(keepDistance(p))
    return answer

places = [
    [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
]

result = [[1, 0, 1, 1, 1]]

for q in [0]:
    qid = solution(places[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')