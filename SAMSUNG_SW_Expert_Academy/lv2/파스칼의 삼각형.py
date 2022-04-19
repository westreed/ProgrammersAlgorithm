# 2005
# 연습문제

# 입력
'''
1
4
'''

case = int(input())
for c in range(case):
    num = int(input())
    print(f'#{c+1}')

    triangle = []
    for i in range(num):
        triangle.append([])
        for j in range(i+1):
            if j == 0 or j == i: triangle[i].append(1)
            else: triangle[i].append(triangle[i-1][j-1] + triangle[i-1][j])
        print(f'{" ".join(map(str, triangle[i]))}')
        