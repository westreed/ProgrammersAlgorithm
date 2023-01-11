import os
import datetime
import pytz
import data
from urllib import parse

Working_Programmers = False
Working_SWAcademy   = False
Working_BAEKJOON    = False

def LabelLanguage(file):
    # langType에 파일 확장자명이 저장됨
    idx = len(file)
    for s in file[::-1]:
        if s == '.':
            langType = file[idx:]
            break
        idx -= 1

    # "문제이름 X.확장자" 일때, 해결하지 못한 문제임 
    solveType = False if file[idx-2:idx] == 'X.' else True

    # 문제이름 가져오기
    if solveType: fileName = file.replace(f".{langType}", "").strip()
    else: fileName = file.replace(f"X.{langType}", "").strip()

    # Dict 형태로 데이터 반환하기
    langList = {"py":"Python", "java":"Java"}
    return {"lang":langList[langType], "solve":solveType, "name":fileName}

TableHeader = {
'Programmers' :                 ["순번","문제 유형","언어","문제 이름","문제 풀이","풀이 링크", "문제 링크"],
'SAMSUNG_SW_Expert_Academy' :   ["순번","문제 유형","언어","문제 이름","문제 풀이","풀이 링크"],
'BAEKJOON' :                    ["순번","문제 유형","언어","문제 이름","문제 풀이","풀이 링크", "문제 링크"]
}

unresolvedText = ["**풀이안됨**", "풀이완료"]

for folder, sitename in data.folder_List:
    print(folder)
    folderPath = f"./{folder}"

    # 레벨 만큼 md파일 생성
    for filedata in os.scandir(folderPath):
        if filedata.is_file(): continue # 파일은 생략하기

        LevelName = filedata.name # 파일이름이랑 다름
        if folder == 'BAEKJOON': LevelName = LevelName[1:] # 폴더앞 숫자제거
        header = [f'# {sitename}\n\n',f'## {LevelName}']
        tables = list()

        tables.append(f"| {' | '.join(TableHeader[folder])} |")
        tables.append(f"| {':--: |' * len(TableHeader[folder])}")

        path = f'{folderPath}/{filedata.name}'
        filelists = os.listdir(path)
        filelists.sort()
        print(filelists)

        for index,file in enumerate(filelists):
            label = LabelLanguage(file)
            fileLink = parse.quote(file)
            problemType = ''
            siteLink = ''
            with open(f'{path}/{file}', 'r', encoding='UTF-8') as f:
                textline = f.readline()
                problemType = textline[1:].strip()
                textline = f.readline()
                if '문제 링크' in TableHeader[folder]:
                    siteLink = textline[1:-1].strip()

            links = f'https://github.com/westreed/ProgrammersAlgorithm/blob/main/{folder}/{filedata.name}/{fileLink}'

            line = f'|{index:03}|{problemType}|{label["lang"]}|{label["name"]}|{unresolvedText[label["solve"]]}|[바로가기]({links})|'
            if '문제 링크' in TableHeader[folder]:
                line += f'[바로가기]({siteLink})|'
            tables.append(line)
        
        tables = [ f"{line}\n" for line in tables ]

        # create MD
        with open(f'{folderPath}/{filedata.name}.md', 'w', encoding = "UTF-8") as f:
            f.writelines(header)
            f.write('\n\n')
            
            # Table
            f.writelines(tables)
            f.write('\n\n')

            # Update
            timeformat = datetime.datetime.now(pytz.timezone('Asia/Seoul'))
            f.write(f"**Update Date {timeformat.strftime('%Y/%m/%d %H:%M:%S %Z')}**")