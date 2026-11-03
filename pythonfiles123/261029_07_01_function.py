#함수

def greet():
    print("점검을 시작합니다")
greet()   # 함수 이름 + 괄호 = 호출

#실습1 첫 함수 만들고 호출하기
def greet():
    print("점검을 시작합니다")
greet()
greet()  #두번호출하면 두번출력

#실습2 반복 코드를 함수로 정리하기
print("[모터]")
print("온도 확인 요망")
print("압력 확인 요망")
print("유량 점검 요망")
print("[펌프]")
print("온도 확인 요망")
print("압력 확인 요망")
print("유량 점검 요망")
def test ():
    print("온도 확인 요망")
    print("압력 확인 요망")
    print("유량 점검 요망")
print("[모터]")
test()
print("[펌프]")
test()

#실습4 함수로 설비점검 자동화하기
def cut ():     #구분선 출력하는 함수 정의
    print("-"*20)
def infor ():   #점검안내를 여러줄 출력하는 함수 정의
    print("온도를 점검하세요")
    print("유량을 점검하세요")
    print("압력을 점검하세요")
print("모터")  #설비마다 두함수호출(같은 안내)
infor()
cut()
print("펌프") 
infor()
cut()
print("밸브")
infor()
cut()
