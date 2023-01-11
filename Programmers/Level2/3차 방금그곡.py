# 2018 KAKAO BLIND RECRUITMENT
# https://programmers.co.kr/learn/courses/30/lessons/17683

def timeTnum(time):
    H,M = time.split(':')
    return int(H)*60+int(M)

def solution(m, musicinfos):
    import heapq
    
    answer = []
    re = {'C#':'1', 'D#':'2', 'F#':'3', 'G#':'4', 'A#':'5'}
    for k,v in re.items():
        m = m.replace(k,v)

    for mi in musicinfos:
        start,end,name,sound = mi.split(',')

        for k,v in re.items():
            sound = sound.replace(k,v)

        length = timeTnum(end)-timeTnum(start)
        sound_length = len(sound)
        if sound_length > length:
            sound = sound[:length]
        else:
            repeat,tail = divmod(length, sound_length)
            _temp = sound*repeat
            _temp += sound[:tail]
            sound = _temp
        if m in sound: heapq.heappush(answer, [-length,name])
    
    if answer: return heapq.heappop(answer)[1]
    else: return '(None)'




m = [
    "ABCDEFG",
    "CC#BCC#BCC#BCC#B",
    "ABC"
]

musicinfos = [
    ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"],
    ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"],
    ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]
]

result = [
    "HELLO",
    "FOO",
    "WORLD"
]

for q in [0,1,2]:
    qid = solution(m[q], musicinfos[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')