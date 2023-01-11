# 7675
# 연습문제

'''
2
2
Annyung Hasae Yo! LoL!
3
my name is Hye Soo. my id is
Rhs0266. what your id Bro?
'''

testcase = int(input())
answer = []
end_string = ['.','?','!']

def compare(string:str) -> tuple:
    re1,re2 = False,False
    if string[-1] in end_string:
        re1 = True
        string = string[:-1]
    
    if string[0].isupper():
        for s in string[1:]:
            if s.isupper() or s.isdecimal():
                break
        else:
            re2 = True

    return (re1, re2)

for tc in range(testcase):
    num = int(input())
    idx = 0
    cnt = [0 for _ in range(num)]
    
    while idx < num:
        sentence = input().split()
        # 나뉘어진 문장 읽기
        for sent in sentence:
            re1,re2 = compare(sent)
            if re2 is True: cnt[idx] += 1
            if re1 is True: idx += 1
    

    answer.append(f'#{tc+1} {" ".join(map(str, cnt))}')

for ans in answer:
    print(ans)