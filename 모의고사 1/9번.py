# 9. 중복되는 문자 제거
# "senteeeencccccceeeee" -> "sentence"
# 한줄만 변경

def solution(characters):
    result = [characters[0]]
    for i in range(1, len(characters)):
        if characters[i-1] != characters[i]:
            result.append(characters[i])
    return ''.join(result)

print(solution("senteeeencccccceeee"))