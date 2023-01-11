# 4751
# 연습문제

# 입력
'''
2
D
APPLE

답
..#..
.#.#.
#.D.#
.#.#.
..#..
..#...#...#...#...#..
.#.#.#.#.#.#.#.#.#.#.
#.A.#.P.#.P.#.L.#.E.#
.#.#.#.#.#.#.#.#.#.#.
..#...#...#...#...#..
'''

testcase = int(input())
answer = ""

decorate = [
    list("..#.."),
    list(".#.#."),
    list("#...#"),
    list(".#.#."),
    list("..#..")
]

for tc in range(testcase):
    ans = [[] for _ in range(5)]
    ipt = input().strip()
    rng = len(ipt)

    for i in range(rng):
        for j in range(5):
            temp = 0
            if i < rng-1:
                temp = decorate[j][:4]
            else:
                temp = decorate[j]

            if j == 2: temp[2] = ipt[i]
            ans[j] += temp
    
    res = ""
    for a in ans:
        res += "".join(a) + "\n"
    
    answer += res

print(answer)