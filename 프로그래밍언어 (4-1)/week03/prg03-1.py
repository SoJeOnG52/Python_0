hap=0
for i in range (101):
    hap +=i
    print(i, end=" ")
    if hap > 300 :  #합이 300이 넘으면 빠져나온다
        break
print(hap) #25까지 넣었을때 hap이 300을 넘었기 때문에 ("325") 더 이상 합을 멈추고 i는 25까지 합은 325가 출력된다.
print("합==>%d" % hap)  # 윗 줄처럼 하니까 어디까지가 합인지 헷갈려서 보기 쉽게 출력