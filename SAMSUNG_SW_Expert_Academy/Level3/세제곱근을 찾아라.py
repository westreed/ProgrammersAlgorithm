# 5688
# 연습문제

# 입력
'''
4
7999
27
7777
64
'''

testcase = int(input())
answer = ''

for tc in range(testcase):
    N = int(input())
    A = round(N**(1/3), 3)
    if int(A) == A:
        answer += f"#{tc+1} {int(A)}\n"
    else:
        answer += f"#{tc+1} -1\n"

print(answer)