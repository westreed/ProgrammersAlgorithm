# 7584
# 연습문제

# 입력
'''
4
3
7
10
100000
'''

# def f(A):
#     return "".join(["0" if a == "1" else "1" for a in A])

# def g(A):
#     return A[::-1]

testcase = int(input())
answer = ""
P = "0"

def gf(A):
    i = len(A)//2
    j = "0" if A[i] == "1" else "1"
    return A[:i] + j + A[i+1:]

for _ in range(30):
    P += "0" + gf(P) #f(g(P))

for tc in range(testcase):
    idx = int(input())
    while True:
        if len(P) >= idx:
            answer += f"#{tc+1} {P[idx-1]}"
            break
        else:
            P += "0" + gf(P)