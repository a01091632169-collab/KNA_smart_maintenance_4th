#기본값 인자
def report(name, value, unit="도"):
    print(name + ":"+ str(value) + unit)
report("압축기A", 75.3)  #압축기A:75.3도
report("펌프1", 7.2, "bar")  #펌프1:7.2bar

def grade(temp, limit=80):
    if temp > limit :
        return "점검필요"
    return "정상"
grade(95, limit=90)  # 키워드로 limit=90 → 기본값 80 대신 90 사용 

#실습1 기본값 인자 함수 만들기 
def sensor(temp, limit=80):
    if temp <= limit :
        print(temp, "정상")
    else:
        print(temp,"경고")
sensor(78)
sensor(95)
sensor(78, limit=50)

def sensor(temp, limit=80):
    if temp <= limit :
        return(temp,"정상")
    else:
        return(temp,"경고")
print(sensor(78))
print(sensor(95))
print(sensor(78, limit=50))
