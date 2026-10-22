#method_ 대문자/소문자 바꾸기, 점검하기, 공백/문자 제거하기, 메서드 이어붙이기

#실습1 대문자로 바꾸기
word = "ready"
print(word.upper())

#실습2 소문자로 바꾸기
word = "WARNING"
print(word.lower())

#실습3 단어 첫글자 대문자로 만들기
word = "kim chul soo"
print(word.title())                   #대소문자 변환

#실습4 대소문자 무시하고 비교하기
a= "fault"
b= "FAULT"
print (a==b)
print(a.lower()==b.lower())

#실습5 대문자인지 소문자인지 검사하기
print("ABC".isupper(), "ABC".islower())
print("abc".isupper(), "abc".islower())
print("Abc".isupper(), "Abc".islower())   

#실습6 파일명 규칙 한 번에 점검하기
a= "Sensor_LOG.CSV"
print(a.startswith("sensor"), a.endswith(".csv"))
a= a.lower()
print(a.startswith("sensor"), a.endswith(".csv"))   #점검(특정문자 들어있는지/대소문자)

#실습7  앞뒤 공백 제거하기
state=" 가동중 "
print('['+ state + ']')
state=state.strip()
print('['+ state + ']')

#실습8 한쪽 공백만 제거하기
state=" 대기 "
print('['+state+']')
state1=state.lstrip()
print('['+state1+']')
state2=state.rstrip()
print('['+state2+']')

#실습9 특정 문자 제거하기
word="***경고***"
print(word)
word=word.strip("*")
print(word)                           #공백/문자 제거

#실습10 메서드 이어붙이기
word=" WARNING "
print("["+word+"]")
word=word.strip().lower()
print("["+word+"]")

#실습11 결과를 변수에 다시 저장하기
word=" 경보 "
print("["+word+"]")
word=word.strip()
print("["+word+"]")                  #메서드 이어붙이기