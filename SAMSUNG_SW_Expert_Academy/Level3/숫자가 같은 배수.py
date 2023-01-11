# 14361
# 연습문제

'''
3
142857
1
1035
'''
def countNumber(number:str):
    from collections import defaultdict
    count = defaultdict(int)
    for n in number:
        count[n] += 1
    return count

testcase = int(input())
answer = []
for tc in range(testcase):
    number = input()
    count = countNumber(number)
    number = int(number)

    check = number
    for n in range(10):
        check += number
        _cnt = countNumber(str(check))
        for i in range(10):
            i = str(i)
            if count[i] != _cnt[i]:
                break
        else:
            check = 'possible'
            break
    else:
        check = 'impossible'
    
    answer.append(f'#{tc+1} {check}')

for ans in answer:
    print(ans)