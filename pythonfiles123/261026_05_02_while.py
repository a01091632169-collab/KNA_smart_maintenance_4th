#while 반복문

#실습1 while로 목표값 도달까지 반복하기
# ans=7
# now=0
# while now != ans:
#     now=int(input("숫자를 입력하세요: "))
# print("정답입니다")

#실습2 플래그로 조건 만족 값 검색하기
found= False 
n= int(input("횟수: "))
for i in range(n):
    v= int(input("측정값: "))
    if v > 80:
        found = True
        break
if found == True:
    print("발견")
else :
    print("없음")


