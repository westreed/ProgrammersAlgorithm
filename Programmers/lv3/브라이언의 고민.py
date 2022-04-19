# 2017 카카오코드 예선
# https://programmers.co.kr/learn/courses/30/lessons/1830
# 원래는 c++, java 언어만 지원하는 문제지만 파이썬으로 풀었습니다.

def solution(sentence):
    from collections import defaultdict

    special_str = defaultdict(list)
    combination_str = []
    guess_str = ''

    # 특수문자 빼오기
    for i,s in enumerate(sentence):
        if s.islower() is True:
            if s not in special_str: special_str[s].append('')
            special_str[s].append(i)
        else: guess_str += s
    
    # 빼내온 특수문자를 통해, 규칙파악하기
    for s in special_str:
        _list = special_str[s]
        check = _list[0]
        _list = _list[1:]
        first, last = _list[0], _list[-1]

        # 규칙 1번
        if _list == list(range(first, last+1, 2)):
            _temp = list(map(lambda x : sentence[x-1], _list)) + [sentence[last+1]]
            _temp = "".join(_temp)

            # check에 값이 있으면 규칙 2번 안에 있는 규칙 1번이라는 의미
            if check != '':
                # 두 값이 일치하면, 오류는 없으므로 추가하지 않고 continue
                if check == _temp: continue
                # 일치하지 않으면, 규칙에 오류가 있음
                else:              return "invalid"
            combination_str.append(_temp)
        # 규칙 2번
        else:
            _temp = sentence[first+1:last]
            # 긁어온 글자 안에 있는 특수문자를 체크하기
            for key in special_str:
                if key in _temp:
                    _temp = _temp.replace(key, "")
                    special_str[key][0] = _temp

            combination_str.append(_temp)

    # 추측문자와 길이가 일치하는지 검사하기
    print(combination_str)
    _length = sum(map(lambda x : len(x), combination_str))

    if _length != len(guess_str): return "invalid"
    else:                         return " ".join(combination_str)

sentence = [
    "HaEaLaLaObWORLDb",
    "SpIpGpOpNpGJqOqA",
    "AxAxAxAoBoBoB",
    "aHbEbLbLbOacWdOdRdLdDc",
    "aHbEbLbLbacWdOdRdLdDc"
]

result = [
    "HELLO WORLD",
    "SIGONG JOA",
    "invalid",
    "HELLO WORLD",
    "invalid"
]

for q in [0,1,2,3,4]:
    qid = solution(sentence[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')