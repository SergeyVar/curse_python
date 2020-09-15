# #Созаёт пунктирную линию
# def dot_lines(a,b):
#     for i in range(b):
#         t.fd(a)
#         t.up()
#         t.fd(a)
#         t.down()##
# # Создаёт круг пунктирной линией
# def dot_circle(a,b):
#     for i in range(36):
#         t.circle(a,b)
#         t.up()
#         t.circle(a,b)
#         t.down()
# from turtle import *
# t = Turtle()
# #t.hideturtle()
# t.pensize(1)
#
# t.speed(0)
# for i in range(4):
#     dot_lines(10,10)
#     t.left(90)
# t.left(45)
# dot_lines(10,14)
# t.up()
# t.home()
# t.fd(100)
# t.down()
# dot_circle(100,5)
# t.screen.exitonclick()
# t.screen.mainloop()

from turtle import *
t = Turtle()
t.getscreen().bgcolor('black')
t.hideturtle()
#t.pensize(1)
t.speed(0)
r=0
g=10
col=['red','yellow','orange']
while True:
    for i in range(100):
        t.pencolor(col[i%3])
        r +=0.3+g//200
        t.circle(r,g)
        t.pensize(0)
t.screen.exitonclick()
t.screen.mainloop()
