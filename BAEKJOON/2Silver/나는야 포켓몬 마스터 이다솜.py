# 자료 구조, 해시를 사용한 집합과 맵
# https://www.acmicpc.net/problem/1620

import sys
input=sys.stdin.readline

M,N = map(int, input().split())
Pokemon = []
PokemonDict = {}

index = 1
for _ in range(M):
    name = input().strip()
    Pokemon.append(name)
    PokemonDict[name] = index
    index += 1

for _ in range(N): 
    cmd = input().strip()
    try: cmd = int(cmd)
    except: pass

    if type(cmd) is int: result = Pokemon[cmd-1]     
    else: result = PokemonDict[cmd]

    print(result)