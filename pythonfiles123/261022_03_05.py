#치환 분리 결합
#replace
print("정 상 가 동".replace(" ",""))
print("010-1234-5678".replace("-",""))
print("3,000".replace(",",""))


#실습1 단어바꾸기
word = "설비 정상 가동"
print(word)
word=word.replace("정상","점검")
print(word)

#실습2 공백 기준으로 나누기
word="PUMP A 03"
word= word.split(" ")
print (word)

#실습3 쉼표 기준으로 나누기
word="a,b,c,d"
print(word.split(","))

#실습4 나누는 횟수 제한하기
word="a,b,c,d"
print(word.split(",",1))

#실습5 리스트 합치기
split_data = ["2025","01","15"] 
print( "-".join(split_data)) 

#실습6 sep으로 이어 출력하기
print("2025","01","15",sep="-") 
print("2025","01","15",sep=",") 

#실습7 구분자 통째로 바꾸기
date="2025/10/15"
print(date)
date= date.split("/")
print(date)
date= '-'.join(date)
print(date)

#실습8
text="1,NORMAL,25.3"
text2=text.split(",")
text3=text2[1].strip().lower()
print(text3)


