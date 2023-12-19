import turtle

wn = turtle.Screen()
wn.bgcolor("light blue")
pen1 = turtle.Turtle()
pen1.color("blue")
pen2 = turtle.Turtle()
pen2.color("red")
pen2.left(30)
pen3 = turtle.Turtle()
pen3.color("green")
pen3.left(90)

def sqrfunc(size):
    for i in range(10):
        pen1.fd(size)
        pen1.left(40)
        pen2.fd(size)
        pen2.right(40)
        pen3.fd(size)
        pen3.right(40)
        size = size + 1

size = 6
for i in range(20):
    sqrfunc(size)
    size += 10

wn.mainloop()