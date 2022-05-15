# 자료구조, 이분탐색
# https://www.acmicpc.net/problem/1920

N = int(input())
N_lists = list(map(int, input().split()))
M = int(input())
M_lists = list(map(int, input().split()))

N_lists.sort()
print(N_lists)

def find(value):
    start = 0
    ends = N-1

    while start <= ends:
        mid = (start+ends)//2
        print(start,ends,mid)
        if N_lists[mid] == value:
            return 1
        
        if N_lists[mid] < value:
            start = mid+1
        else:
            ends = mid-1
    return 0

for m in M_lists:
    print(find(m))