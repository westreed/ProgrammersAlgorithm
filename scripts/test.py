from collections import deque
from copy import deepcopy
import time

testData = list(range(200000))
length = len(testData)
test1 = deepcopy(testData)
test2 = deque(deepcopy(testData))
test3 = {idx:data for idx, data in enumerate(testData)}

def test_delete(object):
    pt = time.time()

    idx, tog = 0, False
    while len(object):
        try:
            if tog is False:
                del object[idx]
                idx += 1
            else:
                del object[idx]
                idx -= 1
        except:
            idx -= 1
            tog = True
    
    print(f"TEST {str(object.__class__)[8:-2]} :: {time.time()-pt:.7}s")

print("삭제연산 (del) 속도비교")
test_delete(test1)
test_delete(test2)
test_delete(test3)

test1 = deepcopy(testData)
test2 = deque(deepcopy(testData))
test3 = {idx:data for idx, data in enumerate(testData)}

def test_seqread(object):
    pt = time.time()

    prev = 0
    for i in range(length):
        if object[i] < prev:
            pass
        prev = i
    
    print(f"TEST {str(object.__class__)[8:-2]} :: {time.time()-pt:.7}s")


print("순차 접근 실험")
test_seqread(test1)
test_seqread(test2)
test_seqread(test3)