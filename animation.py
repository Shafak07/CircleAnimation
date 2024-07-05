import turtle
turtle.bgcolor("DarkBlue")
turtle.pensize(2.5)
turtle.speed(0.5)
color = ["red","green","yellow","orange"]

for a in range(9):
    for i in color:
        turtle.color(i)
        turtle.circle(100)
        turtle.left(10)


turtle.mainloop()