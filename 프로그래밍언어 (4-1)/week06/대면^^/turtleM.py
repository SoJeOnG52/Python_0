import turtle as t
def draw_square(size):
    for i in range(4):
        t.fd(size)
        t.left(90)
        size += 5

t.color('red')
for i in range(10,200,20):
    draw_square(i)

t.done()

def draw_line():
    t.forward(100)
    t.backward(100)

t.color('red')

for i in range(50):
    draw_line()
    t.left(10)

t.done()
