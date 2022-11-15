# 5948
# 연습문제

# 입력
'''
2
1 2 3 4 5 6 7
5 24 99 76 1 77 6

1 2 4 8 16 32 64
'''

testcase = int(input())
answer = ""

for tc in range(testcase):
    result = []
    number = sorted(list(map(int, input().split())), reverse=True)

    for i in range(7):
        for j in range(i+1, 7):
            for k in range(j+1, 7):
                res = number[i]+number[j]+number[k]
                result.append(res)
    result = sorted(list(set(result)), reverse=True)
    print(result)
    answer += f"#{tc+1} {result[4]}\n"

print(answer)