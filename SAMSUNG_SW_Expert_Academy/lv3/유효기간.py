# 10059
# 연습문제

'''
5
0721
2107
0507
0705
1313
'''

testcase = int(input())
answer = []
for tc in range(testcase):
    number = input().rstrip()
    number = [int(number[:2]), int(number[2:])]
    result = 'NA'
    if 1 <= number[0] <= 12:
        result = 'MMYY'
    if 1 <= number[1] <= 12:
        if result == 'NA':
            result = 'YYMM'
        else:
            result = 'AMBIGUOUS'
    
    answer.append(f'#{tc+1} {result}')

for ans in answer:
    print(ans)