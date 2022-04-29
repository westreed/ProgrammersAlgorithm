# 
# https://www.acmicpc.net/problem/1541

from copy import deepcopy
from itertools import permutations

string = input().strip()
values = []
answer = []
save,point = '',0
signs  = 0
for k,v in enumerate(string):
    if v == '+' or v == '-':
        values.append(int(save))
        values.append(v)
        save,point = '',k
        signs += 1
    else: save += v
else: values.append(int(string[point+1:]))

print(values)
for order in permutations(range(signs)):
    tables = []
    for o in order:
        