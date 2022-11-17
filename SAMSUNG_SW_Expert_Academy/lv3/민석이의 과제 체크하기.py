# 5431
# 연습문제

# 입력
'''
2
5 3
2 5 3
7 2
4 6

답
#1 1 4
#2 1 2 3 5 7
'''

testcase = int(input())
answer = ""

for tc in range(testcase):
    N, K = map(int, input().split())
    K_List = sorted(list(map(int, input().split())))
    
    ans = f"#{tc+1}"
    idx = 0
    for n in range(N):
        for k in range(idx, K):
            if K_List[k] == n+1:
                idx = k+1
                break
        else:
            ans += f" {n+1}"
    answer += ans + "\n"

print(answer)