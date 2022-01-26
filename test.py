#1. 숫자가 들어있는 리스트의 합계
scores = [10, 3, 20, 50]

def sum_list(list):
    result = sum(list)
    return result

print(sum_list(scores))   #83

# # 2. 최댓값
def max_list(list):
   # max_num = list[0]
   # for i in range(1, len(list)):
   #     if max_num < list[i]:
   #         max_num = list[i]
   #  return max_num

   # max_num = list[0]
   # for i in list:
   #     if max_num <i:
   #         max_num = i
   #  return max_num

   result = max(list)
   return result

print(max_list(scores))   #50

# 3. 최솟값
def min_list(list):
    result = min(list)
    return result

    # min_num = list[0]
    # for i in range(1, len(list)):
    #     if min_num > list[i]:
    #         min_num = list[i]
    # return min_num

print(min_list(scores))   #3

# 4. 평균
def avg_list(list):
    avg = sum(list)
    result = avg/len(list)
    return result

    # temp = 0
    # count = 0
    # for score in list:
    #     temp += score
    #     count += 1
    # result = temp/count
    # return result

print(avg_list(scores))   #20.75

# 5. 짝수인 것만 세기 /짝수 개수
def count_even(list):
    result = 0
    for i in list:
        if i % 2 == 0:
            result += 1
    return result

print(count_even(scores))   #3

# 6. N개의 0을 가진 리스트 만들기
def make_list(list):
    result = [0 for _ in range(list)]
    return result

print(make_list(6))   #[0, 0, 0, 0, 0, 0]
print([0 for _ in range(6)])
