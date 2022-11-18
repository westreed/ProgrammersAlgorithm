# 4789
# 연습문제

# 입력
'''
4
11111
09
110011
1

답
#1 0
#2 1
#3 2
#4 0
'''

testcase = int(input())
answer = ""

for tc in range(testcase):
    clap_Data = input()
    hire_Person = clap_Data.count("0")
    # clap_Data = list(map(int, list(input())))
    # hire_Person = 0 # 필요한 추가인원
    # clap_Person = clap_Data[0]
    # startIdx = 1

    # while True:
    #     Clap = clap_Person+hire_Person # 먼저 박수를 치는 사람 수 (startIdx시점까지 누적된 수)
    #     for i in range(startIdx,len(clap_Data)):
    #         Need = i
    #         Num = clap_Data[i]
    #         if Num: # 사람이 있을 때
    #             if Clap >= Need:
    #                 Clap += Num
    #             else:
    #                 clap_Person = Clap-hire_Person
    #                 hire_Person += Need-Clap
    #                 startIdx = i
    #                 break
    #     else: # 전부 통과하면, 모두가 일어서서 박수한 경우임
    #         break
    
    answer += f"#{tc+1} {hire_Person}\n"

print(answer)