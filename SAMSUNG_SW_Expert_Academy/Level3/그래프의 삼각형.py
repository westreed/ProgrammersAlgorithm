# 6057
# 연습문제

'''
1
4 5
1 2
2 3
1 3
1 4
3 4
'''
import itertools

testcase = int(input())
answer = []

for tc in range(testcase):
    N,M = map(int, input().split())
    Nodes = [[False for _ in range(N+1)] for _ in range(N+1)]
    Total = 0
    for _ in range(M):
        n1,n2 = map(int, input().split())
        Nodes[n1][n2] = True

    print(Nodes)
    Tri = list(itertools.combinations(range(1,N+1), 3))
    for T in Tri:
        a,b,c = T
        print(T, end=' ')
        if Nodes[a][b] and Nodes[b][c] and Nodes[a][c]:
            print('O')
            Total += 1
        else:
            print('X')

    
    answer.append(f'#{tc+1} {Total}')

for ans in answer:
    print(ans)