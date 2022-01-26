#1
def solution(a, b):
    answer = 0
    diff= (b-a) if a<b else a-b
    answer = 10 / diff
    return answer*60

print(solution(10, 1))