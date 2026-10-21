#자료형

count = 3 #int 정수
temp = 25.5 #float 실수
name = "센서A" #str 문자열

#type() > 자료형 알려줌
# print(type(25))  >>int
# ok = True  //bool형으로 선언
#print(type(ok)) >> bool

#실습1 여러 자료형 변수 만들기
count = 3 #int변수
temp = 25.0 #float변수
name = "sensor_A" #str변수
is_ok = True #bool변수
print(count)
print(temp)
print(name)
print(is_ok)

#실습2 type()으로 자료형 확인하기
print(type(count))
print(type(temp))
print(type(name))
print(type(is_ok))

#실습3 자료형 맞히기 퀴즈
#100은 정수형int
#100.0은 실수형float
#"100"은 문자열형str
print(type(100), type(100.0), type("100"))

#실습4 문자열 숫자와 숫자 비교하기
print(3 + 5) #진짜 숫자끼리 더하기
#print("3" + 5) #글자 + 숫자
#print("30"+"55") #두 자리 문자 숫자 # 3050

#실습5 bool값 만들어 확인하기
#print(3>2) True가 나올 것이라 예상
print(3>2)
print(5==5)  #print(5==5) True 가 나올 것이라 예상
a_bool= True 
print(type(a_bool)) #a_bool이라는 값을 비교하는 자료형 출력해보기

#실습6 변수의 자료형 변경하기
abc = 3 #정수 변수 선언
print(type(abc))
abc = 3.0 #이전에 선언한 정수 변수를 실수로 재할당
print(type(abc))
abc = "3.0" #숫자(실수상태)를 글자로 재할당
print(type(abc))

#실습7 직접 자료형 표현하기
device_temp = 25.0 #실수변수선언
check_count = 5 #정수변수선언
device_name = "sensor_AA" #문자열자료형할당
is_normal = True #bool형선언
print(type(device_temp),type(check_count), type(device_name), type(is_normal))