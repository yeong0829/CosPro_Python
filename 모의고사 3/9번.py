#9
def solution(scores):
    result=[0, 0, 0, 0]
    for i in range(4):
        for k in range(4):
            if i != k:
                result[i]+=scores[i][k]*2
    return result

scores = [['X', 1, 0, 0], [0, 'X', 0, 1], [1, 1, 'X', 1], [1, 0, 0, 'X']]
print(solution9(scores))
