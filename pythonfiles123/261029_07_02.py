#매개변수와 반환값

# def check(name):
#     print(name + " 점검을 시작합니다")
# check("압축기A")

# #실습1 매개변수 1개 함수 만들기
# def check(name):     #매개 변수가 name인 함수 만들고
#     print(name, "점검 시작")   #함수 내용
# check("압축기A")    #함수호출에 인자 입력
# check("펌프1")      #인자 입력2

#실습2 다중 매개변수로 센서값 계산하기
def check(name, temp):
    print(name+ str(temp)+ "도")
check("모터", 78)
check("펌프", 92)

# def report(name, temp):
#     print(name + ": " + str(temp))
# report(name="압축기A", temp=75.3)
# report(temp=75.3, name="압축기A")

#실습3 키워드 인자로 함수 호출하기
def check2 (name, temp):
    print(name, temp)

check2(temp=78, name="모터")
check2(temp=92, name="펌프")

# def add(a,b)
#    return a + b
# total = add(3, 4)     #이런식으로 반환값을 변수에 담아서 활용
# print(total)

#실습4 반환값으로 간단 계산기 만들기
def cal (a,b):
    return a+b
total = cal(80.0,5.0) #반환값 이용 변수
print(total)    #반환값출력
print(total +5)  #반환값변수로 재사용
  
def min_max(values):
    return min(values), max(values)
result = min_max([75.3, 88.0, 49.1])
print(result)

#실습5 센서 통계 함수 만들기
def sensorlist(values):
    return min(values), max(values), sum(values)/len(values)
result=sensorlist([78, 92, 85])
print(result)
