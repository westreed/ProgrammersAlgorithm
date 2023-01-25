# 정렬, 값 / 좌표 압축
# https://www.acmicpc.net/problem/18870

N = int(input())
List = list(map(int, input().split()))
Data = {num:idx for idx, num in enumerate(sorted(list(set(List))))}
print(*map(lambda x:Data[x], List))