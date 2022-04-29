# 자료 구조, 우선순위 큐
# https://www.acmicpc.net/problem/1927

import heapq, sys
input=sys.stdin.readline

heap = []
numb = int(input())
text = ''
for _ in range(numb):
    value = int(input())

    if value == 0:
        if heap: text += str(heapq.heappop(heap)) + '\n'
        else: text += '0\n'
    
    else:
        heapq.heappush(heap, value)

print(text)