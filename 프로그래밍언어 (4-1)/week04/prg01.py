#리스트의 기본
mylist=[30,10,20]
print("현재 리스트 :%s"% mylist)  # %s-> 문자열

mylist.append(40)  #맨뒤에 항목 추가
print("append(40)후의 리스트:%s"% mylist)

print("pop()으로 추출한 값 : %s" %mylist.pop()) #리스트 맨뒤의 항목을 뺀다(해당 항목 삭제)
print("pop()후의 리스트: %s" % mylist)

mylist.sort() #리스트 정렬 sorted(리스트)는 리스트는 그대로 두고, 정렬된 결과만 반환
print("sort()후의 리스트: %s" % mylist)

mylist.reverse()  #순서를 역순으로
print("reverse()후의 리스트 :%s" % mylist)

print("20값의 위치: %d" %mylist.index(20))

mylist.insert(2,222)
print("insert(2,222)후의 리스트 :%s" % mylist)  #지정된 위치에 값 삽입
