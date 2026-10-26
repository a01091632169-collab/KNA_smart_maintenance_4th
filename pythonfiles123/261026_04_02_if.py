#조건문

#실습1 조건 하나로 나이 판정하기

# age= int(input("나이?"))
# if age >=19:
#   print("성인입니다")
# else :
#   print("미성년자 입니다")

#실습2 여러 갈래로 점수 등급 판정하기
# score = int(input("점수 입력"))
# if score >= 90:
#     print("A")
# elif score>= 80 :
#     print("B") 
# elif score>= 70 :
#     print("C") 
# else :
#     print("F")


#실습3 설비온도 상태 판정하기
# temp = int(input("측정온도?"))
# if temp > 80 :
#     print("위험")
# elif 80>= temp > 60 :
#     print("주의")
# else :
#     print("정상")

# #실습4 두 조건을 모두 만족하는지 검증하기
# id="admin"
# pw="1234"
# userid=input("ID 입력: ")
# userpw=input("PW 입력: ")
# if userid==id and userpw==pw :
#     print("로그인 성공")
# else :
#     print("로그인 실패")

#실습5 세 값으로 설비 종합 상태 판정하기
temp=int(input("온도: "))
vib=float(input("진동: "))
current=int(input("전류: "))
if temp>80 or vib>4.0 :
    print("위험:즉시 정지")
else: 
    if current>60 and temp>70:
       print("주의:부하 점검")
    elif vib>2.5 :
       print("주의:진동 관찰")
    else : 
        print("정상")