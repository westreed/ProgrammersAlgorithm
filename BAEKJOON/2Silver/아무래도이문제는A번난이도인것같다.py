# 수학, 애드 혹, 해 구성하기
# https://www.acmicpc.net/problem/1402

"""
1
6 5
"""

# 6 5인 케이스에서 6*-1*-1*1 = 6, 6-1-1+1 = 5 와 같이
# -1과 1을 필요한 만큼 사용하면 어떤 케이스의 숫자든 구현이 가능해서
# 정답은 항상 yes가 됩니다.

if __name__ == "__main__":
    input = __import__("sys").stdin.readline
    T = int(input())

    for _ in range(T):
        A, B = map(int, input().split())
        print("yes")