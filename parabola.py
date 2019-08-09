import turtle as t

# minX 부터 maxX까지 step별로 포물선을 그림
# 포물선은 func으로 정의
def draw(minX,maxX,step,func):
    originalSpeed = t.speed()
    t.speed(0)
    t.up()
    t.goto(minX , func(minX))

    t.speed(originalSpeed)
    t.down()
    for x in range(minX,maxX+step, step):
        t.goto(x,func(x))

# 다항식을 반환하는 함수를 만들어 반환
def poly(a,b,c):
    def func(x):
            return a*x*x + b*x + c
    return func

# x범위를 -200부터 200까지로 하는 0.01x*2 -200 포물선을 1단위로 그리기
draw(-200,200,1,poly(0.01,0,-200))