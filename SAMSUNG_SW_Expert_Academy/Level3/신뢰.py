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
    num = int(cmd[0])
    cmd = list(zip(cmd[1::2], map(int, cmd[2::2])))
    count = 0 # 행동 횟수
    index = 0 # 현재 명령순서
    position = {'B':1, 'O':1} # 로봇의 위치
    commands = {'B':-1, 'O':-1} # 로봇의 명령위치
    # print(cmd)

    while index < num:
        # print(count, index, position, commands)
        # 위치설정이 끝난 후
        if commands['B'] != -1:
            push = False
            for name in ['B', 'O']:
                if commands[name] != num:
                    target_pos = cmd[commands[name]][1]
                    # 목적지에 도달한 경우
                    if target_pos == position[name]:
                        # 내 순서가 먼저인 경우
                        # print(f'내순서 {name} {index}=={commands[name]}')
                        if push is False and index == commands[name]: # min(commands.values())
                            push = True
                            index += 1
                            commands[name] = -1
                        else:
                            continue
                    # 목적지가 아닌 경우
                    else:
                        if target_pos > position[name]:
                            position[name] += 1
                        else:
                            position[name] -= 1

            count += 1

        # 각 로봇의 명령위치 가져오기
        for name in ['B', 'O']:
            if commands[name] != num and commands[name] == -1:
                for i in range(index, num):
                    if cmd[i][0] == name:
                        commands[name] = i
                        break
                else:
                    # 더이상 없는 경우
                    commands[name] = num
    answer.append(f'#{tc+1} {count}')

for ans in answer:
    print(ans)
    