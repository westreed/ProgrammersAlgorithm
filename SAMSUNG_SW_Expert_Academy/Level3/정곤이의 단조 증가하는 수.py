# 6190
# 연습문제

'''
1
4
2 4 7 10
'''

from itertools import combinations

testcase = int(input())
answer = []

def divide(n):
    lst = []
    while n:
        n,t = divmod(n, 10)
        if lst and lst[-1] < t: return False
        lst.append(t)
    return True


for tc in range(testcase):
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()

    result = -1
    for n in map(lambda x:x[0]*x[1], combinations(A, 2)):
        lst = divide(n)
        if lst: result = max(result, n)
    
    answer.append(f'#{tc+1} {result}')

for ans in answer:
    print(ans)