from week06.num import cal as c

print(c.hap(80,70,90,20))
print(c.fact(20))


from num.cal import fact, hap  #함수 호출  cal->쓰는게 가독성이 높다
print(hap(80,70,90,20))
print(fact(20))
#print(multiply(4,5))  #호출하지않은 함수는 사용되지 않음


from num.cal import *  #함수 호출
from week06.num.gcd_m import *
print((hap(80,70,90,20)),(fact(20)),(multiply(4,5)))

print(gcd(72,18))
print(lcm(10,12))

