# 10200
# 연습문제

'''
3
10 3 5
10 7 5
100 100 100
'''

testcase = int(input())
answer = []
for tc in range(testcase):
    N,A,B = map(int, input().split())
    Max = min(A,B)
    Min = A+B-N if (A+B)>=N else 0
    answer.append(f'#{tc+1} {Max} {Min}')

for ans in answer:
    print(ans)