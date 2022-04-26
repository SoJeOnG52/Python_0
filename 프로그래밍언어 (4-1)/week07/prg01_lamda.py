# lamda 함수로 한줄로 함수를 간단하게 정의하기
mul= lambda n1, n2: n1*n2
print(mul(20,2))

#평균구하기
avg= lambda n : sum(n)/len(n)
print("평균=", avg([50,30,25,45,55]))

data=[50,40,60,80,20]
print(list(map(str,data))) #문자열 리스트형태로 바꾸기
print(tuple(map(str,data)))