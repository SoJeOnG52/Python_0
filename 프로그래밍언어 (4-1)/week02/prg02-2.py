##연산자 연습 프로그램(1851782, 이소정)##
num1 = int(input("data1=>"))
num2 = int(input("data2=>"))
print("%d + %d = %10d" % (num1, num2, num1 + num2)) #산술연산자
print("%d ** %d = %10d" % (num1, num2, num1 ** num2))
print("%d + %d = %10d" % (num1, num2, num1 + num2))
print("%d // %d = %10d" % (num1, num2, num1 // num2))
print("%d > %d = %10d" % (num1, num2, num1 > num2)) #비교연산자 #num1 > num2 비교했을때 맞으면 T=1, 틀리면 F=0
print(num1>=10 and num2!=100) #비교와 논리연산자 (연산 순서 나타나있음)

