# 수학, 정수론, 분할 정복을 이용한 거듭제곱, 모듈로 곱셈 역원, 페르마의 소정리
# https://www.acmicpc.net/problem/13172

MOD = 1000000007

def moduler(a, b):
    p = MOD-2
    n = 1
    while p:
        if p & 0x1:
            n = (n*b) % MOD
            p -= 1
        else:
            b = (b*b) % MOD
            p //= 2

    return (a*n) % MOD

if __name__ == "__main__":
    input = __import__("sys").stdin.readline
    M = int(input()) # N, S
    sums = 0
    for _ in range(M):
        n, s = map(int, input().split())
        sums += moduler(s, n)
        if sums >= MOD: sums %= MOD
    
    print(sums)