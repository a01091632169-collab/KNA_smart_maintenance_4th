#문자열 연결(+),반복(*)
#len()-글자 수
#print(len("PYTHON"))

#실습1 길이재기
phone ="01012345678"
print(len(phone))

#실습2 포함 확인하기
print("정상" in "설비 고장 발생", "고장" in "설비 고장 발생")

#실습3 개수 세기
print('sensor-01-temp'.count("-"))

#실습4 위치 찾기
print("temp_2024".find("_"), "temp_2024".find("a"))

#실습5 시작과 끝 확인하기
word = "sensor_log.csv"
print(word.startswith("sensor"), word.endswith("csv"))

#실습6 대소문자 구별하기
word = "WARNING"
print("WARNING"==word, "warning"==word)