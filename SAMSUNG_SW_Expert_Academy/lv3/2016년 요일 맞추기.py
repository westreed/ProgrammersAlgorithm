# 5515
# 연습문제

# 입력
'''
2
1 1
12 31

# 답
#1 4
#2 5
'''

testcase = int(input())
answer = ""

# 1월 1일은 금요일
month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for tc in range(testcase):
    M, D = list(map(int, input().split()))
    Days = 3+D

    for m in range(M-1):
        Days += month[m]
    
    Days %= 7
    answer += f"#{tc+1} {Days}\n"

print(answer)