# 13428
# 연습문제

# 입력
'''
4
12345
54321
142857
10000
9990008
5544332211
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
        for i in range(index+1,length):
            if _number[i] > _number[front]:
                front = i
        # 프론트보다 큰 값이 있는 경우
        if front != index:
            _temp = _number[index]
            _number[index] = _number[front]
            _number[front] = _temp
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
        for i in range(index+1,length):
            if _number[i] < _number[front]:
                if _number[i] == '0':
                    if index > 0:
                        front = i
                else:
                    front = i

        # 프론트보다 작은 값이 있는 경우
        if front != index:
            _temp = _number[index]
            _number[index] = _number[front]
            _number[front] = _temp
            minv = "".join(_number)
            break
        else:
            index += 1
            front = index

    print(f'#{c+1} {minv} {maxv}')
