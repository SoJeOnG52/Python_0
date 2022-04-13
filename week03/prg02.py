#while문
sum=0  # 파이썬은 변수의 형태 선언 안해도 되지만, 이렇게 써주면 sum은 정수형이라고 선언해주는 것과 같음
for i in range(2,11,2):
    print(i, end=" ")
    sum +=i
print("\n 합 = %d" % sum)
print("=================while문===============")
sum=0
i=2
while i<11:
    print(i, end=" ")
    sum +=i
    i +=2
print("\n 합=%d" %sum)  #위 조건에서 벗어나면 이거 실행