from bisect import bisect_left, bisect_right

lists = [1,-1,4,5,4,1,2,5,10,11]
lists.sort()

def insert(_list, v):
    i = bisect_left(_list, v)
    j = bisect_right(_list, v)
    print(f"{v}는 {_list}에서 {i}번째 index에 삽입했습니다. if Right:{j}")
    _list.insert(i, v)

def find(_list, v):
    i = bisect_left(_list, v)
    j = bisect_right(_list, v)
    res = tuple(range(i-1,j-1))
    return res[0] if len(res) == 1 else res

def count(_list, v):
    i = bisect_left(_list, v)
    j = bisect_right(_list, v)
    return j-i

for v in [11, 3, 4, 5]:
    insert(lists, v)

print(find(lists, 5))
print(count(lists, 5))