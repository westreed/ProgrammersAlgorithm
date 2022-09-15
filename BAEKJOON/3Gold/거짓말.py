# 
# https://www.acmicpc.net/problem/1043

import sys
input = sys.stdin.readline

N,M = map(int, input().split()) # 사람의 수, 파티의 수
Truth = list(map(int, input().split())) # Init
Truth = Truth[1:]
Party = []
Relation = [False for _ in range(N+1)] # 진실을 아는 사람 여부

for _ in range(M):
    Party.append(list(map(int, input().split())))

Answer = 0

if Truth[0] == 0: Answer = M
else:
    for t in Truth[1:]:
        Relation[t] = True
    


    
    
    print(Relation)
    print(Party)