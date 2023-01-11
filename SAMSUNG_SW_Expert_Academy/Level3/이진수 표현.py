# 10726
# 연습문제

testcase = int(input())
answer = []
for tc in range(testcase):
    N,M = map(int, input().split())
    M = str(bin(M))[::-1]
    
    result = True
    for n in range(N):
        if M[n] != '1':
            result = False
            break
    
    if result: answer.append(f'#{tc+1} ON')
    else: answer.append(f'#{tc+1} OFF')

for ans in answer:
    print(ans)