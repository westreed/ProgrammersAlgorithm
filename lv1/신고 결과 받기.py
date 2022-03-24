# 2022 KAKAO BLIND RECRUITMENT
# https://programmers.co.kr/learn/courses/30/lessons/92334

def solution(id_list, report, k):
    # 메일로 처리결과를 받은 횟수
    mailReport = {id : 0 for id in id_list}
    # 신고자 : 신고대상
    reportList = {}
    # 신고대상 : 당한 횟수
    reportCount = {id : 0 for id in id_list}

    for id in report:
        # cp 신고자 tp 신고대상
        cp,tp = id.split(" ")
        id_Info = reportList.get(cp)
        if not id_Info:
            # 해당 신고자의 최초 기록
            reportList[cp] = [tp]
            reportCount[tp] += 1
        else:
            # 해당 신고자의 기록이 있는 경우
            if not tp in id_Info:
                id_Info.append(tp)
                reportList[cp] = id_Info
                reportCount[tp] += 1
    
    for id, values in reportList.items():
        count = 0
        for tp in values:
            if(reportCount[tp] >= k):
                count += 1
        mailReport[id] = count

    return list(mailReport.values())


id_list = [
    ["muzi", "frodo", "apeach", "neo"],
    ["con", "ryan"]
]

report = [
    ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],
    ["ryan con", "ryan con", "ryan con", "ryan con"]
]

k = [
    2,
    3
]

result = [
    [2,1,1,0],
    [0,0]
]

for q in [0,1]:
    qid = solution(id_list[q], report[q], k[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')