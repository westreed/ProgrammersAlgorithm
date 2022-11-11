# 9700
# 연습문제

# 입력
'''
2
0.8 0.5
0.6 0.5
'''

tc = int(input())
ans = ""
for t in range(tc):
    p,q = map(float, input().split())
    s1 = (1-p)*q
    s2 = p*(1-q)*q
    if s1 < s2:
        ans += f"#{t+1} YES\n"
    else:
        ans += f"#{t+1} NO\n"

print(ans)