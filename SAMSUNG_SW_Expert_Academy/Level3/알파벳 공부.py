# 15230
# 연습문제

# 입력
'''
5
abcdefghijklmnopqrstu
abcdefghijklmnopqrstuvwzyx
abcefghijk
xyz
absolute
'''

ans = ""
tc = int(input())
for t in range(tc):
    ans += f"#{t+1} "
    abc = input().strip()
    idx = 96 # ord("a")-1
    for s in range(len(abc)):
        check = ord(abc[s])
        if idx+1 != check:
            ans += f"{s}\n"
            break
        idx = check
    else:
        ans += f"{len(abc)}\n"

print(ans)