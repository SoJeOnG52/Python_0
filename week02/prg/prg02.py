##연산자 연습 프로그램 (1851782, 이소정) ###
num1= int(input("data1=> "))
num2= int(input("data2=> "))
print("%d+ %d= %10d" %(num1,num2,num1+num2)) #
print("%d-%d= %d" %(num1,num2,num1-num2))
print("%d** %d= %10d" %(num1,num2,num1**num2))  # 승수 구하기
print("%d>%d/ %d" %(num1,num2,num1/num2))
print("%d// %d= %10d" %(num1,num2,num1//num2)) # 몫 구하기
print("%d>%d= %d" %(num1,num2,num1>num2))  # 대입연산자
print("%d!=%d= %d" %(num1,num2,num1!=num2))
print("%d>=%d= %d" %(num1,num2,num1>=num2))
print("%d>>%d= %d" %(num1,num2,num1>>num2))
print(num1>= 10 and num2!=100)