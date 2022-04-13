#
aa=[[30,40,20],         #aa[0] 에 해당
    [12,70,35,40],      #aa[1] 에 해당
    [25,33,70]]         #aa[2] 에 해당
for i in range(len(aa)) : #3행
    for j in range(len(aa[i])): #aa[0]- 열의 갯수 3열, aa[1]- 열의 갯수 4열
        print(aa[i][j], end=" ")  #aa[0][0],aa[0][1], aa[0][2]까지 출력하면 aa[1][0] 부터 다시 돌아
    print()

