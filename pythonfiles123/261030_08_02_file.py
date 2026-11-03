# f = open('data/08_press.csv', 'r', encoding='utf-8')   # f = 파일객체(연결통로)
# print(type(f).__name__)   # TextIOWrapper
# f.close()

# f= open('data/08_press.csv', 'r', encoding='utf-8') 
# lines = f.readlines()
# print(type(lines).__name__, len(lines))   # list 13
# f.close

#실습1 open으로 파일 열기
# f= open("data/08_press.csv", "r", encoding="utf-8")
# read_text= f.read()  #전체를 읽고, 한 덩어리 문자열로
# print("[read결과]")
# print(read_text)
# f.close
# f= open("data/08_press.csv", "r", encoding="utf-8")
# read_lines= f.readlines()  #전체를 읽고, 줄단위 리스트로
# print("[readlines결과]")
# print(read_lines)
# f.close 

# #실습2 with open으로 파일에 쓰기
# with open ("data/test.txt","w",encoding="utf-8") as f: #파일열어서 f라는 변수에 담음
#     f.write("쓰기 테스트\n")  #파일들어가면 덮어써져 있음
#     f.write("이상 없음\n")
# with open ("data/test.txt","r",encoding="utf-8") as f:
#     print(f.read())

# #실습3 a모드로 기록 이어붙이기
# with open ("data/test.txt","a",encoding="utf-8") as f:
#     f.write ("\n이어쓰기")
    
# with open ("data/test.txt","r",encoding="utf-8") as f: 
#     print(f.read())

#실습4 csv.reader로 CSV읽기
# import csv
# with open('data/08_press.csv', 'r', encoding='utf-8') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)   # 각행이리스트로출력됨


# import csv
# with open('data/08_press.csv', 'w', encoding='utf-8', newline='') as f:
#     writer = csv.writer(f)
#     writer.writerow(['시각', '설비'])
#     writer.writerow(['09:00', 'PUMP-01'])

# #실습5 csv.writer로 CSV쓰기 
# import csv
# with open("data/08_press.csv", "w", encoding="utf-8")as f:
#     writer = csv.writer(f)
#     writer.writerow(["설비ID", "상태"])     # 헤더
#     writer.writerow(["PRESS-01", 1])
#     writer.writerow(["PRESS-02", 1])

# with open("data/08_press.csv", "r", encoding="utf-8") as f:
#     print(f.read())

#실습6 CSV 읽어 조건 저장하기
import csv
list= []
with open("data/08_press.csv", "r", encoding="utf-8")as f:
    reader = csv.reader(f)
    header = next(reader)  #next는 아직 안읽은 한 행을 꺼내는 것(첫줄 호출)
    print(header)    

    for row in reader:  #float 변환해서 전류값 기준 90초과 값만 새로운 리스트에 담기
        current = float(row[4])
        if current > 90 :
            list.append(row)

#조건에 맞는 데이터를 새 csv로 저장
with open("08_current_over90.csv","w",encoding="utf-8",newline="") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(list)

print("저장된 행 수:",len(list))
