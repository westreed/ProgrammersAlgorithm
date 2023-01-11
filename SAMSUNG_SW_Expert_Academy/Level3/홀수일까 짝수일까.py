# 5549
# 연습문제

# 입력
'''
5
1
10
100
185787124368712386825387273871
82518881239123819238912929292

답
#1 Odd
#2 Even
#3 Even
#4 Odd
#5 Even
'''

testcase = int(input())
answer = ""

for tc in range(testcase):
    Last = int(input().strip()[-1])
    if Last % 2:
        answer += f"#{tc+1} Odd\n"
    else:
        answer += f"#{tc+1} Even\n"

print(answer)
