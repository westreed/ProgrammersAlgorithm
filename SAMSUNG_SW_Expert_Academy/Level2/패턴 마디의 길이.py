# 2007
# 연습문제

# 입력
'''
3
KOREAKOREAKOREAKOREAKOREAKOREA
SAMSUNGSAMSUNGSAMSUNGSAMSUNGSA
GALAXYGALAXYGALAXYGALAXYGALAXY
'''

case = int(input())
for c in range(case):
    string  = input()
    length  = 30
    pattern = string[0]
    for s in range(1, length):
        # s는 패턴의 길이이기도 함
        # compare
        for t in range(s, length, s):
            idx  = t
            last = idx+s
            if last > length: continue
            print(s, idx, last, pattern, string[idx:last])
            if pattern != string[idx:last]: break
        else: break

        pattern += string[s]
    print(f'#{c+1} {len(pattern)}')