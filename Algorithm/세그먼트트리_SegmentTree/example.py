arr = [1,2,3,4,5,6,7,8,9,10,]
tree = [0] * (len(arr)*4)

# size 50 > tree크기 72??
call_def = 0

def init(left_node=0, right_node=len(arr)-1, node=1):
    if left_node == right_node:
        tree[node] = arr[left_node]
        return tree[node]
    mid = (left_node+right_node)//2
    tree[node] = init(left_node, mid, node*2) + init(mid+1, right_node, node*2+1)
    return tree[node]

def segment_sum(start, end, left_node=0, right_node=len(arr)-1, node=1):
    global call_def
    # 범위 밖에 있는 경우
    call_def += 1
    if start > right_node or end < left_node:
        return 0
    # 범위 안에 있는 경우
    if start <= left_node and end >= right_node:
        print(f"구간 {left_node}~{right_node} : {tree[node]}")
        return tree[node]
    mid = (left_node+right_node)//2
    return segment_sum(start, end, left_node, mid, node*2) + segment_sum(start, end, mid+1, right_node, node*2+1)

def update(index, value, left_node=0, right_node=len(arr)-1, node=1):
    if index < left_node or index > right_node:
        return
    # 범위 안에 있으면
    tree[node] += value-arr[index]
    if left_node == right_node:
        return
    mid = (left_node + right_node)//2
    update(index, value, left_node, mid, node*2)
    update(index, value, mid+1, right_node, node*2+1)


init() # segment tree init
print(tree)

t = segment_sum(2, 9)
print(f"합은 {t}, 함수는 {call_def}번 호출되었습니다.")

update(2, 10)
print(tree)