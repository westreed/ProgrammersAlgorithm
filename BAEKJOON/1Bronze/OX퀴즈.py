# 구현, 문자열
# https://www.acmicpc.net/problem/8958

case = int(input())
result = ''
for c in range(case):
    string = input().strip()
    _check = 0
    _score = 0
    for s in string:
        if s == 'O':
            _check += 1
            _score += _check
        else:
            _check = 0
    result += f'{_score}\n'
print(result)