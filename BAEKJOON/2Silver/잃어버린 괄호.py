# 수학, 문자열, 그리디 알고리즘, 파싱
# https://www.acmicpc.net/problem/1541

from collections import deque

string = input().strip()
values = deque()
answer = 0
save, index = '', 0
for k,v in enumerate(string):
    if v == '+' or v == '-':
        values.append(int(save))
        values.append(v)
        save, index = '', k
    else: save += v
else:
    if save != '': values.append(int(save))
    else: values.append(int(string[index+1:]))

answer = values.popleft()
save_sign, save_value = False, 0
while values:
    sign = values.popleft()
    value = values.popleft()

    if save_sign is False:
        if sign == '-':
            save_value += value
            save_sign = True
        else:
            answer += value
    else:
        save_value += value

answer -= save_value

print(answer)