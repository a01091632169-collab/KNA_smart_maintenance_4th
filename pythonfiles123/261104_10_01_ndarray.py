import numpy as np

#리스트 vs 배열
#1)리스트 : 서로 다른 자료형도 같이 존재 가능. 느리고 반복문 돌아야함
list = [70,72,71]
print(list*2)   #[70, 72, 71, 70, 72, 71] 이 출력됨. 이런거말고 값을 두배를 원함!
print([v * 2 for v in list]) #2배 되긴한데 반복문 돌아서 느리고 복잡 > 배열 사용
#2)배열 : 같은 자료형만 존재가능. 빠르다
temp =np.array([70,72,71])  #리스트값을 안에 넣어서 배열을 만듦
print(temp) #[70 72 71]
print(temp+2) #[72 74 73] #배열은 리스트에는 있는 콤마가 없음
#튜플로 배열 만들기
print(np.array((1,2,3)))  #배열안에 튜플이 들어가도 됨

#실습1 온도 배열 만들고 화씨로 바꾸기
temps=np.array([30,30,30,30,29,30])
print("측정온도: ", temps)
print("화씨: ", temp*1.8 + 32)


#배열생성
#np.arrange(시작,끝, 간격) 끝값은 포함되지 않음
#np.linspace(시작,끝, 개수) 끝값 포함

#실습2 전류 구간을 같은 간격의 값으로 채우기
current= np.linspace(0,70,8) 
print(current)

#실습3 측정 순번 배열 만들기
num = np.arange(0,40,5) #측정이 40번, 간격이5번
print(num)

#실습4 두 센서 표의 구조 확인하기
temp_current = np.array([[30,15.44],[30,18.69],[33,62.48],[38,18.37]])
print("차원", temp_current.ndim)
print("형태", temp_current.shape)
print("개수", temp_current.size)

#실습5 전류 자료형 확인하고 정수로 바꾸기
current=np.array([[18.69],[17.05],[18.37],[16.83]])
print(current.dtype)
print(current.astype(int))

# reshape : 형태 바꾸기 / flatten : 1차원으로 만들기

#실습6 사이클타임을 표 모양으로 정리하기
values=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(values)
values2= values.reshape(3,4)
print(values2)

#실습7 세 센서 표로 정리하고 다시 펴기
values=np.array([30,18,50,25,17,45,28,19,50,31,18,55])
print (values)
list_4_3=values.reshape(4,3)
print(list_4_3)
print(list_4_3.flatten())
