# 14692
# 연습문제

# 입력
'''
5
2
3
10
50
100
'''

ans = ""
tc = int(input())
for t in range(tc):
    ans += f"#{t+1} "
    N = int(input())
    if N % 2 == 0: ans += "Alice\n"
    else: ans += "Bob\n"

print(ans)