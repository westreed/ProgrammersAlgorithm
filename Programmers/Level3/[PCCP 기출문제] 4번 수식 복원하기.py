# PCCP 기출문제
# https://school.programmers.co.kr/learn/courses/30/lessons/340210

def transform_10_to_base(num:str, base):
    num_int = int(num)
    if num_int == 0:
        return "0"
    res = []
    while num_int:
        q,r = divmod(num_int, base)
        num_int = q
        res.append(str(r))
        if num_int < base:
            res.append(str(num_int))
            break
    return str(int("".join(res[::-1])))

def solution(expressions):
    split_expressions = [e.split() for e in expressions]
    possible_base = list(range(2, 10))
    
    # 1. 불가능한 진법은 제거하기
    for exp in split_expressions:
        if exp[-1] == "X":
            continue

        remove_base = []
        num1, op, num2, _, res = exp
        for base in possible_base:
            try:
                _num1 = int(num1, base)
                _num2 = int(num2, base)
            except:
                remove_base.append(base)
                continue

            if op == "+":
                base_res = transform_10_to_base(str(int(_num1) + int(_num2)), base)
            else:
                base_res = transform_10_to_base(str(int(_num1) - int(_num2)), base)

            if base_res != res:
                remove_base.append(base)
        
        for rb in remove_base:
            possible_base.remove(rb)
    
    predict = []
    remove_base = set() # 불가능한 진법이 있는 경우, 예측된 다른 결과에서도 제거하기 위함
    # 2. 가능한 진법으로 변환하기
    for exp in split_expressions:
        if exp[-1] != "X":
            continue
        
        pred_result = [set()]
        num1, op, num2, _, res = exp
        for base in possible_base:
            try:
                _num1 = int(num1, base)
                _num2 = int(num2, base)
            except:
                remove_base.add(base)
                continue

            if op == "+":
                base_res = transform_10_to_base(str(int(_num1) + int(_num2)), base)
            else:
                base_res = transform_10_to_base(str(int(_num1) - int(_num2)), base)

            pred_result[0].add(base)
            pred_result.append((base_res, base))
        
        predict.append(pred_result)
    
    # 3. 불가능한 진법에 대한 결과 삭제하기
    for pred_result in predict:
        for base in remove_base:
            if base in pred_result[0]:
                for p in pred_result[1:]:
                    if p[1] == base:
                        pred_result.remove(p)
                        pred_result[0].remove(base)
    
    # 4. 결과 출력하기
    answer = []
    idx = -1
    for exp in split_expressions:
        if exp[-1] != "X":
            continue

        idx += 1
        num1, op, num2, _, _ = exp
        pred = predict[idx]
        pred_list = pred[1:]
        
        all_same = set()
        for p in pred_list:
            all_same.add(p[0])
        
        if len(all_same) == 1:
            answer.append(f"{num1} {op} {num2} = {pred_list[0][0]}")
            continue
        else:
            answer.append(f"{num1} {op} {num2} = ?")

    return answer

expressions = [
    ["14 + 3 = 17", "13 - 6 = X", "51 - 5 = 44"],
    ["1 + 1 = 2", "1 + 3 = 4", "1 + 5 = X", "1 + 2 = X"],
    ["10 - 2 = X", "30 + 31 = 101", "3 + 3 = X", "33 + 33 = X"],
    ["2 - 1 = 1", "2 + 2 = X", "7 + 4 = X", "5 - 5 = X"],
    ["2 - 1 = 1", "2 + 2 = X", "7 + 4 = X", "8 + 4 = X"]
]

result = [
    ["13 - 6 = 5"],
    ["1 + 5 = ?", "1 + 2 = 3"],
    ["10 - 2 = 4", "3 + 3 = 10", "33 + 33 = 110"],
    ["2 + 2 = 4", "7 + 4 = ?", "5 - 5 = 0"],
    ["2 + 2 = 4", "7 + 4 = 12", "8 + 4 = 13"]
]

for q in [0,1,2,3,4]:
    qid = solution(expressions[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')
