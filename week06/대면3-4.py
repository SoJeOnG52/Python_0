import turtle as t
def draw_line():
    t.forward(100)
    t.backward(100)

t.color('red')
for i in range(50):
    draw_line()
    t.left(10)

t.done()