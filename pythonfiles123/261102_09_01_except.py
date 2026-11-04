# #try-except구조
# try:
#     temp = int("스물")
# except ValueError:
#     print("ValueError")

# try:
#     result = 10/0
# except: 
#     print("ZeroDivisionError")

# try:
#     print(undefined_var)
# except:
#     print("프로그램 계속")

#실습2 try-except로 오류 넘기기
try:
    temp = int(input("온도: "))
    print("온도는", temp)
except ValueError:
    print("숫자를 입력하세요")
print("프로그램 계속")

#여러 except코드
# try:
#     n = int(row[3])  (칸이 2개뿐일 때)   
# except ValueError:
#     print("숫자 아님")
# except IndexError:
#     print("칸 부족")

#실습3 구체적 예외로 입력 검증하기
try:
    value = int(input("측정값: "))
    print(int(100/value))
except ValueError:
    print("숫자 형식이 아님니다")
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다") 