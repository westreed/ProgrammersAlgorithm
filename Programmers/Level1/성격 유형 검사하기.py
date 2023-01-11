# 2022 KAKAO TECH INTERNSHIP
# https://school.programmers.co.kr/learn/courses/30/lessons/118666

def solution(survey, choices):
    character_Text = ['RT','CF','JM','AN']
    character_Type = {1:[0,0], 2:[0,0], 3:[0,0], 4:[0,0]}
    survey_Type = {"RT":(1,'F'), "TR":(1,'R'), "CF":(2,'F'), "FC":(2,'R'), "JM":(3,'F'), "MJ":(3,'R'), "AN":(4,'F'), "NA":(4,'R')}
    
    for id,sel in zip(survey, choices):
        survey_Idx, score_Type = survey_Type[id]
        
        if score_Type == 'R':
            sel = 8-sel # 순서 바꾸기
        
        if sel == 4: continue
        elif sel < 4: character_Type[survey_Idx][0] += 4-sel
        else: character_Type[survey_Idx][1] += sel-4

    result = ''
    for i in range(4):
        score = character_Type[i+1]
        
        if score[0] == score[1]:
            result += sorted(list(character_Text[i]))[0]
        elif score[0] > score[1]:
            result += character_Text[i][0]
        else:
            result += character_Text[i][1]
    return result

survey = [
    ["AN", "CF", "MJ", "RT", "NA"],
    ["TR", "RT", "TR"]
]

choices = [
    [5, 3, 2, 7, 5],
    [7, 1, 3]
]

result = [
    "TCMA",
    "RCJA"
]

for q in [0,1]:
    qid = solution(survey[q], choices[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')