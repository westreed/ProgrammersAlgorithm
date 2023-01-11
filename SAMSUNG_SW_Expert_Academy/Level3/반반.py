# 11856
# 연습문제

# 입력
'''
5
ABAB
CCDD
EFFE
EEEE
NONE
'''

case = int(input())
for c in range(case):
    string = list(input().strip())
    letter = [string.count(l) for l in set(string)]
    if len(letter) == 2 and letter[0] == 2:
        print(f'#{c+1} Yes')
    else:
        print(f'#{c+1} No')