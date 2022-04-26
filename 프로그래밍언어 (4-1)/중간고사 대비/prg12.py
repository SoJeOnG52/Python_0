# 일반함수 람다함수로 바꾸기
def avg(data):
    return sum(data)/len(data)

d=[20,15,18,20]  #리스트 형태
print(avg(d))
s1=tuple(map(str,d))
print(s1)

avg1=lambda data:sum(data)/len(data)
print(avg1(d))

mul= lambda n1, n2: n1*n2
print(mul(20,2))

avg= lambda n : sum(n)/len(n)
print("평균=", avg([50,30,25,45,55]))

data=[50,40,60,80,20]
print(list(map(str,data))) #문자열 리스트형태로 바꾸기
print(tuple(map(str,data)))