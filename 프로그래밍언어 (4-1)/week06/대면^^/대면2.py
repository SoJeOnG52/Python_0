# week06 함수와 모듈 (1851782 이소정) #
#재귀함수 - 자기 자신을 호출하는 함수

def factorial(n):
    if n==1:
        return n
    else:
        return n*factorial(n-1)
print(factorial(5))
