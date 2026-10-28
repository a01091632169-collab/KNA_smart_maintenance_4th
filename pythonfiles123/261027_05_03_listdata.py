#리스트 데이터 처리

#실습1 조건에 맞는 값만 출력하기
temp = [29,32,35,25,26,28,31]
for a in temp :
    if a >=30 :
        print("고온: ", a)

#실습2 두 조건을 모두 만족하는 값 고르기
timelist=[8,6,12,15,10,9]
for a in timelist :
    if a>=5 and a<=10 :
        print(a)

#최댓값 최솟값 찾기
temps=[25,32,28,35,27]
biggest = temps[0]
for t in temps:
    if t > biggest :
        biggest = t 
print (biggest)

#실습3 조건에 맞는 값만 골라 평균 구하기
temps=[32,36,31]
count= 0
add=0 
for t in temps:
    if t >30 :
       add+=t
       count+=1
print("고온 평균: ", add/count)      

#빈 리스트에서 시작해 값 채우기
temps=[25,26,24,28]
doubled=[]
for t in temps :
    doubled.append(t*2)
print(doubled)      #[50,52,48,56]

#조건에 맞는 값으로 새 리스트 만들기
temps = [25,32,28,35,27]
high = []
for t in temps :
    if t >30:
        high.append(t)
print(high)      #[32,35]

#실습4 조건에 맞는 값으로 새 리스트 만들기
templist=[32,28,25,35,29,27,31,33]
new=[]
for t in templist :
    if t > 30 :
        new.append(t)
print(new)
print(len(new))

#실습5 값을 가공해 새 리스트 만들기
temp=[25,26,24,28,27]
fahrenheit=[]
for t in temp:
    fahrenheit.append(t*1.8+32)
print(fahrenheit)

#실습6 센서 데이터 종합 분석하기
temps=[25,32,28,35,27,31,24,33,29,36]
total=0 ; over_total=0
new=[]
for t in temps:
    total += t
    if t >30 :
        new.append(t)    
        over_total += t  
print("전체평균: ", total/len(temps))
print("고온개수: ", len(new))
print("고온평균: ", over_total/len(new))
#############################################
temps=[25,32,28,35,27,31,24,33,29,36]
total=0 ; hot_total=0
hot=[]
for t in temps:
    total+=t
    if t > 30:
            hot.append(t)
print("전체평균: ", total/len(temps))
for h in hot :
    hot_total+=h
print("고온평균: ", hot_total/len(hot))