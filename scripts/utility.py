import data

def LabelLanguage(file:str) -> dict:
    '''
    Args:
        file (string) : 파일이름
    Returns:
        dict ('lang':string, 'solve':boolean, 'name':string)
    '''

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
    return {
        # data.LangList에 해당 확장자에 대한 언어이름이 없으면, 확장자명 그대로 사용하기
        "lang" : data.LangList[langType] if langType in data.LangList else langType,
        "solve" : solveType,
        "name" : fileName
    }