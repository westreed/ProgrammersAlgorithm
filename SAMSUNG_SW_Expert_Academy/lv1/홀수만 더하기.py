# 2072
# 연습문제

# 입력
'''
3
3 17 1 39 8 41 2 32 99 2
22 8 5 123 7 2 63 7 3 46
6 63 2 3 58 76 21 33 8 1
'''

# 문제풀이
case = int(input())
for c in range(case):
    problemList = (list(map(int, input().split()))) # 업로드할 땐 input으로 받기
    total = sum(list(map(lambda x : x if x % 2==1 else 0, problemList)))
    print(f'#{c+1} {total}')