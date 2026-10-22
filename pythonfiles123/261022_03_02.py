#인덱싱과 슬라이싱
#인덱싱-위치 번호로 글자 하나 꺼내기/ 형식: 문자열[번호]

   #문자열 변수를 만들고 거기서 출력

#실습1,2 양수인덱스, 음수인덱스 꺼내기
word="SIGNAL"
print(word[0],word[2],word[5]) #양수 인덱스
print(word[-1], word[-2])  #음수 인덱스

# print(word[ :3]) 
# print(word[0:3])
# print(word[3: ]) 
# print(word[3:6])

#실습3 구간자르기
word="SIGNAL"
print(word[0:3]) #SIG
print(word[2:5]) #GNA

 #실습4 앞부분 가져오기 (start 생략)
word = "temp_sensor"
print(word[ :4])

#실습5 뒤쪽 전체 가져오기 (end 생략)
word = "temp_sensor"
print(word[5: ]) 

#실습6 뒤 n글자 가져오기
word="sensor_01"
print(word[-2: ])

#실습7 건너뛰며 가져오기
word="SIGNAL"
print(word[0::2])

#실습8 문자열 뒤집기
word="SIGNAL"
print(word[ ::-1])