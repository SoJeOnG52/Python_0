tt=((1,2,3),
    (4,5,6),
    (7,8,9))
tt=list(tt)
for i in range(len(tt)):
    for j in range(len(tt[i])):
        print(tt[i][j], end=" ")
    print()