import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print(f"{func.__name__} 시작 : {start_time}")
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} 종료 : {end_time}")
        print(f"{func.__name__} 경과 : {end_time - start_time}")
        return result
    return wrapper

# INPUT
_input = list(range(1,50))
_k = 5

# itertools.combinations
from itertools import combinations

@timer
def test_case1():
    res = list(combinations(_input, _k))
    print(res[:10])

test_case1()

# yield

@timer
def test_case2():
    def combine(prefix, nums, k):
        if k == 0:
            yield prefix
            return

        if not nums:
            return
        
        yield from combine(prefix + [nums[0]], nums[1:], k-1)
        yield from combine(prefix, nums[1:], k)
    
    res = list(combine([], _input[:], _k))
    print(res[:10])

test_case2()


"""
test_case1 시작 : 1704262412.7967374
[(1, 2, 3, 4, 5), (1, 2, 3, 4, 6), (1, 2, 3, 4, 7), (1, 2, 3, 4, 8), (1, 2, 3, 4, 9), (1, 2, 3, 4, 10), (1, 2, 3, 4, 11), (1, 2, 3, 4, 12), (1, 2, 3, 4, 13), (1, 2, 3, 4, 14)]
test_case1 종료 : 1704262412.9538789
test_case1 경과 : 0.15714144706726074

test_case2 시작 : 1704262412.9538789
[[1, 2, 3, 4, 5], [1, 2, 3, 4, 6], [1, 2, 3, 4, 7], [1, 2, 3, 4, 8], [1, 2, 3, 4, 9], [1, 2, 3, 4, 10], [1, 2, 3, 4, 11], [1, 2, 3, 4, 12], [1, 2, 3, 4, 13], [1, 2, 3, 4, 14]]
test_case2 종료 : 1704262417.869848
test_case2 경과 : 4.915969133377075

<--- 결론 --->
당연히, yield를 쓴게 느리겠지만 코딩테스트 문제를 풀 때 Permutations이나 Combinations의 중간과정에 직접 개입해서 작성이 가능하고 yield는 하나씩 호출하면 next yield가 계산될 때까지만 실행되기 때문에 모든 케이스를 계산할 필요가 없을 때도 좋다.
"""