# 10570
# 연습문제

'''
3
1 9
10 99
100 1000
'''

# 1, 4, 9, 121, 484

def isNotPalindrome(N):
    N = str(N)
    for i in range(len(N)//2):
        if N[i] != N[-(i+1)]:
            return True
    return False

testcase = int(input())
testlist = [-1 for _ in range(1001)]
answer = []
for tc in range(testcase):
    A,B = map(int, input().split())
    total = 0

    for i in range(A,B+1):
        if testlist[i] == -1:
            if isNotPalindrome(i):
                testlist[i] = False
            else:
                root = pow(i, 0.5)
                if int(root) == root:
                    if isNotPalindrome(int(root)):
                        testlist[i] = False
                    else:
                        testlist[i] = True
                        total += 1
                else:
                    testlist[i] = False
        elif testlist[i] == True:
            total += 1
    
    answer.append(f'#{tc+1} {total}')

for ans in answer:
    print(ans)
