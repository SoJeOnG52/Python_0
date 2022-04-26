## 1851782 이소정
for i in range (10):
    for j in range(i,10):
        print("*", end=" ")
    print()
# while문 변경
i= 0    # 초기값=> (0,10,1) 에서 0을 뜻함
while i<10 :  # 최곳값=> (0,10,1) 에서 10을 뜻함
    j=i
    while j<10:
        print("*",end=" ")
        j += 1   # 증가값=> (0,10,1) 에서 1을 뜻함
    print()
    i += 1





