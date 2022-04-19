# 이 폴더가 하나의 모듈이 된다

def fact(n):   #함수 정의 과정 n-->매개변수
    fact=1
    for i in range(1,n+1):
        fact+=i
    return fact

def multiply(x,y=1):
    return x*y

def hap(*p):  #전달인자가 다양하거나 너무 많을때 사용
    h=0
    for data in p :
        h+=data
    return h
#result = hap(90,100,200,10,90)
#print("결과=",result)
#result = hap(90,100,200,10,90,30,50,70,20)
#print("결과=",result)

#print("20!=",fact(20))
#f = fact(20)   #20-->argument, 인자
#print("20!=",f)