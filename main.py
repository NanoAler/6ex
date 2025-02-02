from turtle import *
k = 200
left(90)
tracer(0)
pendown()
begin_fill()
for i in range(12):
    right(90)
    fd(120*k)
    right(90)
    fd(14*k)
end_fill()
penup()

count = 0
canvas = getcanvas()
for x in range(-300,300):
    for y in range(-300,300):
        if canvas.find_overlapping(x*k, y*k, x*k, y*k) != ():
            count += 1

print(count)
done()
