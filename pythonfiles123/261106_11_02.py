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
abs_temp=np.std(temp)  #표준편차
z=(temp - mean_temp)/abs_temp #(값- 평균)/흩어진정도(표준편차)
print(time[np.abs(z) > 2])  
print(np.round(max(z),2))