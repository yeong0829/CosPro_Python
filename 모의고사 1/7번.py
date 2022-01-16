# 7. 파일형식, 파일명, 파일크기
'''
파일 형식이 "jpeg"이고, 파이릌기가 1,000보다 작은 파일만 업로드 할 수 있음
파일정보: "jpeg,all.jpg,500"    결과: 업로드 가능
파일정보: "mpeg,all.mp3,500"    결과: 업로드 불가능 - 파일형식 불가
'''

def solution(file_info):
    sucess = 0
    fail = 0
    for f in file_info: # f = jpeg,all.jpg,500
        splited = f.split(",") # splited = ["jpeg", "all.jpg", "500"]
        if splited[0] == "jpeg" and int(splited[2]) < 1000:
            sucess += 1
        else:
            fail += 1
    return sucess, fail

print(solution(["jpeg,all.jpg,500", "mpeg,all.mp3,500"]))