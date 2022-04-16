#6번 (1851782 이소정)
myShop={"옷": 100,"컴퓨터":2000, "모니터":320}
#6번-(1)
for key in myShop.keys():
    print(key, "->", myShop.get(key))
#6번-(2)
print(myShop["컴퓨터"])  #컴퓨터 구매 가격
print(myShop.get("옷")) #옷 구매 가격
print(sum(myShop.values()))  #전체 구매 가격
#print(myShop)
#print(list(myShop.keys()))
#print(myShop.keys())
#print(myShop.values())
#myShop["폰"]= 400



