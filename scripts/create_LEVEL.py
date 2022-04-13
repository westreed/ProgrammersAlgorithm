import os
from urllib import parse

def isPercentEncoding(s):
    s = ord(s)
    if 97 <= s <= 122:  return False
    if 65 <= s <= 90:   return False
    if 48 <= s <= 57:   return False
    if s == 45 or s == 95 or s == 46 or s == 126: return False
    return True

tableHeader = ["순번","문제 이름","문제 풀이","풀이 링크"]
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

    for index,file in enumerate(filelists):
        unresolved = True if file[-4:] == 'X.py' else False
        name = file.replace("X.py", "").replace(".py", "")
        filelinks = parse.quote(file)
        links = f'https://github.com/westreed/ProgrammersAlgorithm/blob/main/lv{level}/{filelinks}'

        line = f'|{index:02}|{name}|{unresolvedText[unresolved]}|[바로가기]({links})|'
        tables.append(line)
    
    tables = [ f"{line}\n" for line in tables ]

    # create MD
    with open(f'./LEVEL{level}.md', 'w', encoding = "UTF8") as f:
        f.writelines(header)
        f.write('\n\n')
        
        # table
        f.writelines(tables)