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