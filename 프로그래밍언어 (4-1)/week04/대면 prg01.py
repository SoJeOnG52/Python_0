#4-1확장형 데이터
sum2=0
data=list(map(int,input("데이터 입력==>").split(" "))) #split(" ")- 나누기 자르기
print(data)

avg= sum (data)/len(data)
for val in data:
    sum2 += (val - avg) ** 2 #**- 제곱
print("평균:%5.3f, 합계: %5d" % (avg,sum(data)))
print("최댓값:%d,최솟값:%d,범위:%d"%(max(data), min(data),max(data)-min(data)))
print("분산 : %10.4f"% (sum2/len(data)))
