#예외처리 
#else, finally

#실습1 finally로 파일 안전하게 닫기
# import csv
# try:
#     f= open("data/09_ict_inspection.csv","r",encoding="utf-8")
#     header = f.readline()
#     print(header.strip())
# except FileNotFoundError :
#     print("파일이 존재하지 않습니다")
# finally:
#     f.close()
# print("파일이 안전하게 닫힘")

#실습2 CSV를 안전하게 읽기
#파일안에 여러 행렬에서 0행(헤더이자 제목)빼고 측정값에 해당하는 숫자만 저장해서 합산 출력
try: 
    with open("data/09_ict_inspection_dirty.csv","r",encoding="utf-8") as f:    
        rows = f.readlines()[1:]   #헤더는 빼고 저장(숫자값들을 추가해야하니까)
except FileNotFoundError :
    rows = []   #파일이 없으면 빈 결과 

total= 0.0
skipped = 0
for line in rows :
    try:
        total += float(line.split(",")[2]) #측정값칸(인덱스[2])의 숫자들을 더함
    except (ValueError , IndexError):
        skipped +=1
        continue

print("합계: ",round(total,1),"\n건너뜀", skipped)


#실습4 여러 파일 묶어 처리하기
#파일리스트중 있는 파일은 읽고 갯수세고, 없는 파일은 건너뛰는 코드
names = ["data/09_ict_inspection.csv",
         "data/09_없는파일.csv",
         "data/09_ict_inspection_dirty.csv"]
done = 0 
for name in names :
    try:
        with open (name, "r",encoding="utf-8") as f:
            rows=f.readlines()[1:]  #헤더빼고 데이터행들 담기
        print("읽기 성공", name, len(rows),"행")  #데이터 행 수 출력
        done +=1
    except FileNotFoundError :
        print("건너뜀", name)
        continue
print("처리한파일:",done) #처리한 파일 수만 출력 

#실습5 함수 안에서 입력값 검증하기
def check_value(text, lo=0.0, hi=5000.0):
    v = float(text)
    if not (lo < v < hi) :  #범위 밖이면 valueError 발생
        raise ValueError(f'정상 범위 밖: {v}') #괄호안에 오류메시지를 담음
    return v      #여기까지 함수 정의
for t in ["128.5","결측","-999"]:
    try:
        print("통과:", check_value(t))
    except ValueError as e: #e가 위에 괄호안 내용
        print("제외", e)
