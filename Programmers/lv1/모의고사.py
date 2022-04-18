# 완전탐색
# https://programmers.co.kr/learn/courses/30/lessons/42840

class human:
    def __init__(self, array):
        self.index = 0
        self.array = array
        self.arrlen = len(array)
        self.answer = 0
    
    def returnNumber(self, correct):
        value = self.array[self.index]

        if (self.index == self.arrlen-1):
            self.index = 0
        else:
            self.index = self.index + 1

        if (correct == value):
            self.answer = self.answer + 1


def solution(answers):
    human1 = human([1,2,3,4,5])
    human2 = human([2,1,2,3,2,4,2,5])
    human3 = human([3,3,1,1,2,2,4,4,5,5])

    for ans in answers:
        human1.returnNumber(ans)
        human2.returnNumber(ans)
        human3.returnNumber(ans)

    answerList = [human1.answer, human2.answer, human3.answer]
    maxScore = 0
    for i in range(0,3):
        if(maxScore < answerList[i]):
            maxScore = answerList[i]

    checkAnswer = []
    for i in range(0,3):
        if(maxScore == answerList[i]):
            checkAnswer.append(i+1)
    return checkAnswer

answer = [
    [1,2,3,4,5],
    [1,3,2,4,2]
]

result = [
    [1],
    [1,2,3]
]

for q in [0,1]:
    qid = solution(answer[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')