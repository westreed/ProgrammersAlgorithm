import os
import datetime
import pytz
import data
from urllib import parse

Working_Programmers = True
Working_SWAcademy   = True
Working_BAEKJOON    = True

def LabelLanguage(file):
    langList = {"py":"Python", "java":"Java"}
    langType = ""
    solveType = False
    fileName = ""

    idx = len(file)
    for s in file[::-1]:
        if s == '.':
            langType = file[idx:]
            break
        idx -= 1

    # if file[-3:] == ".py": langType = "py"
    # if file[-5:] == '.java': langType = "java"
    # print(file[idx-2:idx])
    solveType = False if file[idx-2:idx] == 'X.' else True
    if solveType: fileName = file.replace("."+langType, "").strip()
    else: fileName = file.replace("X."+langType, "").strip()
    return {"lang":langList[langType], "solve":solveType, "name":fileName}


# 프로그래머스 문제
'''-----------------------------------------------------------------------------------------------'''
if Working_Programmers:
    tableHeader = ["순번","문제 유형","언어","문제 이름","문제 풀이","풀이 링크", "문제 링크"]
    unresolvedText = ["**풀이안됨**", "풀이완료"]

    folderPath = f'./Programmers'

    # 레벨 만큼 md파일 생성
    for idx in range(data.programmers_Folder):
        header = list()
        tables = list()

        level = idx+1
        header = [f'# 프로그래머스\n',f'## LEVEL {level}']

        tables.append(f"| {' | '.join(tableHeader)} |")
        tables.append(f"| {':--: |' * len(tableHeader)}")

        path = f'{folderPath}/lv{level}'
        filelists = os.listdir(path)
        filelists.sort()
        print(filelists)

        for index,file in enumerate(filelists):
            label = LabelLanguage(file)
            # unresolved = True if file[-4:] == 'X.py' else False
            # name = file.replace("X.py", "").replace(".py", "")
            filelinks = parse.quote(file)
            problemType = ''
            programmerslink = ''
            with open(f'{path}/{file}', 'r', encoding='UTF-8') as f:
                textline = f.readline()
                problemType = textline[1:].strip()
                textline = f.readline()
                programmerslink = textline[1:-1].strip()

            links = f'https://github.com/westreed/ProgrammersAlgorithm/blob/main/Programmers/lv{level}/{filelinks}'

            line = f'|{index:02}|{problemType}|{label["lang"]}|{label["name"]}|{unresolvedText[label["solve"]]}|[바로가기]({links})|[바로가기]({programmerslink})|'
            tables.append(line)
        
        tables = [ f"{line}\n" for line in tables ]

        # create MD
        with open(f'{folderPath}/LEVEL{level}.md', 'w', encoding = "UTF-8") as f:
            f.writelines(header)
            f.write('\n\n')
            
            # table
            f.writelines(tables)
            f.write('\n\n')

            # update
            timeformat = datetime.datetime.now(pytz.timezone('Asia/Seoul'))
            f.write(f"**Update Date {timeformat.strftime('%Y/%m/%d %H:%M:%S %Z')}**\n\n")

# 삼성아카데미 문제
'''-----------------------------------------------------------------------------------------------'''
if Working_SWAcademy: 
    tableHeader = ["순번","문제 유형","언어","문제 이름","문제 풀이","풀이 링크"]
    unresolvedText = ["**풀이안됨**", "풀이완료"]

    folderPath = f'./SAMSUNG_SW_Expert_Academy'

    # 레벨 만큼 md파일 생성
    for idx in range(data.ssea_Folder):
        header = list()
        tables = list()

        level = idx+1
        header = [f'# SAMSUNG SW Expert Academy\n',f'## LEVEL {level}']

        tables.append(f"| {' | '.join(tableHeader)} |")
        tables.append(f"| {':--: |' * len(tableHeader)}")

        path = f'{folderPath}/lv{level}'
        filelists = os.listdir(path)
        filelists.sort()
        print(filelists)

        for index,file in enumerate(filelists):
            label = LabelLanguage(file)
            filelinks = parse.quote(file)
            problemType = ''
            with open(f'{path}/{file}', 'r', encoding='UTF-8') as f:
                textline = f.readline()
                problemType = int(textline[2:].strip())
                textline = f.readline()

            links = f'https://github.com/westreed/ProgrammersAlgorithm/blob/main/SAMSUNG_SW_Expert_Academy/lv{level}/{filelinks}'

            line = f'|{index:02}|{problemType:05}|{label["lang"]}|{label["name"]}|{unresolvedText[label["solve"]]}|[바로가기]({links})|'
            tables.append(line)
        
        tables = [ f"{line}\n" for line in tables ]

        # create MD
        with open(f'{folderPath}/LEVEL{level}.md', 'w', encoding = "UTF-8") as f:
            f.writelines(header)
            f.write('\n\n')
            
            # table
            f.writelines(tables)
            f.write('\n\n')

            # update
            timeformat = datetime.datetime.now(pytz.timezone('Asia/Seoul'))
            f.write(f"**Update Date {timeformat.strftime('%Y/%m/%d %H:%M:%S %Z')}**\n\n")

# 백준 문제
'''-----------------------------------------------------------------------------------------------'''
if Working_BAEKJOON:
    tableHeader = ["순번","문제 유형","언어","문제 이름","문제 풀이","풀이 링크","문제 링크"]
    unresolvedText = ["**풀이안됨**", "풀이완료"]

    folderPath = f'./BAEKJOON'

    # 레벨 만큼 md파일 생성
    for idx in range(data.baekjoon_Folder):
        header = list()
        tables = list()

        level = idx+1
        header = [f'# BAEKJOON\n',f'## {data.baekjoon_Level[idx][1:]}']

        tables.append(f"| {' | '.join(tableHeader)} |")
        tables.append(f"| {':--: |' * len(tableHeader)}")

        path = f'{folderPath}/{data.baekjoon_Level[idx]}'
        filelists = os.listdir(path)
        filelists.sort()
        print(filelists)

        for index,file in enumerate(filelists):
            label = LabelLanguage(file)
            # unresolved = True if file[-4:] == 'X.py' else False
            # name = file.replace("X.py", "").replace(".py", "")
            filelinks = parse.quote(file)
            problemType = ''
            with open(f'{path}/{file}', 'r', encoding='UTF-8') as f:
                textline = f.readline()
                problemType = textline[2:].strip()
                textline = f.readline()
                Baekjoonlink = textline[2:-1].strip()

            links = f'https://github.com/westreed/ProgrammersAlgorithm/blob/main/BAEKJOON/{data.baekjoon_Level[idx]}/{filelinks}'

            line = f'|{index:02}|{problemType}|{label["lang"]}|{label["name"]}|{unresolvedText[label["solve"]]}|[바로가기]({links})|[바로가기]({Baekjoonlink})|'
            tables.append(line)
        
        tables = [ f"{line}\n" for line in tables ]

        # create MD
        with open(f'{folderPath}/{data.baekjoon_Level[idx]}.md', 'w', encoding = "UTF-8") as f:
            f.writelines(header)
            f.write('\n\n')
            
            # table
            f.writelines(tables)
            f.write('\n\n')

            # update
            timeformat = datetime.datetime.now(pytz.timezone('Asia/Seoul'))
            f.write(f"**Update Date {timeformat.strftime('%Y/%m/%d %H:%M:%S %Z')}**\n\n")

'''-----------------------------------------------------------------------------------------------'''