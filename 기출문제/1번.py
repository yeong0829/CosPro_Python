#1
def solution1(temperature, A, B):
    answer = 0
    for i in range(A+1, B):
        if temperature[i] > temperature[A] and temperature[i] > temperature[B]:
            answer += 1
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래에는 잘못된 부분이 없으니 위의 코드만 수정하세요.
temperature = [3, 2, 1, 5, 4, 3, 3, 2]
A = 1
B = 6
ret = solution1(temperature, A, B)

print("1solution 함수의 반환 값은", ret, "입니다.")
