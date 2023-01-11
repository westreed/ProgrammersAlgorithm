# 2022 KAKAO BLIND RECRUITMENT
# https://programmers.co.kr/learn/courses/30/lessons/92341

def solution(fees, records):
    from math import ceil
    from collections import defaultdict
    std_time, std_pay, per_time, per_pay = fees

    record_number = defaultdict(list)

    for record in records:
        re_time, re_number, re_state = record.split()
        print(re_time, '\t',re_number, '\t',re_state)

        H,M = map(int, re_time.split(':'))
        re_time = H*60 + M

        # dict에 없는 번호인 경우 (최초 등록)
        if re_number not in record_number:
            record_number[re_number] = [0, re_time]
        else:
            if re_state == 'IN':
                record_number[re_number].append(re_time)
            elif re_state == 'OUT':
                pre_time = record_number[re_number].pop()
                record_number[re_number][0] += re_time - pre_time
    
    # 요금 정산하기
    for record in record_number:
        # 아직 출차하지 않은 차량인 경우
        if len(record_number[record]) >= 2:
            pre_time = record_number[record].pop()
            record_number[record][0] += 1439 - pre_time # 1439는 23:59
        
        # 요금 정산하기
        pay_time = record_number[record][0]
        pay_money = std_pay

        # 기본시간을 초과한 경우
        if pay_time > std_time:
            pay_money += ceil((pay_time - std_time)/per_time)*per_pay
        
        record_number[record] = pay_money

    answer = [i[1] for i in sorted(record_number.items(), key=lambda x:x[0])]
    return answer

fees = [
    [180, 5000, 10, 600],
    [120, 0, 60, 591],
    [1, 461, 1, 10]
]

records = [
    ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"],
    ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"],
    ["00:00 1234 IN"]
]

result = [
    [14600, 34400, 5000],
    [0, 591],
    [14841]
]

for q in [0,1,2]:
    qid = solution(fees[q], records[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')