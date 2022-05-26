# 10505
# 연습문제

'''
3
7
15 15 15 15 15 15 15
10
1 1 1 1 1 1 1 1 1 100
7
2 7 1 8 2 8 4

1
3
1 2 3
'''

testcase = int(input())
answer = []
for tc in range(testcase):
    number = int(input())
    income = list(map(int, input().split()))
    income.sort()
    average = sum(income) / number

    start = 0
    ends = number-1
    total = 0
    while start <= ends:
        mid = (start+ends)//2
        if income[mid] <= average:
            start = mid+1
            total = max(total, start)
        else:
            ends = mid-1
    
    answer.append(f'#{tc+1} {total}')

for ans in answer:
    print(ans)