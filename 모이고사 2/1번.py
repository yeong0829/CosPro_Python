'''
1
사회인 축구대회 총 7팀
각 팀이 다른 모든 팀과 한번씩 경기를 진행
각 팀은 하루에 한 경기만 참여
쉬는 날도 있음
대회에 사용할 축구장을 임대해야 하기 때문에 임대료 계산
대회 참가하는팀수 n
축구장의 하루 임대료 price
임대료를 계산하여 return
'''

def solution(n, price):                     # N : 대회에 참가하는 팀 수 / PRICE : 축구장의 하루 대여료
    games = n * (n - 1) // 2                # 리그 전의 경기의 수
    per_day = n // 2                        # 하루에 진행할 수 있는 경기의 수
    answer = (games // per_day) * price
    return answer                           # RETURN값 임대료

print(solution(2, 1000))