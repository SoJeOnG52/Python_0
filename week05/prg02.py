def div(a=1, b=2):
    return a/b
print('div()=',div())
print('div(4)=',div(4))
print('div(6,3)=',div(6,3))

def multipy(x,y=1):
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

