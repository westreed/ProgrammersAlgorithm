import os
from urllib import parse

tableHeader = ["순번","문제 이름","문제 풀이","풀이 링크", "문제 링크"]
unresolvedText = ["풀이완료", "풀이안됨"]

# 레벨 만큼 md파일 생성
for idx in range(0,4):
    header = list()
    tables = list()

    level = idx+1
    header = [f'# LEVEL {level}']

    tables.append(f"| {' | '.join(tableHeader)} |")
    tables.append(f"| {':--: |' * len(tableHeader)}")

    path = f'./lv{level}'
    filelists = os.listdir(path)
    print(filelists)

    for index,file in enumerate(filelists):
        unresolved = True if file[-4:] == 'X.py' else False
        name = file.replace("X.py", "").replace(".py", "")
        filelinks = parse.quote(file)
        programmerslink = ''
        with open(f'./lv{level}/{file}', 'r', encoding='UTF-8') as f:
            programmerslink = f.readline()
            programmerslink = f.readline()
            programmerslink = programmerslink[1:-1]

        links = f'https://github.com/westreed/ProgrammersAlgorithm/blob/main/lv{level}/{filelinks}'

        line = f'|{index:02}|{name}|{unresolvedText[unresolved]}|[바로가기]({links})|[바로가기]({programmerslink})|'
        tables.append(line)
    
    tables = [ f"{line}\n" for line in tables ]

    # create MD
    with open(f'./LEVEL{level}.md', 'w', encoding = "UTF-8") as f:
        f.writelines(header)
        f.write('\n\n')
        
        # table
        f.writelines(tables)