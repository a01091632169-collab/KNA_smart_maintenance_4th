#문자열
# 따옴표 안에 표현
notice =''' 안내
1.전원
2. 센서
'''
print(notice)

#이스케이프 : \n 줄바꿈, \t 탭
print("이름\t 상태")
print("첫줄\n둘째 줄")

#실습1 여러 줄 문자열 만들기
note = """ 가동 점검표 \n 1. 온도 확인 \n 2. 압력확인 """
print(note)

#실습2 설비 라벨 이어 붙이기
code = "PUMP_A"
state = "정상"
date = "2025-01-15"
print(code+"/"+state+"/"+date)

#실습3 설비 정보 카드 만들기
code = "PUMP_A"
state = "정상"
on_time = str(10)  #int
date = "2025-01-15"
print("설비:"+ code + "\n 상태:" + state +"\n가동시간:" + on_time + "\n점검:" + date)