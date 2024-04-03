# 구현, 정렬
# https://www.acmicpc.net/problem/30619

"""
5
1 3 4 2 5
3
2 3
3 5
1 5
"""

if __name__ == "__main__":
    N = int(input())
    house = list(map(int, input().split()))

    Q = int(input())
    for _ in range(Q):
        L, R = map(int, input().split()) # 사람번호임 house의 값
        _house = house[:]
        _cache1 = []
        _cache2 = []

        # O(n)
        for i in range(N):
            if L <= _house[i] <= R:
                _cache1.append(_house[i])
                _cache2.append(i)
        
        _cache1.sort()
        for i, idx in enumerate(_cache2):
            _house[idx] = _cache1[i]
        print(*_house)