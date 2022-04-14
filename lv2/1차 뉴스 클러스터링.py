# 2018 KAKAO BLIND RECRUITMENT
# https://programmers.co.kr/learn/courses/30/lessons/17677

def settingSTR(string):
    array = []
    temp = []
    for i in range(len(string)-1):
        array.append(string[i:i+2])
    for i in array:
        check = True
        for j in range(2):
            s = ord(i[j])
            if not(s > 10 and (97 <= s and 122 >= s)):
                check = False
                break
        if check: temp.append(i)
    return temp

def unionArray(inarr, arr1, arr2): #합집합
    for i in inarr:
        arr1.remove(i)
        arr2.remove(i)
    return inarr+arr1+arr2
    
def intersectArray(arr1, arr2): #교집합
    temparr2 = arr2[:]
    temp = []
    for i in arr1:
        if i in temparr2:
            temparr2.remove(i)
            temp.append(i)
    return temp

def solution(str1, str2):
    import math
    answer = 0
    tempstr1 = str1.lower()
    tempstr2 = str2.lower()
    setstr1 = settingSTR(tempstr1)
    setstr2 = settingSTR(tempstr2)
    a = intersectArray(setstr1, setstr2)
    b = unionArray(a, setstr1, setstr2)
    i,u = len(a), len(b)
    if u: return math.floor((i*65536)/u)
    elif i == u: return 65536
    else: return 0

str1 = [
    "FRANCE",
    "handshake",
    "aa1+aa2",
    "E=M*C^2"
]

str2 = [
    "french",
    "shake hands",
    "AAAA12",
    "e=m*c^2"
]

result = [
    16384,
    65536,
    43690,
    65536
]

for q in [0,1,2]:
    qid = solution(str1[q], str2[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')