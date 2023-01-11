# 5293
# 연습문제

# 입력
'''
6
2 2 2 1
0 1 0 0
1 0 0 1
1 1 1 1
2 1 1 2
1 2 3 4
0 1 1 0
'''

'''
불가능
A,D만 있는 경우
B,C의 차이가 2이상인 경우

if B > C: A(BC...B)D
if B < C: D(CB...C)A
110010 A1 B1 C2 D1
if B = C: 

'''

testcase = int(input())
answer = []
for tc in range(testcase):
    a,b,c,d = map(int, input().split())
    string  = ''
    
    if b == c and b != 0:
        string = '01'*b + '1'*d + '0' + '0'*a
    elif b == c+1:
        string = '0'*a + '01'*b + '1'*d
    elif b == c-1:
        string = '1'*d + '10'*c + '0'*a
    elif b == c and a == 0 and d != 0:
        string = '1' + '1'*d
    elif b == c and a != 0 and d == 0:
        string = '0' + '0'*a
    else:
        string = 'impossible'

    answer.append(f'#{tc+1} {string}')
            
for ans in answer:
    print(ans)