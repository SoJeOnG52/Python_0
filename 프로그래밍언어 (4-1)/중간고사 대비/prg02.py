# for 문을 이용한 1-100까지의 합 계산
sum =0
for i in range(1,101,1):
    sum +=i
print("합은 %d" % sum)

# while문 변경
i= 1
sum= 0
while i <101:
    sum += i
    i+=1
print("합은 %d" % sum)

# for문을 이용한 구구단 계산
구구단 = int(input("수를 입력=>"))
for i in range(1,11,1):
    print("%d*%d=%d" %(구구단, i, 구구단*i))

# while문 변경
구구단 = int(input("수를 입력=>"))
i =0
while i<10:
    i+=1
    print("%d*%d=%d" % (구구단, i, 구구단 * i))

# for 문 (3-2)
for i in range(10):
    for j in range(i, 10):
        print("*", end="")
    print()

# while문 변경
i= 0
while i <10 :
    j =i
    while j <10:
        print("*", end="")
        j +=1
    print()
    i+=1





