import turtle

t = turtle.Turtle()
t.shape('turtle')
t.penup()
t.goto(0, 300)
t.rt(90)
t.pendown()
t.fd(600)
t.lt(90)
t.back(300)
t.fd(600)
t.penup()
t.goto(0, -300)
t.pendown()
t.color("blue")


def draw_f():
    for x in range(20):
        y = x ** 2 + 1
        t.goto(x, y - 300)  # 시작점을 0,-300으로 잡아서
    t.penup()
    t.goto(0, -300)
    t.pendown()

    for x in range(20):  # 반대방향 그리기
        y = x ** 2 + 1
        t.goto(-(x), y - 300)  # 시작점을 0,-300으로 잡아서,


draw_f()