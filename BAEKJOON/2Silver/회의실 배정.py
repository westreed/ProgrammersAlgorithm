# 그리디 알고리즘, 정렬
# https://www.acmicpc.net/problem/1931

# 입력
'''
11
1 4
3 5
0 6
5 7
3 8
5 9
6 10
8 11
8 12
2 13
12 14
'''

# Try 1
# 50860 KB	332 ms

input = __import__('sys').stdin.readline

Number = int(input())
Meeting = []
FlowTime = 0
Answer = 0

for _ in range(Number):
    meetdata = list(map(int, input().split()))
    meetdata = [meetdata[1]-FlowTime] + meetdata
    Meeting.append(meetdata)

Meeting.sort()

index = 0
while index < Number:
    _, start, end = Meeting[index]
    if start >= FlowTime:
        FlowTime += end-FlowTime
        Answer += 1
    
    index += 1

print(Answer)

# Try 2
# 59204 KB	316 ms

input = __import__('sys').stdin.readline

Number = int(input())
Meeting = []
FlowTime = 0
Answer = 0

for _ in range(Number):
    meetdata = list(map(int, input().split()))
    Meeting.append(meetdata)

Meeting.sort(key=lambda x:(x[1],x[0]))

index = 0
while index < Number:
    start, end = Meeting[index]
    if start >= FlowTime:
        FlowTime += end-FlowTime
        Answer += 1
    
    index += 1

print(Answer)