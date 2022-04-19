# 1989
# 연습문제

# 입력
'''
3
level
samsung
eye
'''

case = int(input())
for c in range(case):
    string = input()
    if string == string[::-1]: print(f'#{c+1} 1')
    else:                      print(f'#{c+1} 0')