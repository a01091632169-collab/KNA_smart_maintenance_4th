#연산자(계산, 비교, 논리)와 변수할당 연습

# 실습1 사칙연산 계산기
a=17
b=5
print(a+b, a-b, a*b, a/b) #22, 12, 85, 3.4
print(a//b, a%b, a**b) #3, 2, 1419857 

#실습2 평균과 도형 계산
side_a, side_b, side_c = 3, 4, 5 #변수3개이자 직육면체  
average= (side_a+side_b+side_c)/3
length = 10 #정사각형 한 변의 길이
width = length*length #정사각형 넓이
volume = side_a*side_b*side_c  #직육면체 부피
print(average, width, volume) #예상결과:4, 100, 60

#실습3 비교연산출력
print('a'=='a')
print("a"!="a")
print(5>3)
print(5<3)
print(5>=3)
print(5<=3) #TFTFTF 예상

#실습4 정상범위와 다중센서 판정
temp = 85
temp_check = ((temp >=60)and(temp<=90)) #True
#temp_check = temp>=60 and temp<=90  //이렇게 바로 해도 됨
pressure = 5 
pressure_check = ((pressure >=3)and(pressure<=7))
all= (temp_check and pressure_check)
print("출력결과: 온도정상",temp_check, "압력정상",pressure_check, "모두정상",all)

#실습5 복합 할당으로 재고 추적
stock = 100
print(stock)
stock +=50  #입고>150
print(stock)
stock -=30 #출고>120
print(stock)
stock +=5 #반품>125
print(stock)

#실습6 설비 지표 계산
all=500 
trash=23
product_rate= (trash/all)*100
all_operation=24 
operation=21
operation_rate= (operation/all_operation)*100
print("불량률",product_rate,"%","가동률",operation_rate,"%")

#실습7 시간 변환과 상자 포장
all_time=500
hour=all_time//60
minute=all_time%60
print(hour,"시간",minute,"분")