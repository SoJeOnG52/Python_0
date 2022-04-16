import turtle as t
def draw_circle(n):
    n=360/ n
    for i in range(n):
        t.circle(100)
        t.left(n)

def draw_square(size):
    for i in range(4):
        t.fd(size)
        t.left(90)
        size += 5

 def draw_line():
    t.forward(100)
    t.backward(100)
