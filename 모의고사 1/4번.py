# 4. 국가신용등급에따라 관세 계산
'''
등급        관세율
"S"         5%
"G"         10%
"V"         15%
예: "S"인 국가에서 수입하는 물품의 가격이 1000원인 경우 관세율 5% 적용한 가격은 1050원
'''

def solution(price, grade):
    answer = 0
    if grade == "S":
        answer = price * 1.05
    if grade == "G":
        answer = price * 1.10
    if grade == "V":
        answer = price * 1.15
    return answer

print(solution(1000, "S"))   #1050


def solution2(price, grade):
    global rate
    if grade == 'S':
        rate = 5
    elif grade == 'G':
        rate = 10
    elif grade == 'V':
        rate = 15
    answer = price * (1 + rate/100) # 1000 x (1 + rate / 100)
    return int(answer)