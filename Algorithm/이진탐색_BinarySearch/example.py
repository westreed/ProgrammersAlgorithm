from bisect import bisect_left, bisect_right

lists = [1,-1,4,5,4,1,2,5,10,11]
lists.sort()

for v in [11, 3, 4]:
    i = bisect_left(lists, v)
    j = bisect_right(lists, v)
    print(f"{v}는 {lists}에서 {i}번째 index에 삽입될 수 있습니다. Right:{j}")
    lists.insert(i, v)