# from turtle import *
# t = Turtle()
# t.hideturtle()
# t.pensize(1)
# t.screen.bgcolor('black')
# t.pencolor('orange')
# t.speed(9)
# for i in range(5,700,3):
#     t.fd(i)
#     t.left(90)
# t.screen.exitonclick()
# t.screen.mainloop()

# from turtle import *
# t = Turtle()
# t.hideturtle()
# t.pensize(1)
# t.screen.bgcolor('black')
# t.pencolor('green yellow')
# colors=['yellow','red','green','blue']
# t.speed(0)
# for i in range(3,200):
#    t.pencolor(colors[i%4])
#    t.circle(i)
#    t.left(91)
# t.screen.exitonclick()
# t.screen.mainloop()

from turtle import *

t = Turtle()
t.hideturtle()
t.pensize(1)
t.screen.bgcolor('black')
t.pencolor('green yellow')

t.speed(9)
t.up()
t.goto(0, -150)
t.down()
a = 200
t.circle(a)
n=19
for i in range(n):
    n -=1
    if n % 2 != 0:
        t.pencolor('green yellow')
    else:
        t.pencolor('blue3')
    t.up()
    t.left(90)
    t.fd(10)
    t.down()

    t.right(90)
    a -= 10
    t.circle(a)

t.screen.exitonclick()
t.screen.mainloop()
