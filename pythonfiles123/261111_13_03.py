import pandas as pd
# #실습1 로그에 설비 정보 붙이기
F= 'data/13_diecasting_shot.csv'
F2 = 'data/13_diecasting_master.csv'
df = pd.read_csv(F) #주조 로그 파일
df2 = pd.read_csv(F2) #설비 대장 파일
# print(df.shape,df2.shape)
# print(df.columns)
# print(df2.columns) #열출력해서 공통된칸 찾기
# #공통된 칸이름 : 설비ID >> 기준으로 삼고 두 표 합치기
# merged=df.merge(df2,on='설비ID',how='inner')
# print(merged.shape) #합치면 185행12열
# print(merged['라인'].head(2)) #합쳤을 때 라인 열의 위 두줄 출력

#실습2 합친 뒤 행 수로 검산하기
F= 'data/13_diecasting_shot.csv'
F2 = 'data/13_diecasting_master.csv'
df = pd.read_csv(F) #주조 로그 파일
df2 = pd.read_csv(F2) #설비 대장 파일
merge_inner=df.merge(df2,on='설비ID',how='inner')
print("inner",len(merge_inner)) #185
merge_left=df.merge(df2,on='설비ID',how='left')
print("left",len(merge_left)) #200
merge_outer=df.merge(df2,on='설비ID',how='outer')
print("outer",len(merge_outer))  #201
#inner는 주조로그파일에만 있고 설비대장파일에는 없는 설비ID가 있는 행이 삭제됨(매칭된것만 남음)
#left는 주조로그파일에만 있고 설비대장파일에 없더라도 합쳤을때 주조로그파일의 모든행에 열이 추가됨(빈칸으로).
print(merge_left[merge_left["라인"].isna()]["설비ID"].head(1),merge_left["라인"].isna().sum())#DIE-C-01 #15
#left의 라인결측설비15행 찾기
#라인은 대장파일에 존재하는 열 > 주조로그파일에만 있는 설비 ID는 매칭안되어서 열이 추가되지만 빈칸으로 남음
print(merge_outer[merge_outer["샷"].isna()]["설비ID"],merge_outer["샷"].isna().sum()) #DIE-D-01 #1
#로그파일에 없고 대장파일에만 있는 설비ID 찾기(로그파일에만 있는 열 칸이 비었는지 확인하면 됨)

#실습3 concat으로 위아래 합치기
F= 'data/13_diecasting_shot.csv'
df = pd.read_csv(F)
print(df.shape) 
part1 = df.iloc[:100].reset_index(drop=True)
part2 = df.iloc[100:].reset_index(drop=True)
#200줄짜리 로그 이등분하고 인덱스 각각 0부터 새로 매기기
stacked = pd.concat([part1,part2]) #합치기
print("크기:",stacked.shape, "라벨0인 행 개수:", len(stacked.loc[0]))
#크기와 라벨0인 행의 갯수 확인
restacked= pd.concat([part1,part2], ignore_index=True)
print(restacked.index[-1])
# 재번호 후 다시 합쳐서 마지막 인덱스 확인

#실습4 라인 정보를 붙여 점검표 만들기
F= 'data/13_diecasting_shot.csv'
F2 = 'data/13_diecasting_master.csv'
log = pd.read_csv(F) #주조 로그 파일
master = pd.read_csv(F2) #설비 대장 파일

joined=log.merge(master,on="설비ID",how="left")
with_line=joined[joined["라인"].notna()]
print(len(with_line))  #185
#라인이 비어 있는 줄을 빼고 남은 줄 수 확인(채워져있는 행의 개수 출력)

not_ok= with_line[with_line['품질등급']!="양품"]
#품질등급이 양품이 아닌행을 True처리, True인 행들만의 모든 열을 출력(그 줄 출력)
print(len(not_ok)) #양품이 아닌 줄 개수 #34

result=not_ok.sort_values("비스킷두께",ascending=False) #비스킷두께 값이 큰 것부터 내림차순 정리
print(result[["샷","설비ID","비스킷두께","품질등급"]].head(5).to_string(index=False))
#비스킷두께 내림차순으로 샷,설비,라인,두께,등급 상위 5행 출력 #198 192 43 197 171 에 해당하는 행이 출력됨






