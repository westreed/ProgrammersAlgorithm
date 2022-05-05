# 구현, 문자열
# https://www.acmicpc.net/problem/10809

string = input().strip()
alphabet = {chr(id+97) : '-1' for id in range(26)}

for k,v in enumerate(string):
    if alphabet[v] == '-1':
        alphabet[v] = str(k)

print(' '.join(list(alphabet.values())))