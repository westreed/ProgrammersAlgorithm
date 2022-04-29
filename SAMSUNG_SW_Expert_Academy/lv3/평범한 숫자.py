# 11736
# 연습문제

# 입력
'''
2
3
1 3 2
5
1 3 5 4 2
'''

case = int(input())
for c in range(case):
    length = int(input())
    lists  = list(map(int, input().split()))
    answer = 0

    for i in range(1, length-1):
        v1,v2,v3 = lists[i-1], lists[i], lists[i+1]
        minv = min(v1,v2,v3)
        maxv = max(v1,v2,v3)
        if minv != v2 and maxv != v2:
            answer += 1

    print(f'#{c+1} {answer}')