#최대공약수 구하는 방법
def gcd(a,b) :
    if a < b:    #b보다 a가 커야하므로 b보다 a가 더 크면
        a, b = b, a #a,b를 바꿔라
    while b !=0:
        n= a % b
        if n ==0:
            break
        else:
            a=b
            b=n
    return b

print(gcd(20,72))

#최대공배수
def lcm(a,b):

    return a*b //gcd(a,b)