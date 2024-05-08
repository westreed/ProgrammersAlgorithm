# 
# https://www.acmicpc.net/problem/15666

"""
N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

N개의 자연수 중에서 M개를 고른 수열
- 같은 수를 여러 번 골라도 된다.
- 고른 수열은 비내림차순이어야 한다.
- 길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순이라고 한다.
"""

def bfs(N, M, array):
    visit = {}
    queue = [(0, 0, "")]

    while queue:
        idx, dept, string = queue.pop(0)

        if dept == M:
            visit[string] = 0
            print(string.lstrip())
            continue

        for i in range(idx, N):
            res = f"{string} {array[i]}"
            if visit.get(res) is None:
                visit[res] = 0
                queue.append((i, dept+1, res))

if __name__ == "__main__":
    N, M = map(int, input().split())
    array = sorted(list(map(int, input().split())))
    bfs(N, M, array)