#f-string

# name= "홍길동"
# age= 25
# print(f'{name}님은 {age}살 입니다')
# code= "EQP-001"
# print(f'설비{code} 점검 완료') #중간에 '설비'+ code+ "점검완료" 이런거 불편

#실습1 f-string으로 변수 끼워 출력하기
name= "PUMP_A"
temp = 87
print(f'설비{name}, 온도{temp}')

#실습2  f-string 안에서 계산하기
score_a = 84
score_b = 87
score_c = 90
print(f'점수a:{score_a}, 점수b:{score_b}, 점수c:{score_c}. 평균: {(score_a+score_b+score_c)/3}')

value=12.3456
print((f'{value:.2f}'))
print((f'{value:.1f}'))
print((f'{value:.3f}'))

#실습3 소수점 자릿수 지정하기
value=87.456
print(f'{value:.1f}/{value:.2f}')

#실습4 센서 로그 한 줄 정리 리포트 만들기
text=" 5, sensor_2, WARNING, 0.78912 "
print(text)
text2=text.strip().split(",")  #공백지우고 리스트 안에 나열
print(text2) 
sensor=text2[1].strip()  #센서 정보 뽑아서 공백제거
state=text2[2].strip().lower()   #상태 정보 뽑아서 공백제거, 소문자변환
value=float(text2[3].strip())
print(f"[센서 {sensor}] 상태 {state}, 측정값 {value:.2f}")
# <출력결과> : [센서 sensor_2] 상태 warning, 측정값 0.79  

