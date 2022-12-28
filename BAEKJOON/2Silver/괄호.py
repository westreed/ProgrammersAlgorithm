# 자료 구조, 문자열, 스택
# https://www.acmicpc.net/problem/9012

# 입력
'''
6
(())())
(((()())()
(()())((()))
((()()(()))(((())))()
()()()()(()()())()
(()((())()(
'''

input = __import__('sys').stdin.readline
testcase = int(input())

for _ in range(testcase):
    parenthesis = input().strip()
    cnt = [0, 0]
    res = 'YES'
    pair = 0

    for par in parenthesis:
        if par == '(':
            cnt[0] += 1
            pair += 1
        
        else:
            if pair == 0:
                res = 'NO'
                break
            
            cnt[1] += 1
            pair -= 1
    
    if cnt[0] != cnt[1] or pair != 0:
        res = 'NO'
    
    print(res)