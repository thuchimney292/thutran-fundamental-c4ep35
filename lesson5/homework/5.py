from turtle import *
def draw_star(x,y,length):
    penup()
    setpos(x,y)
    pendown()
    left(72)
    for i in range(5):
        forward(length)
        right(144)
draw_star(100,100,100)
mainloop()