F="data/12_metro_compressor.csv"
import pandas as pd
import numpy as np
#실습1 앞뒤를 미리 보고 첫인상 잡기
# import pandas as pd

# df=pd.read_csv("data/12_metro_compressor.csv")

# print(df.head()) #앞부분 기본 줄 수(5줄) 출력 #4번째줄 오일온도 빈칸
# print(df.tail()) #뒷부분 기본 줄 수 출력(5줄)으로 마지막 번호 확인   #끝이 199

# print(df.head(3), df.tail(10)) #앞부분3줄 뒷부분10줄 확인 

#실습2 표의 뼈대 읽기
import pandas as pd
# FD = "data/12_metro_digital.csv"
# df = pd.read_csv(FD)
# print(df.shape) #파일 행렬 크기
# print(df.columns.tolist()) # 열마다의 자료형 출력
# print(df.dtypes) 
# print(df.head())
# print(df.info())

#실습3 info로 결측까지 한 번에 보기
# F="data/12_metro_compressor.csv"
# df = pd.read_csv(F)
# print(df.info())
# #r오일온도 199개 > 결측1개 

#실습4 통계 요약에서 이상 신호 찾기
# F="data/12_metro_compressor.csv"
# df = pd.read_csv(F)
# print(df.describe().round(2))

# state=df["가동상태"].values
# cur=df["모터전류"].values

# print(round(float(np.mean(cur[state == "가동"])), 2))   # 4.25
# print(round(float(np.mean(cur[state == "정지"])), 2))   # 0.04

#실습6 탐색 리포트 만들기
FS="data/12_metro_small.csv"
df=pd.read_csv(FS)
print(df.head())
print("크기",df.shape)
print(df.info()) #오일온도 non-null 29개 > 결측1개

stats=df.describe() #숫자정보 열 정보 변수에 저장

miss = int (df["오일온도"].isna().sum() ) #결측값의 수(결측값은 T)
#isna:각 값이 결측이면 True, 아니면False. sum:T는1 F는0 1의 값 더하기
print('오일온도 결측:', miss, '건')

mean_current = round(float(stats["모터전류"]["mean"]), 2)
median_current = round(float(stats["모터전류"]["50%"]), 2)
print("모터전류 평균/중앙값:", mean_current, median_current)

