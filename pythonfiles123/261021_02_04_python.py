#name = input("이름: ")
#print("안녕하세요"+ name +"님")

#실습1 태어난 해 입력받아 출력하기
#age=int(input("나이: "))
#print("내년에는", age+1 , "살")

#숫자입력계산
# year=int(input("태어난 년도?"))
# age=2026-year+1
# print("내 나이는",age,"살 입니다")

#실습2 여러 개 값 입력받기
# country = input("어디 출신이세요?")
# city = input("어디 사세요?")
# print(country+"의"+city+"에 사시나봐용")

#실습3 두 수 입력받아 사칙연산
# a= int(input("숫자입력해주세요 : "))
# b= int(input("숫자입력해주세요2 : "))
# print("합=",a+b)
# print("차=", a-b)
# print("곱=", a*b)
# print("나누기=", a/b)

#실습4 입력값 비교해 출력하기
# temp = int(input("온도가 몇도인가요?"))
# print("80초과?", temp>80)
# print("0이상?", temp>=0)

#실습5 세 점수 받아 평균 구하고 기준 비교
score_a = int(input("a점수?"))
score_b = int(input("b점수?"))
score_c = int(input("c점수?"))
aver=(score_a+score_b+score_c)/3
print("평균은",aver,"이고,","기준점수 50점 이상:", aver>=50)
