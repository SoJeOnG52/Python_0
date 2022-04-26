temp =[28,31,33,35,27,26,25]
hap=0
imin=imax=temp[0]
for i in temp:  #여기서 range 쓰려면 범위가 있어야하는데 temp가 범위 그자체임으로 temp를 써준다
    print(i,end=" ")
    hap+=i #hap=hap+i
    if imax<i :
        imax=i
    if imin>i:
        imin=i
print("합=%d, 최댓값=%d, 최솟값=%d" %(hap, imax, imin))
print("평균=%5.2f"%(hap/len(temp))) #합 나누기 문자열의 문자갯수 = 평균