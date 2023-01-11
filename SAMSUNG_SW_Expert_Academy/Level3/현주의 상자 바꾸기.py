# 5789
# 연습문제

# 입력
'''
1
5 2
1 3
2 4

답
#1 1 2 2 2 0
'''

testcase = int(input())
answer = ''

for tc in range(testcase):
    N, M = list(map(int, input().split()))
    Box = [0 for _ in range(N)]

    for i in range(M):
        L, R = list(map(int, input().split()))
        for j in range(L-1, R):
            Box[j] = i+1
    
    ans = " ".join(map(str, Box))
    answer += f"#{tc+1} {ans}\n"

print(answer)