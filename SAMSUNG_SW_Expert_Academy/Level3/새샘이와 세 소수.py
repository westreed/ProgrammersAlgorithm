# 5986
# 연습문제

'''
3
7
11
25
'''
primes = [2]
for i in range(3,1000,2):
    for prime in primes:
        if not i % prime: break
    else:
        primes.append(i)

testcase = int(input())
answer = ""
for tc in range(testcase):
    number = int(input())
    length = len(primes)
    total = 0

    for i in range(length):
        if primes[i] > number: break
        for j in range(i, length):
            if primes[j] > number: break
            for k in range(j, length):
                if primes[k] > number: break
                if primes[i]+primes[j]+primes[k] == number:
                    total += 1
    
    answer += f'#{tc+1} {total}\n'

print(answer)