# sensors={"모터온도:":78, "진동":0.5}
# print(sensors)
# print(type(sensors))
# empty={}

# sensors = {"모터온도": 78, "진동": 0.5} 
# print(sensors["모터온도"]) 
# print(sensors["진동"])

# sensors = {"모터온도": 78} 
# sensors["펌프압력"] = 95
# sensors["유량"] = 42
# print(sensors)
# sensors["모터온도"] = 80
# del sensors["펌프압력"]

# sensors = {"모터온도": 78} 
# print(sensors.get("모터온도")) 
# print(sensors.get("유량")) 
# print(sensors.get("유량", 0))

# sensors = {"모터온도": 78, "펌프압력": 95} 
# print("모터온도" in sensors)    #True
# print(78 in sensors)    #False
# if "유량" in sensors: 
#   print(sensors.get("유량"))

# sensors = {"모터온도": 78, "압력": 95} 
# print(list(sensors.keys())) 
# print(list(sensors.values())) 
# avg = sum(sensors.values()) / len(sensors)
# print(avg)

# sensors = {"모터온도": 78, "진동": 0.5} 
# for name, value in sensors.items():
#   print(name, "측정값:", value)

values= {"모터온도":95, "압력":88}
limits={"모터온도":90, "압력":90}
for name, value in values.items():  #item으로 키와값을 반복해서 뽑고, 
    if value > limits[name]:  #딕셔너리[키]로 원하는 값을 뽑음
       print(name,"warning")  

sensors = {"모터온도": 78, "진동": 0.5} 
new_data= {"모터온도": 80, "유량": 42} 
sensors.update(new_data) 
print(sensors)

names = ["모터온도", "진동", "압력"] 
values = [78, 0.5, 95] 
sensors = dict(zip(names, values)) 
print(sensors)

sensors = {"모터온도": [78,79,80]}
temps = sensors["모터온도"]
print(sum(temps)/len(temps))
print(max(temps))

plant = { 
"1번모터": {"온도": 78, "상태": "정상"}, 
"2번펌프": {"압력": 95, "상태": "경고"}, } 
print(plant["2번펌프"]["압력"])

#실습1 딕셔너리 만들고 다루기
sensors={"모터온도":78, "진동":0.5 } #센서명과 측정값 = 키와 값 딕셔너리 저장
print(sensors["모터온도"])     #키로 값 꺼내기
sensors["모터온도"]=80       #기존 키 수정
sensors["압력"]=95          # 새 키 추가
print(sensors)           
print(sensors.get("유량",0))    #없는 키 기본값0으로 조회 
print("모터온도" in sensors)   # in 으로 키 존재 확인

#실습2 update로 여러 값 한 번에 갱신하기
sensors={"모터온도":78, "진동":0.5 } 
new={"압력": 95}
print(sensors)
sensors.update(new)
print(sensors)
del sensors["진동"]
print("센서 수:", len(sensors))

#실습3 딕셔너리로 통계 내기
sensors={'모터온도': 78, '진동': 0.5, '압력': 95}
avg=sum(sensors.values())/len(sensors)
print("평균:",avg)
for name , value in sensors.items():
    top=""  #최댓값 키
    max= 0  #최댓값 값
    if value>max:
        max=value
        top=name
print("최댓값 센서:",top,max)

#실습4 zip으로 센서명-값 매핑하기
sensors=["모터온도","진동","압력"]
values=[78,0.5,95]
sensors=dict(zip(sensors,values))
print(sensors)
for name, value in sensors.items():
  print(name, value)

#실습5 임계값으로 경고 센서 분류하기
values = {'모터온도': 78, '진동': 0.5, '압력': 95}
limits= {"모터온도": 75, '진동': 1.0, '압력': 100}
warning=[]
for name, value in values.items():  
   if value > limits[name]:  #name이란거에 모터온도, 진동, 압력이 저장되는거라서 limit에서 모터온도를 검색해도 똑같이 name으로 인식
      warning.append(name)
print("경고센서: ", warning)

#실습6 중첩 딕셔너리로 설비 관리하기
plant={"1번모터":{"온도":78, "상태":"정상"},"2번펌프":{"압력":95, "상태":"경고"}}
print(plant["2번펌프"]["압력"])
for name, infor in plant.items():
   if infor["상태"] == "경고" :
      print(name, "점검 필요")

#실습7 표 데이터를 딕셔너리로 변환하기
rows = ["온도,78", "압력,95", "진동,0.5"]
sensors = { }
for row in rows:   #튜플은 값을 바로 나눠받지만 리스트는 아님
    name, value = row.split(",") #리스트 안의 문자열을 row에 받고 쉼표기준 나눔
    sensors[name]=float(value)
print(sensors) 

#실습8 센서 데이터 통합 정리
sensors = {'모터온도': 78, '진동': 0.5, '압력': 95}
limits= {"모터온도": 75, '진동': 1.0, '압력': 100}
warning=set()
avg=sum(sensors.values())/len(sensors) 
print(avg)

for name, value in sensors.items():   #item 순회
   if sensors[name] > limits[name]:    #초과한 값 찾기
      warning.add(name)                #초과한 값 셋에추가
print("위험 센서:", sorted(warning))   #셋 출력