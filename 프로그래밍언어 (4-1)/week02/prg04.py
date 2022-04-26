# 반복문(for) #
#for i in range(10): # 0부터 시작 10 전 까지 끝, 1칸 씩 증가
    #print(i, end = " ") #end = " ": 옆으로 출력되는 방법
for i in range(0,10,2): #1부터 시작, 10 전까지 끝, 2칸씩 증가
        print(i, end=" ")
for _ in range(5) : # 제어변수가 없다면 그냥 언더바(_) 사용가능
    print("경영정보학과")

#1-100까지 합을 계산#
sum = 0  #변수 초기화 기능
#for i in range(2, 101, 2):   #짝수의 합을 구하려면
for i in range(1,101,1):
    sum+=i     #sum+=i-> sum= sum+i 둘이 더한 값을 sum에 반복적으로 넣음
print("합은 %d" % sum)

# while문 변경
i= 1
sum= 0
while i <101:
    sum += i
    i+=1
print("합은 %d" % sum)

# su 에 입력한 숫자의 구구단 #
su= int(input("수를 입력="))
for i in range(2,10,1) :
    print("%d * %d= %d" % (su, i , su*i))

for i in [0,1,2]:
    print("안녕?66^^")

