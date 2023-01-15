# 자료 구조, 그래프 이론, 그래프 탐색, 분리 집합
# https://www.acmicpc.net/problem/1043

input = __import__('sys').stdin.readline

def MaxLiarParty():
    N,M = map(int, input().split()) # 사람의 수, 파티의 수
    Truth = set(list(map(int, input().split()))[1:]) # Init
    Party = [set(list(map(int, input().split()))[1:]) for _ in range(M)]
    
    if Truth:
        while True:
            isLoop = False
            for some_party in Party:
                if Truth & some_party:
                    diff = some_party - Truth
                    if diff:
                        Truth.update(diff)
                        isLoop = True
            
            if isLoop is False:
                break
        
        for some_party in Party:
            if Truth & some_party:
                M -= 1
    
    return M

        
print(MaxLiarParty())