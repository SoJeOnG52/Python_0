## 1851782 이소정
temp=[28, 31,33,35,27,26,25]
hap=0
imax=imin=temp[0]
for data in temp:
    #print(data,end="")
    hap+=data
    if imax<data:
        imax=data  # 최댓값 구해주는 로직
    if imin >data :
        imin=data
print("합=%d, 최댓값= %d, 최솟값=%d" %(hap,imax,imin))
print("평균=%7.2f"% (hap/len(temp)))  # len(temp) ==> 문자열의 문자 갯수를 숫자값으로 출력

