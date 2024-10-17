# 정렬, 값 / 좌표 압축
# https://www.acmicpc.net/problem/18869

"""
2 3
1 3 2
12 50 31
"""

input = __import__("sys").stdin.readline
M, N = map(int, input().split())
planets = [
    tuple(map(int, input().split())) for _ in range(M)
]

from collections import defaultdict

count = defaultdict(int)
for m in range(M):
    union_planet = sorted(list(set(planets[m])))
    # 숫자가 다르면, 같은 구성으로 체크할 수 없으므로 정렬된 순서(index)로 사전을 만듬.
    # 이게 가능한 이유는 같은 구성을 가진 행성 조건이 대소비교이므로 이를 중복없이 정렬하고 인덱스화하면 같아짐.
    rank = {union_planet[i] : i for i in range(len(union_planet))}
    rplanet = tuple([rank[i] for i in planets[m]])
    count[rplanet] += 1

ans = 0
for v in count.values():
    # 같은 구성을 가진 행성이 2개 이상 존재해야 쌍을 이룰 수 있음.
    # 3개부터는 행성의 "쌍"을 구하는 문제이기 때문에, 중복없이 2개의 쌍을 이루는 경우의 수를 구해야함.
    if v > 1:
        ans += (v*(v-1))//2

print(ans)