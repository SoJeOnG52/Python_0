##중첩 for문
#for i in range(5):
 #   for j in range(3):
  #      print("%d,%d" % (i,j))
   # print()    #줄바꿈
for i in range(2,10):
    for j in range(2,10):
        print("%d*%d=%d" % (i,j, i*j),end=" ")
    print()