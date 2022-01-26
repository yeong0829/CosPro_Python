#7
def solution(a, b):
    result=[0, 0]
    for i in range(3):
        temp = b
        for k in range(3):
            if a %10 == temp %10:
                if i == k:
                    result[0]+=1
                else:
                    result[1]+=1
            temp //= 10
        a //= 10
    return

print(solution(123, 345)) # Strike 0 / Ball 1