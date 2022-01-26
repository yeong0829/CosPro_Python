#5
def solution(mho_cards, mhe_cards):
    result = -1
    mho = 0
    mhe = 0
    for i in range(len(mho_cards)):
        if mho_cards[i] > mhe_cards[i]:
            mho += 1
        else:
            mhe += 1
    if mho > mhe:
        result = 1
    elif mho < mhe:
        result = 0
    return result

print(solution([3, 5, 1, 7, 2], [8, 6, 9, 4, 0]))