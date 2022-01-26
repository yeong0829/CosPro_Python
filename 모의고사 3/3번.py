#3
def solution(table):
    answer = 0
    max=0
    for i in range(1, len(table)):
        sum = 0
        for k in range(5):
            if table[0][k] == table[i][k]:
                sum += 1
        if max<sum:
            max=sum
            answer = i
    return answer