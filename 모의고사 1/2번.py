# 2. 최고 점수와 죄저 점수를 제외한 나머지 점수들의 합계 구하기

def func_a(s):
    s.sort() # s = sorted(s)
    return s[len(s)-1], s[0] # s[len(s)-1] == s[-1]

def func_b(s):
    ret = 0
    for i in s:
        ret += i
    return ret

def solution(scores):
    sum = func_b(scores)
    max, min = func_a(scores)
    return sum - max - min

scores = [100, 50, 30, 40, 60]
print(solution(scores))    #150