# 5. 369게임 - 1~numver까지 박수를 몇번치는지 알아내는 함수 작성
# 전달되는 number는 2자리 이상의 정수

def solution(number):
    count = 0
    for i in range(1, number+1):
        current = i
        while current != 0:  # not current == 0
            unit = current % 10
            if unit == 3 or unit == 6 or unit == 9:
                count += 1
            current //= 10
    return count

print(solution(12)) # 3
print(solution(13)) # 4