# 구현, 그래프이론
# https://www.acmicpc.net/problem/3098

'''
5 4
1 2
2 3
3 4
4 5
'''

input = __import__('sys').stdin.readline
N, M = map(int, input().split())
Friends = {i : [0, []] for i in range(1, N+1)} # (0명, [관계유형])

def addFriend(lists, A, B):
    a = lists[A]
    a[0] += 1
    a[1].append(B)

    b = lists[B]
    b[0] += 1
    b[1].append(A)

for _ in range(M):
    A, B = map(int, input().split())
    addFriend(Friends, A, B)

Days = [0]
while True:
    import copy

    check = 0
    for n in range(1,N+1):
        if Friends[n][0] == N-1:
            check += 1
    if check == N: break

    Days.append(0)
    # 모두와 친구가 아닌 경우
    Friends_ = copy.deepcopy(Friends)
    for n in range(1, N+1):
        if Friends[n][0] == N-1: continue
        # n의 친구들 m
        for m in Friends_[n][1]:
            # m과 친구인 k
            for k in Friends_[m][1]:
                if n != k and k not in Friends[n][1]:
                    addFriend(Friends, n, k)
                    Days[Days[0]+1] += 1
    
    Days[0] += 1

for d in Days:
    print(d)