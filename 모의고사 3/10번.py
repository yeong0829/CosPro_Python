#10
def solution(strings):
    result=0
    for s in strings:
        length = len(s)
        result += (length /4)
        if length %4 !=0:
            result +=1
    return result