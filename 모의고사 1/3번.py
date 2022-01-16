# 3. 200점 이하의 점수 세기
# 한줄 수정하기

def solution(scores):
    count = 0
    for s in range(len(scores)):
        if scores[s] <= 200:
            count += 1
    return count

scores=[400, 100, 200, 150]
print(solution(scores))