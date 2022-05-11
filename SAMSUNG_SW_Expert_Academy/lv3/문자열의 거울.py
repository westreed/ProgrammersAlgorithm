# 10804
# 연습문제

'''
2
bdppq
qqqqpppbbd
'''

testcase = int(input())
mirror = {'b':'d', 'd':'b', 'p':'q', 'q':'p'}
answer = []
for tc in range(testcase):
    string = list(input().rstrip())
    for i in range(len(string)):
        string[i] = mirror[string[i]]
    string.reverse()
    answer.append(f'#{tc+1} {"".join(string)}')

for ans in answer:
    print(ans)
