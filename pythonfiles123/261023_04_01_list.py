#리스트 - 여러값을 담는 목록

#실습1 나만의 데이터 리스트 만들기
list1=[25,26,24,27,26]
print(list1)
print(len(list1))
list2=[]
print(len(list2))

#실습2 인덱스로 값 꺼내기
temp=[22,23,27,25,26,23]
print(temp[0])
print(temp[2])
print(temp[-1])

#실습3 인덱스로 꺼낸 값 계산하기
item=[100,222,333,150,200,122]
item1=item[0]
item2=item[5]
total=item1+item2
print(total)
print(total/2)

#실습4 슬라이싱으로 구간 자르기
temp=[22,24,27,23,34,25,26,28,30,21]
print(temp[0:3])
print(temp[-3:])
print(len(temp[0:3]))

#실습5 데이터를 두 구간으로 나누기
list=[3,4,5,6,5,4,6,7,8,7,5,3]
first=list[0:6]
print(first)
second=list[6:12]
print(second)
print(len(first))
print(len(second))

#실습6 값 찾아 바꾸기
templist=[25,26,240,28,27]
print(240 in templist)
print(templist.index(240))
templist[2]=24
print(templist)
print(240 in templist)

#실습7 측정값 추가하기 
lista=[]
lista.append(30)
print(lista)
lista.insert(0,28)
print(lista)
listb=[31,32]
lista.extend(listb)
print(lista)

#실습8 잘못된 값 제거하기
list=[25,26,24,999,28,26]
list.remove(999)
print(list)
print(list.pop(1))
del list[0]
print(list)

#실습9 정렬하고 탐색하기
templist=[22,28,39,24,24,26,27]
templist.sort()
print(templist)
templist.reverse()
print(templist)
print(templist.count(24))
print(templist.index(24))
