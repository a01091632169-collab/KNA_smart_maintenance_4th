import numpy as np

F = 'data/11_diecasting_series.csv'

ct = np.genfromtxt(F, delimiter=",", skip_header=1, usecols=1)
print(ct.shape, ct.dtype) #(50,) float64

def col(c):
    return np.genfromtxt(F, delimiter=",", skip_header=1, usecols=c)


# #자리 찾기
# #fanct indexing : 여러 위치 한 번에 추출 가능(떨어진 자리도 한 번에 가능)

# vib = np.array([2.1,2.3,2.0,5.8])
# pick = np.array([0,3])
# print(vib[pick])   #[2.1 5.8]

# #정렬과 정렬순서
# print(np.sort(vib))     #[2.  2.1 2.3 5.8]
# print(np.argsort(vib))  #[2 0 1 3]

# #argmax, argmin
# vib = np.array([2.1, 2.3, 6.1, 2.0, 5.8])
# cycle = np.array([1, 2, 3, 4, 5]) #진동값의 위치를 나타내는 배열

# pos = np.argmax(vib) #3번째위치 즉 인덱스2가 저장됨
# print(cycle[pos])  #인덱스2는 3
# # 출력: 3

#실습1 최대 사이클타임 시점 찾기
#사이클타임이 제일 긴 시간을 찾아서 번호와 시간을 출력

#time = np.genfromtxt(F, delimiter=",", skip_header=1, usecols=0)
#ct = np.genfromtxt(F, delimiter=",", skip_header=1, usecols=1)

def col(c):
    return np.genfromtxt(F, delimiter=",", skip_header=1, usecols=c)

time=col(0)
ct=col(1)

idx = ct.argmax()  #사이클타임 최대일때 인덱스 알기
print(time[idx], ct[idx]) #인덱스를 시점과 사이클타임에 넣어서 값 출력하기 

