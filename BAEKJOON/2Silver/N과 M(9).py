# 백트래킹
# https://www.acmicpc.net/problem/15663

if __name__ == "__main__":
    N, M = map(int, input().split())
    Array = sorted(list(map(int, input().split())))
    answer = {}

    from itertools import permutations
    for res in permutations(Array, M):
        answer[res] = 1
    
    for key in answer.keys():
        print(*key)