# 자료구조, 큐
# https://www.acmicpc.net/problem/10845

# 입력
'''
15
push 1
push 2
front
back
size
empty
pop
pop
pop
size
empty
pop
push 3
empty
front
'''

input = __import__('sys').stdin.readline

Queue = []
Res = ''
for _ in range(int(input())):
    cmd = input()

    if cmd.startswith('push'):
        Queue.append(int(cmd[5:]))
    elif cmd.startswith('pop'):
        if Queue:
            num = Queue.pop(0)
            Res += f'{num}\n'
        else:
            Res += f'-1\n'
    elif cmd.startswith('size'):
        Res += f'{len(Queue)}\n'
    elif cmd.startswith('empty'):
        if Queue:
            Res += f'0\n'
        else:
            Res += f'1\n'
    elif cmd.startswith('front'):
        if Queue:
            Res += f'{Queue[0]}\n'
        else:
            Res += f'-1\n'
    elif cmd.startswith('back'):
        if Queue:
            Res += f'{Queue[-1]}\n'
        else:
            Res += f'-1\n'

print(Res)