# 10965
# 연습문제

# 입력
'''
8
1
2
3
4
5
6
60
1000
'''
case = int(input())
answer = []
maxv = 10**7

primes=[2]
for i in range(3,int(maxv**0.5),2):
    for prime in primes:
        if not i % prime:break
    else:
        primes.append(i)

for c in range(case):
    number = int(input())
    value = 1

    # 제곱수가 아닌 경우
    if number**0.5 != int(number**0.5):
        for prime in primes:
            if prime > number: break
            cnt = 0
            while number % prime == 0:
                number //= prime
                cnt += 1
            if cnt > 0 and cnt % 2 != 0:
                value *= prime
        if number > 1:
            value *= number
                
    answer.append(f'#{c+1} {value}')

for ans in answer:
    print(ans)


# from collections import defaultdict

# def factor(x):

#     d = 2
#     lists = defaultdict(int)

#     while d <= x:
#         r = x % d
#         if r == 0:
#             lists[d] += 1
#             x = x // d
#         else:
#             d += r
    
#     return lists

# case = int(input())
# answer = []

# for c in range(case):
#     number = int(input())
#     value = 1

#     if number**0.5!=int(number**0.5):
#         lists = factor(number)
#         print(lists)
        
#         for k, v in lists.items():
#             if v % 2 != 0: value *= k
    
#     answer.append(f'#{c+1} {value}')

# for ans in answer:
#     print(ans)