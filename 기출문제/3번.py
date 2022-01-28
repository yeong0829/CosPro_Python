#3
#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution3(people):
    answer = [0 for _ in range(4)]
    for p in people:
        if p < 95:
            answer[0] += 1
        elif p >= 95 and p < 100:
            answer[1] += 1
        elif p >= 100 and p < 105:
            answer[2] += 1
        elif p >= 105:
            answer[3] += 1
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
people = [97, 102, 93, 100, 107]
ret = solution3(people)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("3solution 함수의 반환 값은 ", ret, " 입니다.")