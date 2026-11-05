import numpy as np

# #인덱싱, 슬라이싱
# # a= np.array([0,1,2,3,4])
# # print(a[0],a[-1])  # 0 4
# # print(a[1:4])      #[1,2,3]
# # print(a[::2])      #[0 2 4]

# # data = np.array([[70, 2.1], [72, 2.3]]) 
# # print(data[0])        # 출력: 행 전체 
# # print(data[ : , 0])     

# #실습1 특정구간 꺼내기
# data=np.array([4603,4604,4605,4603,4607,4609,4603,4611,4613,4603])
# print(data)
# print("맨 앞", data[0])
# print("맨 뒤", data[-1])
# print("2~4번 째 값", data[1:4])
# print("하나씩 건너뛴 값", data[::2])

# #실습2 한 시점과 한 센서 따로 꺼내기
# data=np.array([[4603,32.5],[4601,32.6],[4610,32.3], [4605,32.4]])
# print(data) #네 시점의 회전수와 토크를 한 줄씩 묶어 표로 만들기
# print(data[2]) # 세 번째 시점의 값 통째로 꺼내기
# print(data[:,[0]]) #모든 시점의 회전수만(0열) 세로로 모아 꺼내기
# print(data[:,[1]]) #모든 시점의 토크만(1열) 세로로 모아 꺼내기

# #브로드캐스팅
# table= np.array([[72,2.4],[95,6.8]])
# print(table.shape) #(2,2)
# base=np.array([70,2.0])
# print(table - base)  
# #  [[22,0.4]
# #   [25, 4.8]]

# #실습3 회전수를 0과 1사이로 맞추기
# rpm=np.array([4603,4603,4967,4603,4603,4603,4603,4987,4603,3632])
# low = rpm.min()
# high = rpm.max()                          
# norm = (rpm- low) / (high - low)   #모든값에서 최솟값뺀 것을 (최댓값-최솟값)으로 나누기
# result=np.round(norm,2)    #소수 점둘째자리에서 다듬어 출력
# print(result)

# print("0의 개수:", np.sum(result == 0))  #np.sum은 True의 갯수를 세는것
# print("1의 개수:", np.sum(result == 1))
# #가장작은값이 0 가장큰 값이 1 이 되는 10개짜리 배열 출력

#실습4 저회전 이상 시점 걸러내기
rpm=np.array([4603,4603,58,4603,4603,1216,4603,4603,1217,4603])#회전수 묶음 
current=np.array([2,3,21,2,3,2,2,3,2,147]) #전류 묶음 준비

low_rpm = rpm <2000   #low_rpm=np.array([False, True, True])을 의미
print(rpm[low_rpm]) #회전수 2000미만 항목 출력
print(rpm[low_rpm],current[current>25]) #회전수 2000미만 또는 전류25초과 참거짓묶음

print(np.sum(low_rpm)) #저회전 횟수 출력(항목갯수)
print(np.sum((low_rpm) | (current>25))) #저회전, 고전류 횟수

print(np.mean(low_rpm)*100, "%") #T/F들의 평균(1/0)>백분율
print(np.mean((low_rpm)|(current>25))*100, "%")

#실습5 조건에 걸린 시점의 개수와 비율 세기
tq= np.array([2,2,21,2,3,2,2,3,2,147]) #토크열개묶음
high = tq>10  #10넘는지 판단해서 TF로 저장
print(high) #[False False  True False False False False False False True]
print(high.sum()) #2  high에서 True 갯수
print(round(high.mean(),2))  #0.2 true,false(1,0)값들의 평균으로 비율 구하기

#실습6 센서별 평균과 표준편차 구하기
#4시점 x 2센서
data=np.array([[4603,2],[4967,21],[3632,147],[58,5]])
print(np.round(data.mean(axis=0),1))  #세로로 평균
print(np.round(data.std(axis=0),1))   #세로로 표준편차


# #파일에서 배열로 불러오기(np.loadtxt)
# rpm=np.loadtxt('data/10_mct_tool.csv',
#                 delimiter=",",               #값을 나누는 기호
#                 skiprows=1,                  #첫 줄(제목) 건너뜀  
#                 usecols=4)                   # 5번째열=회전수
# print(rpm)     


# rpm_tq=np.loadtxt('data/10_mct_tool.csv',
#                 delimiter=",",               #값을 나누는 기호
#                 skiprows=1,                  #첫 줄(제목) 건너뜀  
#                 usecols=(4,5))                   # 5열 회전수,6열 토크 둘다 가져올때
# print(rpm_tq)
# print(rpm.shape)  #40 #값(행 즉 리스트)이 몇개있는지   

#실습7 파일에서 회전수를 불러와 통계내기
rpm=np.loadtxt('data/10_mct_tool.csv',delimiter=",",skiprows=1,usecols=4)
print("회전수 평균:", rpm.mean())
print("표준편차:",round(rpm.std(),2))
print("최소:",rpm.min(),"최대:",rpm.max())

#실습8 걸러낸 값들만 모아 통계 내기
tq=np.loadtxt('data/10_mct_tool.csv',delimiter=",",skiprows=1,usecols=5)
over_tq = tq>10    #10넘는 토크들만 변수에 리스트 형태안에 True로 저장
print(tq[over_tq])  #True리스트에 해당하는 값들을 tq변수에서 실제값 뽑기
print("개수",np.sum(over_tq)) #사실 true값들(1)의 합. 4개니까 1x4=4
print(tq[over_tq].mean()) #전체평균

#실습9 불러오기부터 통계까지 한 흐름으로
rpm_tq=np.loadtxt('data/10_mct_tool.csv',delimiter=",",skiprows=1,usecols=(4,5))

print("구조:",rpm_tq.shape, rpm_tq.dtype) #몇줄몇칸, 어떤 종류인지
rpm= data[:, 0]  #모든행의 첫번째열만 꺼내기 > 회전수 열의 내용만 사용
low= rpm[rpm<2000]
print("이상시점 개수:", low.size, "이상 평균", low.mean()) #이상회전수 개수와 평균
print(rpm.mean())   #회전수 평균