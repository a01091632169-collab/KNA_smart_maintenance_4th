# 실습１ 변수출력하기（숫자, 문자）
temp = 25
print (temp)
name = "센서A"
print(name)

#실습２ 변수 수정(변수값, 변수명)
temp = 30
print(temp)
temperature = temp
print (temperature)

# 실습3 직접 변수 만들어 출력하기
my_number = 7
print (my_number)
mood = "good"
print(mood)

# 실습4 나이/점수/개수 변수로 표현
age=25
label = "나이"  #설명용 글자 변수
print(label)
print(age)

# 실습5 변수 값 바꿔가며 추적하기
x=10
print(x)
x= x+5
print (x)
x= x*2
print (x) 

# 실습6 두 변수 값 옮기고 바꾸기
a=100
b = a
a = 999
print(a) 
print(b) # a를 999로 설정하기 전에 b에 복사했으므로 b는 기존의 a값이 출력됨

# 실습7 오류내고 고치기
temp_ = 25
print(temp_)
score_ = 90
print(score_)

# 실습8 주석으로 변수 설명 달기
temp = 25 #섭씨온도
count = 3 #센서개수
#temp = 100 //주석문장
print(temp)

# 실습9 값 예측 미니 퀴즈
x=5
x=10
x= x+1
# 11이 나올듯
print(x)

# 실습10 정보 카드 만들기
print("자기소개카드")
name = "chaeyoung"
age = 25
city = "pohang"
print("name:", name), print("age:", age), print("city:",city)

# 실습11 변수 이름 다듬기
a=25
b= 3
temp_a = 25
count_a = 3 #상세하게 알아볼수있는말로 
print(temp_a)
print(count_a)

# 실습12 변수 한 줄 만들기 도전
x,y,z=1,2,3
width, height = 4,3
print(width), print(height)
print(z)