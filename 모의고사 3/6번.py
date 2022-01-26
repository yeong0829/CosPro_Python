#6
def solution(string):
    answer = 0
    number=0
    s = string+' '
    for c in s:
        if '0'<=c and c<='9' :
            number =  number*10+int(c)
        else:
            answer += number
            number=0
    return answer

print(solution("Korean world cup 2018. olympic stadium 10, 11 pm 1."))
