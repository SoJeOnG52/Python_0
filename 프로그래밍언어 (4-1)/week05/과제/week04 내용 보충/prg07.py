#7번 (1851782 이소정)
#스타벅스에서 판매 중인 메뉴
starbucks={"아메리카노":2000,"카페라떼":2500,"자몽허니블랙티":3500,"블랙티레모네이드":3500,"돌체라떼":3000}
print(starbucks)

#1. 오늘 주문 가능한 메뉴를 출력하라 ex)
print("<오늘 주문 가능한 메뉴>")
for key in starbucks.keys():
    print(key)
print("---^^---")
#2. 메뉴에 알맞는 가격을 알려주어라 ex) 00의 가격은 00입니다.
while(True):
    menu = input(str(list(starbucks.keys())) + "중 가격이 궁금한 메뉴를 입력하세요-->")
    if menu in starbucks:
        print("<%s>의 가격은 <%s>입니다." % (menu, starbucks.get(menu)))
    elif menu == "주문할게요":
        print("주문 감사합니다")
        break
    else:
        print("재입력바랍니다.")

#전체 음료의 가격을 출력하라
print("전체 음료의 가격은", sum(starbucks.values()))

#가장 비싼 음료의 가격을 출력하라
print("가장 비싼 음료의 가격은",max(starbucks.values()))
