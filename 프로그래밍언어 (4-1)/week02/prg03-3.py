# 중첩 if문-elif 로 보다 간단하게 #
num=int(input("점수==>"))
grade=''   # 문자변수라고 초기화 시킨것
if num >= 90 :
    grade='A'
elif num >= 70 :
    grade = 'B'
elif num >= 70 :
    grade = 'C'
elif num >= 60:
    grade = 'D'
else:
    grade = 'F'

print("당신의 점수 %d, 학점 %c 입니다." %(num, grade))