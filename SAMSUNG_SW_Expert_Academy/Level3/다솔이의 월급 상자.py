# 6692
# 연습문제

'''
1
2
0.3 100
0.7 1
'''

testcase = int(input())
answer = []

for tc in range(testcase):
    case = int(input())
    pays = []
    for _ in range(case):
        t1,t2 = input().split()
        pays.append((float(t1), int(t2)))
    
    answer.append(f'#{tc+1} {sum([p[0]*p[1] for p in pays])}')

for ans in answer:
    print(ans)