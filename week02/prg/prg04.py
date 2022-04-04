num =int(input("점수=>"))
grade=''  #'' 문자 변수로 초기화 한 것
if num>= 90:
    grade='A'
else:
    if num >= 80:
        grade= 'B'
    else:
        if num>= 70:
            grade='C'
        else:
            grade='F'
print("당신의 점수 %d, 학점%c" % (num,grade))    