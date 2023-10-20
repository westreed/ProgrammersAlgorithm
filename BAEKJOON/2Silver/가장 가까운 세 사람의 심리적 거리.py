# 브루트포스 알고리즘, 비둘기집 원리
# https://www.acmicpc.net/problem/20529

from collections import defaultdict
input = __import__('sys').stdin.readline
T = int(input())

MBTI = ("ISTJ", "ISFJ", "INFJ", "INTJ", "ISTP", "ISFP", "INFP", "INTP", "ESTP", "ESFP", "ENFP", "ENTP", "ESTJ", "ESFJ", "ENFJ", "ENTJ")

MBTI_Dist = defaultdict(dict)
for first_mbti in MBTI:
    for second_mbti in MBTI:
        dist = len(set(first_mbti+second_mbti))-4
        MBTI_Dist[first_mbti][second_mbti] = dist

for _ in range(T):
    N = int(input())
    _list = input().split()
    _min = 12

    if N > 32:
        print(0)
        continue

    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                _i = _list[i]
                _j = _list[j]
                _k = _list[k]

                _sum = MBTI_Dist[_i][_j]+MBTI_Dist[_i][_k]+MBTI_Dist[_j][_k]
                if _min > _sum:
                    _min = _sum
    
    print(_min)