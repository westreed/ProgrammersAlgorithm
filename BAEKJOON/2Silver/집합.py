# 구현, 비트마스킹
# https://www.acmicpc.net/problem/11723

input = __import__('sys').stdin.readline
M = int(input())
Set = set()
All = [i for i in range(1, 21)]

Command = {
    'add'   : lambda x: Set.add(x),
    'remove': lambda x: Set.remove(x) if Set & {x} else False,
    'check' : lambda x: print(1) if Set & {x} else print(0),
    'toggle': lambda x: Set.remove(x) if Set & {x} else Set.add(x),
    'all'   : lambda _: Set.update(All),
    'empty' : lambda _: Set.clear()
}

for _ in range(M):
    Trigger, *Value = input().split()
    if Value: Value = int(Value[0])
    else: Value = 0
    Command[Trigger](Value)