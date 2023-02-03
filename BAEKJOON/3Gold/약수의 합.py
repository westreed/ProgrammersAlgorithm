# 
# https://www.acmicpc.net/problem/17425

# 입력
'''
5
1
2
10
70
10000
'''

MAX = 1000001
Sums = [1 for _ in range(MAX)]

for i in range(2, MAX):
    for j in range(i, MAX, i):
        Sums[j] += i
    
    Sums[i] += Sums[i-1]

input = __import__('sys').stdin.readline
Answer = []
for _ in range(int(input())):
    N = int(input())
    Answer.append(Sums[N])

print("\n".join(map(str, Answer)))