import os
import datetime
import pytz
import data
from utility import LabelLanguage
from urllib import parse

unresolvedText = ["**풀이안됨**", "풀이완료"]

for folder, sitename in data.folder_List:
    print(folder)
    folderPath = f"./{folder}"

    TableHeader = data.LevelTableHeader[:]
    if folder not in data.ProblemLinkBool or data.ProblemLinkBool[folder] is True:
        TableHeader.append("문제 링크")

    # 레벨 만큼 md파일 생성
    for filedata in os.scandir(folderPath):
        if filedata.is_file(): continue # 파일은 생략하기

        LevelName = filedata.name # 파일이름이랑 다름
        # if folder == 'BAEKJOON': LevelName = LevelName[1:] # 폴더앞 숫자제거
        header = [f'# {sitename}\n\n',f'## {LevelName}']
        tables = list()

        tables.append(f"| {' | '.join(TableHeader)} |")
        tables.append(f"| {':--: |' * len(TableHeader)}")

        path = f'{folderPath}/{filedata.name}'
        filelists = os.listdir(path)
        filelists.sort()
        print(filelists)

        # 폴더가 비어있으면, md파일을 생성하지 않고 다음으로 넘기기
        if not filelists: continue

        for index,file in enumerate(filelists):
            label = LabelLanguage(file)
            fileLink = parse.quote(file)
            problemType = ''
            siteLink = ''
            with open(f'{path}/{file}', 'r', encoding='UTF-8') as f:
                textline = f.readline()
                problemType = textline[2:].strip()
                textline = f.readline()
                if '문제 링크' in TableHeader:
                    siteLink = textline[2:].strip()

            links = f'https://github.com/{data.githubLink}/blob/main/{folder}/{filedata.name}/{fileLink}'

            line = f'|{index:03}|{problemType}|{label["lang"]}|{label["name"]}|{unresolvedText[label["solve"]]}|[바로가기]({links})|'
            if '문제 링크' in TableHeader:
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