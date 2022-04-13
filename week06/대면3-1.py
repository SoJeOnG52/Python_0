#from turtle import*
import turtle as t
t.color('blue')
for i in range(6):   # 반복문 사용
    t.circle(100)  # 반지름을 기준으로 원을 그림
    t.right(60)
t.done()

def draw_circle(n):
    n=360/ n
    for i in range(n):
        t.circle(100)
        t.left(n)
#draw_circle(12)