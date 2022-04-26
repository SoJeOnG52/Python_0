#break, continue ##
i = 0; sum = 0
while i < 10:
    i += 1        #여기 있어야지 continue 아래에 있으면 i가 변화가 없으니 계속 반복된다.
    if i%2 != 0:  #2로 나누어서 나머지는 0 -> 짝수라는 말 / 홀수 경우에는 != (=같지않다) 하면됨
        continue  #짝수는 위로 올라감
    sum+=i        # continue에서 걸리지 않는건 홀수이기 때문에 홀수의 합이 구해진다.
print(sum)
hap=0
for i in range (101):
    hap +=i
    print(i, end=" ")
    if hap > 300 :  #합이 300이 넘으면 빠져나온다
        break
print(hap)
