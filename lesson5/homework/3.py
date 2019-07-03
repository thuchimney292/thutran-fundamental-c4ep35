from turtle import *
def draw_square(length,_color):
    color(_color)
    for i in range(4):
        forward(length)
        left(90)
length = int(input('Enter the length of square = '))
_color = str(input('Enter the color of square = '))
draw_square(length,_color)
mainloop()