##전역, 지역변수
def fun1():
    x=100 #지역변수
    print('값1=',x)

def fun2():
    print('값2=',x)
# 전역변수 호출 방법
#fun 밖에서 부르기
x=200
#함수 호출
fun1()
fun2()

#혹은 global 0 라고 선언하기
def func3():
    global a
    a=10
    print("%d 전역변수" % a)
func3()
