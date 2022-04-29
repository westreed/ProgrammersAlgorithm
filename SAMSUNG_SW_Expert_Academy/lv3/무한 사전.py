# 11445
# 연습문제

# 입력
'''
2
cat
dog
man
mana
'''

case = int(input())
for c in range(case):
    word1 = input().strip()
    word2 = input().strip()

    length = len(word1)
    if word1 == word2[:length]\
        and word2[length:] == 'a':
        print(f'#{c+1} N')
    else:
        print(f'#{c+1} Y')