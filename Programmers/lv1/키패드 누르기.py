# 2020 카카오 인턴십
# https://programmers.co.kr/learn/courses/30/lessons/67256

def distanceKey(hand, key): #거리 구하는 함수
    tempHand = [hand[0], hand[1]]
    return abs(tempHand[0]-key[0]) + abs(tempHand[1]-key[1])

def solution(numbers, hand):
    answer = ''
    leftHand_Pos = [0, 3] #10,*
    rightHand_Pos = [2, 3] #12,#
    for num in numbers:
        num_Pos = []
        if(num > 0): #1~9
            num_Pos = [(num-1)%3, int((num-1)/3)]
        else: #0
            num_Pos = [1,3]
        if(num % 3 == 1): #LeftHand
            leftHand_Pos = num_Pos
            answer += 'L'
            continue
        if(num > 0 and num % 3 == 0): #RightHand
            rightHand_Pos = num_Pos
            answer += 'R'
            continue
        leftDis = distanceKey(leftHand_Pos, num_Pos)
        rightDis = distanceKey(rightHand_Pos, num_Pos)
        print("위치 L",leftHand_Pos, " R",rightHand_Pos, "거리 L",leftDis, " R",rightDis)
        if(leftDis == rightDis):
            if(hand == "left"):
                leftHand_Pos = num_Pos
                answer += 'L'
            else:
                rightHand_Pos = num_Pos
                answer += 'R'
        elif(leftDis < rightDis):
            leftHand_Pos = num_Pos
            answer += 'L'
        else:
            rightHand_Pos = num_Pos
            answer += 'R'
    return answer

numbers = [
    [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],
    [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
]

hand = [
    "right",
    "left",
    "right"
]

result = [
    "LRLLLRLLRRL",
    "LRLLRRLLLRR",
    "LLRLLRLLRL"
]

for q in [0,1,2]:
    qid = solution(numbers[q], hand[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')