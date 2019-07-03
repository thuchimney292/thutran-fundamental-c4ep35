def is_inside(position,rect):
    x,y=position
    x0,y0,w,h=rect
    if x0<=x<=x0+w and y0<=y<=y0+h:
        return True
    else:
        return False
print(is_inside([200,120],[140,60,100,200]))