# 수학
# https://www.acmicpc.net/problem/2292

# 1: 1
# 2: 2~7 (+6)
# 3: 8~19 (+12)
# 4: 20~37 (+18)
# 5: 38~61 (+24)

N = int(input())
Answer = 0
Cnt,Pre = 1,1

while True:
    if N == 1:
        Answer = 1
        break

    Nxt = Pre+(Cnt*6)
    print(Pre+1, Nxt)
    if Pre+1 <= N <= Nxt:
        Answer = Cnt+1
        break

    Cnt += 1
    Pre = Nxt

print(Answer)