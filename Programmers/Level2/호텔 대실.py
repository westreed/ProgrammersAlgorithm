# 연습문제
# https://school.programmers.co.kr/learn/courses/30/lessons/155651

def numByTime(time):
    hour, mins = map(int, time.split(":"))
    return hour*60 + mins

def solution(book_time):
    from heapq import heappop, heappush
    
    book_time.sort()
    MaxRoom,Rooms,Queue = 0, 0, []
    for room in book_time:
        start, end = map(numByTime, room)

        idx = 0
        while idx < Rooms:
            if Queue[0] <= start:
                heappop(Queue)
                Rooms -= 1
            else:
                idx += 1
        
        heappush(Queue, end+10)
        Rooms += 1
        if MaxRoom < Rooms: MaxRoom = Rooms
    
    return MaxRoom

book_time = [
    [["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]],
    [["09:10", "10:10"], ["10:20", "12:20"]],
    [["10:20", "12:30"], ["10:20", "12:30"], ["10:20", "12:30"]]
]

result = [
    3, 1, 3
]

for q in [0,1,2]:
    qid = solution(book_time[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')