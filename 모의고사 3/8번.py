#8
def solution(password, key):
    answer = 0
    match_cnt = 0
    for k in key:
        for p in password:
            if k == p:
                match_cnt += 1
                break
    if match_cnt >= len(key):
        answer = 1
    return answer