'''
2
학생들 신발 사이즈 조사
축구화 사이즈 작은 순서대로 "7", "7.5", "8", "8.5", "9", "9.5" 총 6종류
원하는 사이즈 리스트 shoes_size
가장 작은 사이즈부터 순서대로 리스트에 담아 return
'''

def solution(shoes_size) :
    answer = [0 for _ in range(len(shoes_size))]        # count를 세기 위한 변수 초기화
    for size in shoes_size:
        if size == '7':
            answer[0] += 1
        elif size == '7.5':
            answer[1] += 1
        elif size == '8':
            answer[2] += 1
        elif size == '8.5':
            answer[3] += 1
        elif size == '9':
            answer[4] += 1
        elif size == '9.5':
            answer[5] += 1
    return answer


print(solution(['7', '9', '7', '8.5', '8', '7']))