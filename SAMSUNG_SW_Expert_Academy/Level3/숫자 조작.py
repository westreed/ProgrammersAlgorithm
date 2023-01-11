# 13428
# 연습문제

# 입력
'''
6
10000
1520
11110
10101
99450
11520
21320
9900321
142857
12121
'''

# 결과
'''
10000 10000
1025 5120
10111 11110
10011 11100
49950 99540
10521 51120
12320 31220
1900329 9930021
124857 842157
11122 21121
'''

case = int(input())
for c in range(case):
    number = input().rstrip()
    maxv, minv = number, number
    number = list(number)
    length = len(number)

    # 최대값 구하기
    _number = number[:]
    index   = 0
    front   = 0
    while True:
        if index == length: break
        for i in range(length-1, index, -1):
            if _number[i] > _number[front]:
                front = i
        # 프론트보다 큰 값이 있는 경우
        if front != index:
            _number[index], _number[front] = _number[front], _number[index]
            maxv = "".join(_number)
            break
        else:
            index += 1
            front = index

    # 최소값 구하기
    _number = number[:]
    index   = 0
    front   = 0
    while True:
        if index == length: break
        for i in range(length-1, index, -1):
            if _number[i] < _number[front]:
                if _number[i] == '0':
                    if index > 0:
                        front = i
                else:
                    front = i

        # 프론트보다 작은 값이 있는 경우
        if front != index:
            _number[index], _number[front] = _number[front], _number[index]
            minv = "".join(_number)
            break
        else:
            index += 1
            front = index

    print(f'#{c+1} {minv} {maxv}')
