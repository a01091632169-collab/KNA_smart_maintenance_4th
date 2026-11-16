import pandas as pd
#실습1 한 조건으로 행 거르기
df = pd.read_csv('data/13_diecasting_shot.csv')
print(df.shape)
condition = df["비스킷두께"]>=16
print("참의갯수:",condition.sum()) #참의 갯수 #74
print(df[condition],"행 개수",len(condition)) #실제 행 출력, 전체 행의 갯수 #200
condition2 = df["비스킷두께"]<16
print("16미만 수의 갯수",condition2.sum()) #16보다 적은 수의 개수 #112
print("16이상 + 16미만 행 수", condition.sum()+condition2.sum()) #186

#실습2 두 조건 묶기
df = pd.read_csv('data/13_diecasting_shot.csv')
condition= (df["비스킷두께"]>=16) & (df["사이클타임"] >=25)  #여기까진 T/F로 모든행이 저장
print("비스킷두께16이상 and 사이클타임25이상 개수",(condition.sum())) #72 #T(1)만 다 더해서 개수 세기
condition2= (df["비스킷두께"]>=16) | (df["사이클타임"] >=25)
print("비스킷두께16이상 or 사이클타임25이상 개수",(condition2.sum())) #86
#조건.sum() 은 조건을 만족하는 것의 갯수 = len(df[조건]) # print(len(df[condition]))=72
condition3= ~(df["품질등급"]=="불량")      #불량인 조건에 물결> 불량이 아닌 조건
print("불량이 아닌 개수",len(df[condition3])) #180

#실습3 목록과 범위로 거르기
df = pd.read_csv('data/13_diecasting_shot.csv')
print( len(df [df["품질등급"].isin(["주의","불량"]) ] ))#38 #품질등급열에서 주의나 불량인 샷 줄 수 출력
print(len( df[df["비스킷두께"].between(10,16) ] ))#117  #비스킷두께가 10~16사이인 샷 줄 수 출력
print(len( df[df["설비ID"].str.contains("A")] ) )#111 #설비이름에 A가 들어간 샷 줄 수 출력
print(len( df[df["설비ID"]=="DIE-A-01"]  ))#63 #A라인 1호기 줄 수 출력

#실습4 비스킷두께 기준으로 정렬하기
df = pd.read_csv('data/13_diecasting_shot.csv')
sorted = df.sort_values("비스킷두께", ascending=False)
print(sorted["샷"].head(5).tolist()) #[198, 192, 43, 171, 197] #비스킷두께 내림차순 정렬 후,상위 5개 행의 샷 번호를 리스트로 출력
sorted2 = df.sort_values(["품질등급","사이클타임"],ascending=[True,False]) 
#문자열에서 가나다순으 오름차순>True #품질등급 가나다순, 사이클타임 내림차순 정렬 
print(sorted2["샷"].head(5).tolist()) #[200, 181, 182, 191, 196]

print(df["샷"].head(5).tolist()) #원본의 앞5줄 [1, 2, 3, 4, 5]

#실습5 조건과 정렬로 리포트 만들기
df = pd.read_csv('data/13_diecasting_shot.csv')
state= df[ (df["품질등급"]!="양품") & (df["비스킷두께"]>=16) ]
#양품아니고 비스킷두께 16이상인 조건 묶기
#마지막에 df[]로 한 번 더 묶어줘서 True에 해당하는 행의 모든 열정보가 담기는것
print(state.shape) #(25,8)
print(len(state)) #25
sorted=state.sort_values("비스킷두께",ascending=False)
#걸러낸 결과를 비스킷두께가 큰 순서(내림차순)로 줄 세우기
report=sorted[["설비ID","비스킷두께","품질등급"]]
print(report.head(5)) #세열만 상위 5줄 출력

x= df[ (df["품질등급"]!="양품") & df["비스킷두께"].isna() ]
#결측때문에 제외된 양품이 아닌 샷 #isna는 값이 비어있는지 결측값확인 메서드
print(len(x)) #3
