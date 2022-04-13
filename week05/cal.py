#
def fact(n):   #함수 정의 과정 n-->매개변수
    fact=1
    for i in range(1,n+1):
        fact+=i
    return fact

#print("20!=",fact(20))
f = fact(20)   #20-->argument, 인자
print("20!=",f)