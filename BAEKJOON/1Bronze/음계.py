# 구현
# https://www.acmicpc.net/problem/2920

playing = input().strip()
if   playing == '1 2 3 4 5 6 7 8':
    print('ascending')
elif playing == '8 7 6 5 4 3 2 1':
    print('descending')
else:
    print('mixed')