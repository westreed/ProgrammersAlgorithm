import os
import datetime
import pytz

header = list()
tables = list()
with open('./md/header.md', 'r', encoding = "UTF-8") as f:
    header = f.readlines()
    f.close()

tableHeader = ["난이도","문제 링크","해결한 문제 수","전체 문제 수"]
tables.append(f"## 프로그래머스")

tables.append(f"| {' | '.join(tableHeader)} |")
tables.append(f"| {':--: |' * len(tableHeader)}")

for idx in range(4):
    path = f'./Programmers/lv{idx+1}'
    filelists = os.listdir(path)
    
    problems   = len(filelists)
    unresolved = 0
    for file in filelists:
        if file[-4:] == 'X.py':
            unresolved += 1
    
    links = f'https://github.com/westreed/ProgrammersAlgorithm/blob/main/Programmers/LEVEL{idx+1}.md'
    
    line = f'|레벨{idx+1}|[바로가기]({links})|{problems-unresolved:02}|{problems:02}|'
    tables.append(line)

tables.append(f"## 삼성 SW 아카데미")

tables.append(f"| {' | '.join(tableHeader)} |")
tables.append(f"| {':--: |' * len(tableHeader)}")

for idx in range(3):
    path = f'./SAMSUNG_SW_Expert_Academy/lv{idx+1}'
    filelists = os.listdir(path)
    
    problems   = len(filelists)
    unresolved = 0
    for file in filelists:
        if file[-4:] == 'X.py':
            unresolved += 1
    
    links = f'https://github.com/westreed/ProgrammersAlgorithm/blob/main/SAMSUNG_SW_Expert_Academy/LEVEL{idx+1}.md'
    
    line = f'|레벨{idx+1}|[바로가기]({links})|{problems-unresolved:02}|{problems:02}|'
    tables.append(line)

tables = [ f"{line}\n" for line in tables ]

# README.md

with open('./README.md', 'w', encoding = "UTF-8") as f:
    f.writelines(header)
    f.write('\n\n')
    
    # table
    f.writelines(tables)
    f.write('\n\n')

    # update
    timeformat = datetime.datetime.now(pytz.timezone('Asia/Seoul'))
    f.write(f"**Update Date {timeformat.strftime('%Y/%m/%d %H:%M:%S %Z')}**\n\n")