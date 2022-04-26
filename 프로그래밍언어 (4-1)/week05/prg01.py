#def multiply (a,b):
def multiply(a, b=1):  #디폴트값 지정, 디폴트 값은 앞에 적을 수 없음
    return a*b
#print(multiply(20,3))
print(multiply(100))  #인자를 한개만 했을때--> 'b'에 해당하는 전달인자가 없어서 안됨.
