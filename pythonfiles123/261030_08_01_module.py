# import math
# result = math.sqrt(16)
# print(result)

#실습1 import 세 방식으로 모듈 가져오기
# import math
# result = math.sqrt(16)
# print(result)

# from math import sqrt
# result2= sqrt(16)
# print(result2)

# import math as abc
# result3 = abc.sqrt(16)
# print(result3)

#실습2 표준 라이브러리로 센서값 만들기
# import random
# num1= random.randint(1,100)
# print(num1)

# import math
# num2 = math.sqrt(num1)
# print(num2)

import os
cwd = os.getcwd()
print(cwd)  #C:\Users\chang\OneDrive\바탕 화면\posco_AI_\pythonfiles123 #현재폴더절대경로

import os
files = os.listdir("data")
for name in files:
    print(name)

path = os.path.join("data","08_press.csv")
if os.path.exists(path):
    print("파일있음",path)

#실습3 os로 폴더 목록 살펴보기
import os
cwd = os.getcwd()
print("<현재경로>", cwd)

print("<폴더 안 목록>")
files= os.listdir("data")
for file in files :
    print(file)

print("<.csv 파일만>")
for file in files:
    if file.lower().endswith(".csv"):
        print(file)


#실습4 os로 파일 존재 확인하기
import os
path_08press= os.path.join("data","08_press.csv")
if os.path.exists(path_08press):
    print("True, 파일있음")
else :
    print("False, 파일없음")

print(path_08press)

#실습5 datetime으로 점검 기록 남기기
import os
import datetime
num_file = len(os.listdir("data"))
now_time= datetime.datetime.now()
print(f'파일 {num_file} 개, 점검시각 {now_time}')

#실습6  폴더에서 csv 파일만 골라내기
import os
folder_list = os.listdir("data")
csv_list=[]

for file_name in folder_list:
    if file_name.endswith(".csv"):
        csv_list.append(file_name)

print("[CSV]")
for files in csv_list:
    path = os.path.join("data",files)
    print("-",path)