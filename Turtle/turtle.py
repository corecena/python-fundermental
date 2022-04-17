import turtle  


> import turtle
>>> s = turtle.getscreen()
>>> t= turtle.Turtle()
>>> t.fd(100)
>>> t.rt(90)
>>> t.fd(100)
>>> t.rt(90)
>>> t.fd(100)
>>> t.rt(90)
>>> t.fd(100)
>>> t.rl(90)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Turtle' object has no attribute 'rl'
>>> t.rt(90)
>>> t.fd(10000)
>>> t.goto(1000 1000)
  File "<stdin>", line 1
    t.goto(1000 1000)
                ^
SyntaxError: invalid syntax
>>> t.goto(1000 ,1000)
>>> t.rt(120)
>>> t.fd(6000)
>>> t.home()
>>> t.circle(60)
>>> t.dot(20)
>>> t.dot(60)
>>> turtle.bgcolor("green")
>>> turtle.bgcolor("blue")
>>> turtle.title("My first turtle")
>>> t.shapesize(12,67,56)
>>> t.shapesize(12,17,6)
>>> t.fillcolor("red")
>>> t.pencolor("cyan")
>>> t.color("pink", "yellow")
>>> t.begin_fill()
>>> t.fd(1000)
>>> t.bd(600)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Turtle' object has no attribute 'bd'
>>> t.lt(120)
>>> t.fd(1000)
>>> t.lt(120)
>>> t.fd(1000)
>>> t.end_fill()
>>> t.shape("circle")
>>> t.shape("turtle")
>>> t.shape("classic")
>>> t.shape("arrow")
>>> t.speed(2)