'''
5
카페 회원들에게 일련번호 부여
가장 많은 글을 작성한 회원의 글 개수는 가장 적게 작성한 회원의 글 개수가 몇 배인
가장 많은 글을 작성한 회원의 글 개수는 가장 적게 작성한 회원의 글 개수가 몇 배인지
1. 리스트에 들어있는 각 회원별 글 개수를 셉니다.
2. 가장 많이 작성한 회원의 글 개수를 구합니다.
3. 가장 적게 작성한 회원의 글 개수를 구합니다.
4. 가장 많이 작성개수가 가장 적게 작성한 개수보다 몇 배인지 구함
'''

# 리스트에 들어있는 각 회원별의 글 개수 계산
def func_a(arr):
    counter = [0 for _ in range(1001)]
    for i in arr:
        counter[i] += i
    return counter

# 가장 많이 작성한 회원의 글 개수 계산
def func_b(arr):
    ret = 0
    for i in arr:
        if ret < i:
            ret = i
    return ret

# 가장 적게 작성한 회원의 글 개수  계산
def func_c(arr):
    ret = func_b(arr) # 최대값을 최소값 구하는 변수에 초기화
    for i in arr:
        if ret > i and i != 0: # arr 배열의 0으로 초기화된 값은 최솟값으로 들어가면 안됨
            ret = i
    return ret

def solution(arr):
    counter = func_a(arr)
    max_cnt = func_b(counter)
    min_cnt = func_c(counter)
    return max_cnt // min_cnt

print(solution([500, 500, 1, 1000, 500, 500, 1000, 1, 1]))