import numpy as np
F = 'data/11_hydraulic_cooler.csv'
def col(c):
    return np.genfromtxt(F, delimiter=",", skip_header=1, usecols=c)

x= np.array([2.0,np.nan,4.0])
print(np.isnan(x))  #f t f
print(np.isnan(x).sum()) #1

#결측값 무시 nanmean
temp = np.array([70.1, np.nan, 71.2, 70.8])
print(np.mean(temp))  #nan
print(round(float(np.nanmean(temp)), 2)) #70.7

#실습1 결측 확인하고 결측 제외 통계내기
vib=col(2)

print("결측 수:", np.isnan(vib).sum()) #6 #결측수 
print("비율:", np.isnan(vib).mean()) #0.12 #np.isnan(vib)가 T/F로 돼서 평균구하면 비율
print("결측 제외 평균:", round(float( np.nanmean(vib)), 3)) #0.566
print("일반 평균: ", np.mean(vib) ) #nan

#사분위수
vib_s=np.array([2.0,2.2,2.5,2.8,3.0,6.5])
print(np.round(float (np.percentile(vib_s,25)) ,2))
print(np.round(float (np.percentile(vib_s,75)) ,2))
#여러자리 한번에
print(np.round(float(np.quantile(vib_s,0.25)),2))

#IQR = Q3-Q1, 경계:(Q3-Q1)x1.5+Q3
#실습2 IQR로 이상치 찾기
temp=col(1)
q1,q3=np.round(np.percentile(temp,[25,75]),2)
iqr=q3-q1
upper=np.round(1.5*iqr+q3,2)
print("상한값:",upper)
print("걸리는 값",temp[temp>upper])

#z-score = (값-평균)/표준편차. 절댓값z>2 이면 이상치
#실습3 z-score로 이상 시점 찾기
time=col(0)
temp=col(1) #시점과 온도 불러오기

mean_temp= np.mean(temp) #평균
std_temp=np.std(temp)  #표준편차
z=(temp - mean_temp)/std_temp #(값- 평균)/표준편차 
print(time[np.abs(z) > 2])  
print(np.round(max(z),2))

#실습4 경보 판정하기
time=col(0)
temp=col(1) #시점과 온도 불러오기

temp_mean= np.nanmean(temp)
temp_std=np.nanstd(temp)  #온도의 평균과 흩어진 정도

upper=temp_mean + 3*temp_std
print("상한", np.round(upper,2)) #평균+3x표준편차=상한

cycle=time[temp>upper]
print("걸리는 사이클",cycle) #상한을 넘는 온도의 사이클 출력

#실습5 상관관계 확인하기
temp= col(1)
effi= col(3)

corr_=np.corrcoef(temp,effi) #상관계수(표형태)
corr=round(float(np.corrcoef(temp,effi)[0,1]),2) #필요한칸 하나만+소수점 자르기
print(corr) #-0.99 > 온도가 오르면 냉각효율은 떨어짐

#실습6 센서별 통계 한 번에 구하기
temp=col(1) ; vib=col(2) ; effi=col(3) ; power=col(4) #유압데이터 4열 불러오기

data= np.stack([temp,vib,effi,power])#네 묶음을 위아래로 쌓기 > 행이 센서, 열이 시점
print(data.shape) #(4,50)
mean=np.round(np.nanmean(data, axis=1),1) #센서마다(행 별) 따로 평균 나오게 방향 지정
print("센서 별 평균",mean)   #[37.7   0.57 44.7  57.7 ]
std=np.round(np.nanstd(data, axis=1),1)
print("흩어진 정도", std)   #[6.  0.1 7.6 1.6]

#실습7 변화 경계 후보 찾기
time=col(0) ; temp=col(1)
cs=np.cumsum(temp-np.nanmean(temp)) #온도-평균의 누적합
mincs=np.argmin(cs)  #누적합이 가장 작아지는 자리
print("사이클타임",time[mincs],"누적합",round(cs[mincs],1)) 

# 온도(1열)와 냉각효율(3열)로 2×50 배열 생성
F = "data/11_hydraulic_cooler.csv"
data = np.genfromtxt(F, delimiter=",", skip_header=1, usecols=(1, 3)).T
m = np.nanmean(data, axis=1, keepdims=True) #행별 평균 (2,1)
s = np.nanstd(data, axis=1, keepdims=True) 
score = np.abs((data - m) / s).sum(axis=0) #(값-평균)/표준편차=z > z절댓값의 합
print(np.argmax(score))      # 49 (0부터 세는 인덱스)
print(np.argmax(score) + 1)  # 50 (사이클 번호)

#실습8 종합 이상 점수로 정비 우선순위 정하기
time=col(0) ; temp=col(1); effi=col(3); status=col(5)
def z (a):
    return np.abs( (a-np.nanmean(a))/np.nanstd(a))  #z score 함수

score= z(temp) + z(effi) #종합점수

i = np.nanargmax(score) #종합점수가 가장 높은 곳의 인덱스
print( "최고점수", int(time[i]), "번", round(score[i],2) ) #최고점수 시점과 z값
#최고점수 50 번 6.79

top= np.argsort(score)[ ::-1][:3] #상위 세 시점
print("상위 세 시점", time[top].astype(int))
#상위 세 시점 [50 49 48]