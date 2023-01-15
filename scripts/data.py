
githubLink = 'westreed/ProgrammersAlgorithm'

# 사이트별 폴더 ('폴더이름', '사이트이름') 으로 작성하기
# 폴더이름은 파일 접근을 위해서, 사이트이름은 md파일로 생성하면서 사이트이름을 표기할 때 사용됩니다.
folder_List = [
    ('BAEKJOON', 'BAEKJOON'),
    ('Programmers', '프로그래머스'),
    ('SAMSUNG_SW_Expert_Academy', 'SAMSUNG SW Expert Academy')
]

# Table Header Data
ReadmeTableHeader   = ["문제 난이도","문제 링크","해결한 문제","전체 문제", "해결비율(%)"]
LevelTableHeader    = ["순번","문제 유형","언어","문제 이름","문제 풀이","풀이 링크"]

# 문제 링크가 없을 땐, 아래에 데이터를 추가해주세요.
ProblemLinkBool = {
    'SAMSUNG_SW_Expert_Academy': False
}

# 사용하는 언어에 따라, 아래의 dict을 추가해주세요.
LangList = { # 확장자 : 언어이름
    "py"    : "Python",
    "java"  : "Java",
}