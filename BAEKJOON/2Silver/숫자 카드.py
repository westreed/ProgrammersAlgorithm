# 자료 구조, 정렬, 이분 탐색, 해시를 사용한 집합과 맵
# https://www.acmicpc.net/problem/10815

input = __import__("sys").stdin.readline
N = int(input())
cards = set(map(int, input().split()))
M = int(input())
finds = list(map(int, input().split()))

answer = []
for k in finds:
    if k in cards:
        answer.append("1")
    else:
        answer.append("0")

print(" ".join(answer))