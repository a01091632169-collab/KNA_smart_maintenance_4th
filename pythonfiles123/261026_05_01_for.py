# #반복문

# #실습1 range로 숫자 흐름 출력하기
# N=int(input("숫자: "))
# for i in range(1, N+1):
#     print(i)

# for i in range(2, N+1, 2):
#     print(i)
# for i in range(5,0, -1):
#     print(i)

# # 평균 구하기
# total= 0
# count= 0
# for i in range(1,6):
#     total+=i5
#     count+=1
# if count >0:
#     print("평균:", total/count)

# #실습2 반복으로 1부터 N까지 합계 구하기
# N= int(input("숫자를 입력하세요: "))
# total=0
# for i in range(N+1):
#     total +=i 
# print ("합: ",total)

#실습3 중첩 반복으로 구구단 출력하기
# for dan in range(2,10): 
#     for num in range (1,10):
#         print(dan,"x",num,"=",dan*num,end=" ")
#     print ("\n-----")


for dan in range(2,10): 
     for num in range (1,10):
         print(f'{dan}x{num}={dan*num}')
     print ("-----")

#실습4 기준을 초과하는 값 세기
# count=0
# for num in range(5):
#     num= int(input("측정값? "))
#     if num > 80 :
#       count +=1
# print("(5회중", count,"개가 80초과)", "초과개수: ", count)


