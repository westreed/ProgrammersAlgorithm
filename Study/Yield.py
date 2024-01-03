
def yield_func():
    for i in range(10):
        print("안녕하세요.", i)
        yield i

res = yield_func()
print(res)
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))