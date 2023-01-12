

def LabelLanguage(file):
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
    langList = {"py":"Python", "java":"Java"}
    return {"lang":langList[langType], "solve":solveType, "name":fileName}