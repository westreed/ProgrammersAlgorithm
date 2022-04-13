import os

header = list()
tables = list()
with open('./md/header.md', 'r', encoding = "UTF8") as f:
    header = f.readlines()
    f.close()

tableHeader = ["난이도","문제 링크","해결한 문제 수","전체 문제 수"]
tables.append(f"| {' | '.join(tableHeader)} |")
tables.append(f"| {':--: |' * len(tableHeader)}")
for idx in range(0, 4):
    level = f'레벨{idx+1}'

    path = f'./lv{idx+1}'
    filelists = os.listdir(path)
    
    problems   = len(filelists)
    unresolved = 0
    for file in filelists:
        if file[-4:] == 'X.py':
            unresolved += 1
    
    line = f'|{level}|[바로가기](https://github.com/westreed/ProgrammersAlgorithm/blob/main/LEVEL{idx+1}.md)|{problems-unresolved}|{problems}|'
    tables.append(line)

tables = [ f"{line}\n" for line in tables ]

# README.md

with open('./README.md', 'w', encoding = "UTF8") as f:
    f.writelines(header)
    f.write('\n')
    
    # table
    f.writelines(tables)