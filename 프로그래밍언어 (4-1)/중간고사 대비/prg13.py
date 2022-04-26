#딕셔너리 key, value 값
myShop={"옷": 100,"컴퓨터":2000, "모니터":320}
for key in myShop.keys():
    print(key,"->",myShop.get(key))