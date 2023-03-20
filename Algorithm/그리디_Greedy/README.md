# 그리디 (Greedy)


## 그리디 알고리즘이란?

* 주어진 상황에서 지금 이 순간 당장 최적인 답을 선택하여 적합한 결과를 도출하는 것
* 문제를 풀기 위한 최소한의 아이디어를 떠올릴 수 있는 능력을 요구함
* 떠올린 아이디어에 대한 정당성 분석이 중요

## <문제> 잃어버린 괄호

출처 : [잃어버린 괄호](https://www.acmicpc.net/problem/1541)

세준이는 양수와 +, -, 그리고 괄호를 가지고 식을 만들었다. 그리고 나서 세준이는 괄호를 모두 지웠다. 그리고 나서 세준이는 괄호를 적절히 쳐서 이 식의 값을 최소로 만들려고 한다. 괄호를 적절히 쳐서 이 식의 값을 최소로 만드는 프로그램을 작성하시오.<br><br>

첫째 줄에 식이 주어진다. 식은 ‘0’~‘9’, ‘+’, 그리고 ‘-’만으로 이루어져 있고, 가장 처음과 마지막 문자는 숫자이다. 그리고 연속해서 두 개 이상의 연산자가 나타나지 않고, 5자리보다 많이 연속되는 숫자는 없다. 수는 0으로 시작할 수 있다. 입력으로 주어지는 식의 길이는 50보다 작거나 같다.

## 문제 해결 아이디어

- 최소값으로 만들기 위해서는 음수의 값이 커야한다.
- 음수 기호가 나왔을 때, 다시 음수 기호가 나오기 전까지 묶어서 계산해주면 가장 큰 음수가 만들어진다.


```python
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
```