# 대입연산자#
## 변수 선언 부분#
money, c500, c100, c50, c10 = 0, 0, 0, 0, 0

#main code section
money= int (input("교환할 돈을 입력=>"))

c500 = money//500 #c500에 몫을 넣고
money %= 500      # money에 나머지 넣어라

c100 = money //100
money %= 100

c50 = money// 50
money %= 50

c10 = money// 10
money %= 10

print("500원짜리=> %d" % c500)
print("100원짜리=> %d" % c100)
print("50원짜리=> %d" % c50)
print("10원짜리=> %d" % c10)
print("잔돈은=> %d" % money)
