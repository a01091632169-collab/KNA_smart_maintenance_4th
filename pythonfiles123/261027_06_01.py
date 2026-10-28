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

#실습2 튜플 리스트를 반복 처리하기
sensors=(("모터온도",78),("회전속도",100),("펌프압력",95))
for name, value in sensors:
    print(name, value)
    if value > 90 :
        print(name, "warning")

#실습3 중첩 튜플로 센서 위치 관리하기
sensors=[("모터온도",78,(3,5)),("회전속도",100,(7,2)),("펌프압력",95,(4,8))]
for name, value, pos in sensors:
    x,y = pos
    print(name, "위치: ", x,y )
    if x <= 5 :
        print(name)