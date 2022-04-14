# 스택/큐
# https://programmers.co.kr/learn/courses/30/lessons/42583

def solution(bridge_length, weight, truck_weights):
    bridge_weights = 0
    bridge_trucks = [] #다리에 올라간 트럭
    elapsed_time = -1
    while True:
        #시간 경과
        elapsed_time += 1

        #다리를 건너는 트럭 진행
        for truck in bridge_trucks:
            truck[1] += 1
            if truck[1] > bridge_length-1:
                bridge_weights -= truck[0]
                bridge_trucks.pop()
        
        #현재 다리무게와 다음트럭의 무게의 합이 견딜 수 있는 무게보다 같거나 작은 경우
        if truck_weights and bridge_weights+truck_weights[0] <= weight and len(bridge_trucks) < bridge_length:
            bridge_weights += truck_weights[0]
            bridge_trucks.insert(0,[truck_weights[0], 0])
            del truck_weights[0]
        
        #모든 트럭이 통과했을 때 경과시간 반환
        if (not bridge_trucks) and bridge_weights == 0:
            return elapsed_time+1

bridge_length = [
    2,
    100,
    100
]

weight = [
    10,
    100,
    100
]

truck_weights = [
    [7,4,5,6],
    [10],
    [10,10,10,10,10,10,10,10,10,10]
]

result = [
    8,
    101,
    110
]

for q in [0,1,2]:
    qid = solution(bridge_length[q], weight[q], truck_weights[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')