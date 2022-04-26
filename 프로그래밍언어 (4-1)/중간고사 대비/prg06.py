#없애라
alist=[10,20,30,40,50,60]
del(alist[0:3])
print(alist)

# 추가
alist=[10,20,30,40,50,60]
alist[1:4]=[44,55,66]
print(alist)

#각 원소에 *3
alist=[1,2,3,4,5]
blist=[3*x for x in alist]
print(blist)

Mylist=[30,10,20]
print("현재리스트:%s" % Mylist)
#뒤에 추가
Mylist.append(40)
print("append 후 %s" %Mylist)
#원하는 위치에 추가
Mylist.insert(2,40)
print("insert 후 %s" %Mylist)
#원하는 값 삭제
Mylist.remove(40)
print("remove 후 %s" %Mylist)
#원하는 위치 삭제
del(Mylist[2])
print("del 후 %s" %Mylist)
#리스트 길이
len(Mylist)
print("len 후 %s" % len(Mylist))
#리스트 복사
Mylist2=Mylist.copy()
print("Mylist.copy()후의 %s" % Mylist2)
