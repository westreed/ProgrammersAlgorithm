# 문자열, 해싱
# https://www.acmicpc.net/problem/15829

L = int(input())
String = input().strip()

Hash = 0
for s in range(L):
    idx = ord(String[s])-96
    Hash += idx*pow(31,s)

print(Hash % 1234567891)