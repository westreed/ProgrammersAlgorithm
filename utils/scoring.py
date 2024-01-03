def Scoring(solution, *args, **kwargs):
    result = kwargs["result"]
    del kwargs["result"]

    _case = len(result) # 정답 수만큼 케이스 존재
    _args = list(zip(*args, *kwargs.values()))

    for c in range(_case):
        # _res = globals()["solution"](*_args[c])
        _res = solution(*_args[c])
        if _res == result[c]:
            print(f"#{c}. correct | {_res}")
        else:
            print(f"#{c}. incorrect | {_res}")