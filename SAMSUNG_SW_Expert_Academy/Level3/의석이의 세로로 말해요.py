# 5356
# 연습문제

# 입력
'''
2
ABCDE
abcde
01234
FGHIJ
fghij
AABCDD
afzz
09121
a8EWg6
P5h3kx

답
#1 Aa0FfBb1GgCc2HhDd3IiEe4Jj
#2 Aa0aPAf985Bz1EhCz2W3D1gkD6x
'''

testcase = int(input())
answer = ""

for tc in range(testcase):
    wordList   = [input().strip() for _ in range(5)]
    wordLength = [len(word) for word in wordList]
    maxRange   = max(wordLength)
    
    ans = f"#{tc+1} "
    for x in range(maxRange):
        for y in range(5):
            if wordLength[y]-1 < x: continue
            ans += wordList[y][x]
    
    answer += ans + '\n'

print(answer)