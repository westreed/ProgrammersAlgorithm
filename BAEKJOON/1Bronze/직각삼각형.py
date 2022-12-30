# 수학, 기하학, 피타고라스 정리
# https://www.acmicpc.net/problem/4153

input = __import__('sys').stdin.readline

while True:
    datas = sorted(list(map(int, input().split())))

    if datas == [0, 0, 0]: break

    if datas[0]**2 + datas[1]**2 == datas[2]**2:
        print('right')
    else:
        print('wrong')
