import os
import datetime
import pytz
import data
from utility import LabelLanguage

header = list()
tables = list()
with open('./md/header.md', 'r', encoding = "UTF-8") as f:
    header = f.readlines()
    f.close()

tableHeader = ["난이도","문제 링크","해결한 문제","전체 문제", "해결비율(%)"]

for folder, sitename in data.folder_List:
    tables.append(f"\n\n## {sitename}\n\n")
    tables.append(f"| {' | '.join(tableHeader)} |")
    tables.append(f"| {':--: |' * len(tableHeader)}")

    print(folder)
    folderPath = f"./{folder}"

    # 레벨별 데이터 가져오기
    level_line = []
    for filedata in os.scandir(folderPath):
        if filedata.is_file(): continue # 파일은 생략하기

        path = f'{folderPath}/{filedata.name}'
        filelists = os.listdir(path)

        problems = len(filelists)
        unsolved = 0
        for file in filelists:
            label = LabelLanguage(file)
            if label["solve"] is False:
                unsolved += 1
        
        links = f'https://github.com/{data.githubLink}/blob/main/{folder}/{filedata.name}.md'
        line = f'|{filedata.name}|[바로가기]({links})|{problems-unsolved:02}|{problems:02}|'
        if problems == 0: line += f'100%|'
        else: line += f'{int(round(((problems-unsolved)/problems)*100, 0))}%|'
        level_line.append(line)
    level_line.sort()
    tables += level_line

# Create README.md
tables = [ f"{line}\n" for line in tables ]
with open('./README.md', 'w', encoding = "UTF-8") as f:
    f.writelines(header)
    f.write('\n\n')
    
    # table
    f.writelines(tables)
    f.write('\n\n')

    # update
    timeformat = datetime.datetime.now(pytz.timezone('Asia/Seoul'))
    f.write(f"**Update Date {timeformat.strftime('%Y/%m/%d %H:%M:%S %Z')}**")