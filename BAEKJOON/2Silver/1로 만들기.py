# 다이나믹 프로그래밍
# https://www.acmicpc.net/problem/1463

# 입력
'''
10
>> 3
'''
number = int(input())
maxN   = 10**6
lists  = [0xFFFFFFFF for _ in range(maxN+1)]

def DP(number, lists):
    lists[1] = 0
    for i in range(1,number):
        i2,i3 = i*2,i*3
        lists[i+1] = min(lists[i]+1, lists[i+1])
        if i2 <= maxN: lists[i2] = min(lists[i]+1, lists[i2])
        if i3 <= maxN: lists[i3] = min(lists[i]+1, lists[i3])
    return lists[number]

print(DP(number, lists))