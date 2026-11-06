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

#실습2 사이클타임 급변한 구간 찾기
time= col(0) #시점 불러오기
ct= col(1)   #사이클타임 불러오기

change = np.abs(np.diff(ct)) #이웃한 사이클 타임의 변화량을 절댓값으로 새 변수에 저장 
max_idx= change.argmax() #절댓값중에 젤 큰거 찾기(변화 젤 많은 구간)
print(max_idx,"번과",max_idx+1,"번 사이에서",change[max_idx],"만큼 변화")

#clip
#실습3 측정 오류값 범위 안으로 보정하기
cyl= col(2)
cyl[0]=9999
print(round(cyl.mean(),1))  #421.5
clipped=np.clip(cyl,100,300)
print(clipped.mean())    #227.5

#np.where, np.unique, return_counts
#실습4 상태를 세 단계로 나누어 세기
ct=col(1)
label = np.where(ct>=1000,2,np.where( (ct>=50)&(ct<1000), 1, 0))

states,counts = np.unique(label,return_counts=True)
print(states, counts) #[0 1 2] [46  2  2]
print(counts / counts.sum()) #[0.92 0.04 0.04]
# print("정상:",counts[0],"경고:",counts[1],"잼:",counts[2])
# print("비율은",counts[0]/50, counts[1]/50,counts[2]/50) 

#실습5 다중 센서 행렬 만들고 구간 잘라내기

M = np.stack([col(1),col(2),col(3),col(4)])
print(M.shape)  #(4,50) 출력

last = M[ :, -10:]  #모든행(:)(총4행)의, 마지막에서부터 10개열 뽑아내기 
print(last.shape)     #(4,10) 출력

#실습6 이상 시점 한 번에 정리하기
time,ct,p_cyl= col(0),col(1),col(2)                  #1.시점 · 사이클타임 · 실린더압력 세 열을 불러오기

                                                     #2 사이클타임이 가장 컸던 시점과 그때의 값 찾기
idx=ct.argmax()  #ct 최대시점과 그때의 값 찾기
print("사이클타임 max:",time[idx],"번,",ct[idx])  #인덱스49 시점50

change=np.abs(np.diff(ct))  #ct의 변화량구하고 절댓값 변환         #3  이웃한 값의 변화량이 가장 컸던 구간 찾기
max_change= np.argmax(change) #ct 변화량 중 가장 큰부분 인덱스 뽑기
print("급변:",time[max_change],"->",time[max_change+1]) #급변 구간 출력
#인덱스로하면 48>49, 시점으로하면 49>50

label=np.where((ct>=50) | (p_cyl<150),1,0) #조건부합1 부적합0     #4 사이클타임 50이상 or 실린더압력 150아래인 시점 경고로 보고 비율 구하기
print(round(label.mean(),2))

sorted= np.argsort(ct)                                           #5  사이클타임이 큰 순서로 상위 세 시점을 뽑아 함께 출력
print("상위 세 시점",time[sorted[-1]],time[sorted[-2]],time[sorted[-3]])
#top = np.argsort(ct)[::-1][:3]  #49 47 42
#print(time[top])  #50 48 43
