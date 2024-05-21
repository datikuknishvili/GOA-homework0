from turtle import *


#home
speed(10)


width(8)
color("brown")

begin_fill()
color("purple")
forward(-300)
left(90)

back(300)
right(90)

forward(600)
left(90)

forward(300)
left(90)


end_fill()
begin_fill()

color("purple")

forward(600)

left(90)
forward(300)


left(90)
forward(250)

end_fill()

#door
begin_fill()
left(90)
color("blue")
forward(150)

right(90)
forward(100)

right(90)
forward(150)
end_fill()
#roof

penup()
goto(300,0)
pendown()

color("brown")
begin_fill()
left(240)
forward(350)

left(60)
forward(350)
end_fill()

#leftwindow
color("blue")
penup()
goto(-170,-50)
pendown()


begin_fill()
color("blue")
right(30)
forward(80)

left(90)
forward(80)

left(90)
forward(80)

left(90)
forward(80)

end_fill()

#rightwindow
penup()
goto(165,-50)
pendown()

begin_fill()
color("blue")

right(90)
forward(80)

right(90)
forward(80)

right(90)
forward(80)

right(90)
forward(80)

end_fill()

#garden
penup()
goto(-920,-310)
pendown()
begin_fill()
color("green")

right(90)
forward(1850)

right(90)
forward(180)

right(90)
forward(1850)

right(90)
forward(180)
end_fill()

#garage
penup()
goto(-840,-295)
pendown()

begin_fill()
color("grey")
forward(250)
right(90)
forward(300)
right(90)
forward(250)
right(90)
forward(300)
end_fill()
color("black")
right(90)
forward(50)
right(90)
forward(300)
left(90)
forward(50)
left(90)
forward(300)
right(90)
forward(50)
right(90)
forward(300)
left(90)
forward(50)
left(90)
forward(300)
right(90)
forward(50)
right(90)
forward(300)
right(90)
forward(250)
right(90)
forward(300)
right(90)
forward(250)


exitonclick()
