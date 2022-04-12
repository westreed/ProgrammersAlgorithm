# 탐욕법(Greedy)
# https://programmers.co.kr/learn/courses/30/lessons/42860

def solution(name):
    # A~Z (65~90)
    answer  = []
    length  = len(name)
    _name   = [ord(i) for i in name]
    keyword = [65 for _ in range(length)]
    print(keyword)
    

    def index(p):
        if p >= length: return p-length
        elif p < 0:     return length+p
        return p
    
    def dfs(_keyword, pos, action):
        if _keyword == _name:
            answer.append(action)
            return True
        
        act = min(91-_name[pos], _name[pos]-65)
        _keyword[pos] = name[pos]
        action += act
        
        rg = 0
        while True:
            rg += 1
            left  = index(pos-1)
            right = index(pos+1)
            check = False
            if _name[left] != _keyword[left]:
                dfs(_keyword, left, action+1)
                check = True
            if _name[right] != _keyword[right]:  
                dfs(_keyword, right, action+1)
                check = True
                
            if check:
                return False
    
    dfs(keyword, 0, 0)
    print(answer)
        
    
    # while True:
    #     if _name[pos] != keypad[pos]:
    #         # 뒤로 가는게 더 적은지, 앞으로 가는게 더 적은지
    #         act = min(91-_name[pos], _name[pos]-65)
    #         keypad[pos] = _name[pos]
    #         action += act
        
    #     # 정답과 이름이 같은 경우
    #     if keypad == _name: break

    #     pos = index(pos-1)
    #     action += 1



name = [
    "JEROEN",
    "JAN",
    "AAIAPB",
    "LOAAAHAJAAFAEBAWO"
]

result = [
    56,
    23,
    24,
    79
]

for q in [-1]:
    qid = solution(name[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')