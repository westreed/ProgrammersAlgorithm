# 2050
# 연습문제

# 입력
'''
ABCDEFGHIJKLMNOPQRSTUVWXYZ
'''

string = input()
string = list(map(lambda x:str(ord(x)-64), string))
string = " ".join(string)
print(string)