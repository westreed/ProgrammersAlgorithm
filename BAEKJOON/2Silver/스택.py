# 자료구조, 스택
# https://www.acmicpc.net/problem/10828

# 입력
'''
14
push 1
push 2
top
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
top
'''

input = __import__('sys').stdin.readline

Stack = []
Res = ''
for _ in range(int(input())):
    cmd = input()

    if cmd.startswith('push'):
        Stack.append(int(cmd[5:]))
    elif cmd.startswith('pop'):
        if Stack:
            num = Stack.pop()
            Res += f'{num}\n'
        else:
            Res += f'-1\n'
    elif cmd.startswith('size'):
        Res += f'{len(Stack)}\n'
    elif cmd.startswith('empty'):
        if Stack:
            Res += f'0\n'
        else:
            Res += f'1\n'
    elif cmd.startswith('top'):
        if Stack:
            Res += f'{Stack[-1]}\n'
        else:
            Res += f'-1\n'

print(Res)