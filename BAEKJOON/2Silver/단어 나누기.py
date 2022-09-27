# 구현, 문자열, 브루트포스 알고리즘, 정렬
# https://www.acmicpc.net/problem/1251

'''
mobitel
bomitel
'''
import heapq

string = input().strip()
length = len(string)
splits = []

for i in range(length-2):
    for j in range(i+1, length-1):
        spl = string[0:i+1][::-1] + string[i+1:j+1][::-1] + string[j+1:][::-1]
        heapq.heappush(splits, spl)

print(splits[0])