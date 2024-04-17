# 자료 구조, 문자열, 스택
# https://www.acmicpc.net/problem/9935

"""
mirkovC4nizCC44
C4
> mirkovniz

12ab112ab2ab
12ab
> FRULA
"""

if __name__ == "__main__":
    S = input().strip()
    B = input().strip()

    LENGTH_S = len(S)
    LENGTH_B = len(B)
    strings = list(S)

    matchs = [(0,0)]

    for i in range(LENGTH_S):
        idx,pos = matchs[-1]
        if S[i] != B[idx]:
            if S[i] == B[0]:
                matchs.append((1, i))
            else:
                matchs.append((0, i))
        else:
            matchs.append((idx+1, i))
            if idx+1 == LENGTH_B:
                for _ in range(LENGTH_B):
                    _,pos = matchs.pop()
                    strings[pos] = ""
    
    ans = "".join(strings)
    print("FRULA" if ans == "" else ans)
