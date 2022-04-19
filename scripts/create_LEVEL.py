import os
import datetime
import pytz
from urllib import parse


# 프로그래머스 문제
'''-----------------------------------------------------------------------------------------------'''
tableHeader = ["순번","문제 유형","문제 이름","문제 풀이","풀이 링크", "문제 링크"]
unresolvedText = ["풀이완료", "**풀이안됨**"]

folderPath = f'./Programmers'

# 레벨 만큼 md파일 생성
for idx in range(4):
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
        unresolved = True if file[-4:] == 'X.py' else False
        name = file.replace("X.py", "").replace(".py", "")
        filelinks = parse.quote(file)
        problemType = ''
        programmerslink = ''
        with open(f'{path}/{file}', 'r', encoding='UTF-8') as f:
            textline = f.readline()
            problemType = textline[1:].strip()
            textline = f.readline()
            programmerslink = textline[1:-1].strip()

        links = f'https://github.com/westreed/ProgrammersAlgorithm/blob/main/Programmers/lv{level}/{filelinks}'

        line = f'|{index:02}|{problemType}|{name}|{unresolvedText[unresolved]}|[바로가기]({links})|[바로가기]({programmerslink})|'
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
tableHeader = ["순번","문제 유형","문제 이름","문제 풀이","풀이 링크"]
unresolvedText = ["풀이완료", "**풀이안됨**"]

folderPath = f'./SAMSUNG_SW_Expert_Academy'

# 레벨 만큼 md파일 생성
for idx in range(3):
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
        unresolved = True if file[-4:] == 'X.py' else False
        name = file.replace("X.py", "").replace(".py", "")
        filelinks = parse.quote(file)
        problemType = ''
        with open(f'{path}/{file}', 'r', encoding='UTF-8') as f:
            textline = f.readline()
            problemType = textline[1:].strip()
            textline = f.readline()

        links = f'https://github.com/westreed/ProgrammersAlgorithm/blob/main/SAMSUNG_SW_Expert_Academy/lv{level}/{filelinks}'

        line = f'|{index:02}|{problemType}|{name}|{unresolvedText[unresolved]}|[바로가기]({links})|'
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