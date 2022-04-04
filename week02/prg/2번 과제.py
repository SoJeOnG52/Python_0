## 중첩if문 (1851782 이소정)
num =int(input("점수=>"))
grade=''                        #'' 문자 변수로 초기화 한 것
if num>= 90:
    grade='A'
elif num >= 80:
     grade= 'B'
elif num>= 70:
    grade='C'
else:
    grade='F'
print("당신의 점수 %d, 학점%c" % (num,grade))