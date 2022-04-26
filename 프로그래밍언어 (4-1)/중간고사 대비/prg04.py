#4-4 두수를 입력받아 최대공약수를 구하는 프로그램을 작성하라(유클리드)
a= int(input("큰 수를 입력=>"))
b= int(input("작은 수를 입력=>"))

while b!=0:
    n=a%b
    if n==0:
        break
    else:
        a=b
        b=n
print("최대공약수는 %d 입니다."%b)

#5-5 최대공약수를 구하는 함수를 작성하고, 호출하는 프로그램 작성하라(유클리드)
def gcd(a,b) :
    if a<b:
        a,b =b,a
    while b!= 0:
        n= a%b
        if n ==0:
            break
        else:
            a = b
            b = n
    return b
print("최대공약수는 %d 입니다."% gcd(6,2))


