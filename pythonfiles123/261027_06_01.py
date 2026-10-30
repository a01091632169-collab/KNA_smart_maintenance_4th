#튜플 
# sensor = ("모터온도", 78) #센서이름과 값을 하나의 튜플로 묶기
# print(sensor)
# one=(78,)
# not_tuple=(78)

# tuple 인덱싱 : 번호로 튜플값 꺼내기
# sensor = ("모터온도", 78, "C")
# print(sensor[0])
# print(sensor[-1])

# sensors=[("모터온도", 78),("베어링진동", 0.5),]
# print(len(sensors))  #2

# sensor =("모터온도", 78, (3, 5))
# print(sensor[2][0])

# #실습1 센서를튜플로 묶고 꺼내기
# sensor = ("모터온도",78)
# print(sensor)
# print(sensor[0])
# print(sensor[1])
# name, value = sensor
# print(name, value)

# #실습2 튜플 리스트를 반복 처리하기
# sensors=(("모터온도",78),("회전속도",100),("펌프압력",95))
# for name, value in sensors:
#     print(name, value)
#     if value > 90 :
#         print(name, "warning")

# #실습3 중첩 튜플로 센서 위치 관리하기
# sensors=[("모터온도",78,(3,5)),("회전속도",100,(7,2)),("펌프압력",95,(4,8))]
# for name, value, pos in sensors:
#     x,y = pos
#     print(name, "위치: ", x,y )
#     if x <= 5 :
#         print(name)

# ids={"S01","S02", "S01"}
# print(ids)
# logs=["S01","S02","S01", "S03"]
# unique=set(logs)
# print(unique)

#실습4 셋으로 중복 센서 제거하기
sensors=["s02","s01","s03","s02","s03"]
sensor2 = set(sensors)   #리스트를 셋으로 감싸기
print(sensor2)
print(sorted(sensor2))
print("종류 수:" , len(sensor2))

#실습5 두 라인의 센서 구성 비교하기
sensor_a={"s01","s02","s03","s05"}
sensor_b={"s04","s03","s05"}
print(sensor_a.union(sensor_b))  #전체
print(sensor_a.intersection(sensor_b)) #교집합
print(sensor_a.difference(sensor_b))  #a-b
print(sensor_b.difference(sensor_a))  #b-a

#실습6 두 시점의 이벤트 센서 추적하기
day1={"s01","s02","s03"} #어제이슈
day2={"s02","s03","s05"} #오늘이슈
print("신규 이상:", day2.difference(day1)) #오늘 새로생긴 이슈
print("지속 이상:", day1.intersection(day2)) # 어제 오늘 지속된 이슈