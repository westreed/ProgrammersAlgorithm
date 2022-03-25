# 2018 KAKAO BLIND RECRUITMENT
# https://programmers.co.kr/learn/courses/30/lessons/17681

def change(n, a, x):
    s = ''
    num = 0
    while (a>0):
        a, r = divmod(a,x)
        if (r>9):
            r=chr(ord('a')+r-10)
        s = f'{r}{s}'
        num += 1
    while (num<n):
        s = f'0{s}'
        num += 1
    return s

def solution(n, arr1, arr2):
    arrA = []
    for i in range(n):
        arr1[i] = change(n, arr1[i], 2)
        arr2[i] = change(n, arr2[i], 2)
    for i in range(n):
        temp1 = ",".join(arr1[i])
        temp2 = ",".join(arr2[i])
        temp1 = temp1.split(",")
        temp2 = temp2.split(",")
        b=''
        for j in range(n):
            a = int(temp1[j]) | int(temp2[j])
            if (a == 1):
                b += str('#')
            else:
                b += str(' ')
        arrA.append(b)
    print(arrA)
    return arrA

n = [
    5,
    6
]

arr1 = [
    [9, 20, 28, 18, 11],
    [46, 33, 33 ,22, 31, 50]
]

arr2 = [
    [30, 1, 21, 17, 28],
    [27 ,56, 19, 14, 14, 10]
]

result = [
    ["#####", "# # #", "### #", "#  ##", "#####"],
    ['######', '###  #', '##  ##', ' #### ', ' #####', '### # ']
]

for q in [0,1]:
    qid = solution(n[q], arr1[q], arr2[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')