##전역, 지역변수
def fun1():
    x=100 #지역변수
    print('값1=',x)

def fun2():
    print('값2=',x)

x=200  #전역변수
#함수 호출
fun1()
fun2()