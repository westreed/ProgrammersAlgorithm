# 5162
# 연습문제

# 입력
'''
2
3 5 6
6 8 20

답
#1 2
#2 3
'''

testcase = int(input())
answer = ""

for tc in range(testcase):
    A,B,C = map(int, input().split())
    A,B = min(A,B), max(A,B)
    
    _A, R = divmod(C, A)
    _B, R = divmod(R, B)

    answer += f"#{tc+1} {_A+_B}\n"

print(answer)