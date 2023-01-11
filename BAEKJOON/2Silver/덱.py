# 자료구조, 덱
# https://www.acmicpc.net/problem/10866

# 입력
'''
15
push_back 1
push_front 2
front
back
size
empty
pop_front
pop_back
pop_front
size
empty
pop_back
push_front 3
empty
front
'''

input = __import__('sys').stdin.readline

Deque = []
Res = ''
for _ in range(int(input())):
    cmd = input()

    if cmd.startswith('push_front'):
        Deque.insert(0, int(cmd[10:]))
    elif cmd.startswith('push_back'):
        Deque.append(int(cmd[9:]))
    elif cmd.startswith('pop_front'):
        if Deque:
            num = Deque.pop(0)
            Res += f'{num}\n'
        else:
            Res += f'-1\n'
    elif cmd.startswith('pop_back'):
        if Deque:
            num = Deque.pop()
            Res += f'{num}\n'
        else:
            Res += f'-1\n'
    elif cmd.startswith('size'):
        Res += f'{len(Deque)}\n'
    elif cmd.startswith('empty'):
        if Deque:
            Res += f'0\n'
        else:
            Res += f'1\n'
    elif cmd.startswith('front'):
        if Deque:
            Res += f'{Deque[0]}\n'
        else:
            Res += f'-1\n'
    elif cmd.startswith('back'):
        if Deque:
            Res += f'{Deque[-1]}\n'
        else:
            Res += f'-1\n'

print(Res)