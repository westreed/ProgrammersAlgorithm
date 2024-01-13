# 다이나믹 프로그래밍, 문자열
# https://www.acmicpc.net/problem/9251

if __name__ == "__main__":
    A, B = input().rstrip(), input().rstrip()
    Al,Bl = len(A), len(B)
    lcs = [0] * Al

    for b in range(Bl):
        cnt = 0
        for a in range(Al):
            if lcs[a] > cnt:
                cnt = lcs[a]
            elif A[a] == B[b]:
                lcs[a] = cnt + 1
    
    print(max(lcs))