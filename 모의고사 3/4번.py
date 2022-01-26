#4
def solution(walls):
    answer = 0
    painted_walls=0
    hour=1
    while painted_walls <walls:
        painted_walls=(hour)+(hour//2)+(hour//4)
        hour+=1
    answer = hour-1
    return answer


print(solution(100))