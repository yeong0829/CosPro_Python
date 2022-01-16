# 10. 정수가 들어있는 리스트의 평균과 평균 미만인 값이 몇개인지 구하기
# 예: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]이라면 평균은 5, 평균 미만인 값은 4개
# 한줄만 변경

def solution(data):
    total = 0
    for i in data:
        total += i
    cnt = 0
    average = total // len(data)
    for i in data:
        if i < average:
            cnt += 1
    return cnt

data = [i for i in range(1, 11)]
print(solution(data))

print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  #4