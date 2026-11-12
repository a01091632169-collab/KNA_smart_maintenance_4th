import pandas as pd
#실습1 열 골라 꺼내기
df = pd.read_csv('data/13_diecasting_small.csv')
one= df["형체력"]
print(type(one)) #<class 'pandas.Series'>
print(one.head(3).tolist()) #[258.0, 257.0, 253.0]

two= df[["형체력","실린더압력"]]
print(type(two)) #<class 'pandas.DataFrame'>
print(two.shape) #(30, 2)
print(type(df[["형체력"]])) #<class 'pandas.DataFrame'>

#실습2 라벨과 번호로 행 골라내기
df = pd.read_csv('data/13_diecasting_small.csv')
print(df.loc[0,'샷']) #이름표 0번행의 '샷'(샷번호가 적힌 열) 출력 #1
print(df.iloc[0],["샷"]) #위에서부터 0번째 행을 고르고 거기서 샷에 해당하는 열 출력 #1
sorted=df.sort_values("형체력",ascending=False)
print(sorted.loc[0,"샷"])  #1
print(sorted.iloc[0],["샷"])  #23

#실습3 행과 열을 함께 잘라내기
df = pd.read_csv('data/13_diecasting_small.csv')
print(df.columns)
parts1=df.loc[0:4,["실린더압력","형체력"]]  
print(parts1,parts1.shape) #앞 다섯 줄의 실린더압력과 형체력 뽑고 크기 출력(5,2)
parts2=df.iloc[0:5,[2,6]]  
print(parts2,parts2.shape) 

#실습4 필요한 구간만 뽑아내기
df=pd.read_csv('data/13_diecasting_shot.csv')
print(df.shape) #200줄짜리 다이캐스팅 로그를 읽어 전체 크기를 확인
print(df.columns) #칸이름 확인
first=df.loc[0:9,["설비ID","비스킷두께","품질등급"]]  #0-9이름표로 뽑기
print(first,first.shape)
second=df.iloc[-5: , : ]  #위치번호로뽑기
print(second, second.shape)