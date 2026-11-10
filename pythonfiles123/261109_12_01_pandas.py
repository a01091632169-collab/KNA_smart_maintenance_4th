


# # #실습1 설비 센서 파일 불러와 확인하기
# # import pandas as pd  
# # df = pd.read_csv("data/12_metro_compressor.csv") #첫줄을 열 이름으로 사용(헤더로 인식)
# # print(df.head( ))  #표의 맨위 5행 가져오기
# # print(df.shape)   #변수에 담은 것이 몇줄 몇칸인지
# # print(df.head(3))  #앞부분 몇 줄 화면에 띄우기 (3줄)
# # print(df) #빈칸있나 확인 > 표 전체 출력

# # #실습2 필요한 열만 이름으로 골라 읽기
# # import pandas as pd  
# F="data/12_metro_compressor.csv"
# FS="data/12_metro_compressor_semicolon.csv"
# # print(pd.read_csv(F).shape) #원래파일크기 (200,7)

# # sel=pd.read_csv(F,usecols=["측정시각","오일온도","모터전류"])
# # print(sel.shape) #(200,3) #열이 몇 개로 줄었는지 크기 출력
 
# # part=pd.read_csv(F,nrows=20)
# # print(part.shape) #(20,7) #행이 몇 개로 줄었는지 크기 출력

# #실습3 구분자와 인코딩 맞춰 읽기
# import pandas as pd
# semicolon=pd.read_csv(FS)
# print(semicolon.shape)  #(200,1) #세미콜론으로 구분자가 되어있어서 다 한 열에 출력됨

# sc=pd.read_csv(FS,sep=";",encoding="utf-8")
# print(sc.shape) #(200,7) #값을 나누는기호(세미콜론) 다시 지정후 읽기

# print(sc.columns.tolist()) #['측정시각', ....'모터전류', '가동상태']
# #한글 열 출력

#실습4 옵션을 한 번에 적용해 읽기
import pandas as pd
F="data/12_metro_compressor_semicolon.csv"
sc=pd.read_csv(F,sep=";",encoding="utf-8",  #구분자, 글자읽는법 정하기
              usecols=["측정시각","오일온도","모터전류"], #세 열만 고르기  
              nrows=50)   #앞에서부터 50줄만 읽기
print(sc.shape) #크기 출력
print(sc.head(3)) #앞부분3줄만 출력해서 확인  