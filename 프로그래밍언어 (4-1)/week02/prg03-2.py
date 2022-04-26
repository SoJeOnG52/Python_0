# 중첩 if문 #
num=int(input("점수==>"))
grade=''   # 문자변수라고 초기화 시킨것
if num >= 90 :
    grade='A'
else :
    if num >= 80 :
        grade= 'B'
    else :
        if num >= 70 :
            grade = 'C'
        else:
            if num >= 60:
                grade = 'D'
            else:
               grade = 'F'
print("당신의 점수 %d, 학점 %c" %(num, grade))




