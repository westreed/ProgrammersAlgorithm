# 14555
# 연습문제

# 입력
'''
3
||||||
(|..|)
.|.(|...||)|...()..
'''

ans = ""
tc = int(input())
for t in range(tc):
    field = input().strip()
    field = field.replace("()", "(").replace(")", "(")
    count = field.count("(")
    ans += f"#{t+1} {count}\n"
print(ans)