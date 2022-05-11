# 10761
# 연습문제

'''
3
4 B 2 O 1 O 2 B 4
3 B 5 B 8 O 100
2 O 2 O 1
'''

testcase = int(input())
answer = []
for tc in range(testcase):
    cmd = input().split()
    num = cmd[0]
    cmd = cmd[1:]
    timer = 0
    index = 0 # 현재 명령순서
    postion = {'B':0, 'O':0} # 로봇의 위치

    while index <= num:
        order = index*2
        tag,btn = cmd[order],cmd[order+1]

        if postion[tag] == btn:
            index += 1
        else:
            
        

