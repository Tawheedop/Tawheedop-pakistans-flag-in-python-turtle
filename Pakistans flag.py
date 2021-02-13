from turtle import*
title('Pak flag by RT')

'''NOTE:- some words not may be in your dictionary they may show warning with lines below them'''

pensize(1)
penup()
fillcolor('#01411c')  # green color
goto(-300, 150)
pendown()

# green part of flag

begin_fill()
forward(500)
rt(90)
forward(300)
rt(90)
forward(500)
rt(90)
forward(300)
rt(90)
end_fill()

# white part of flag

fillcolor('#ffffff')   # white color
begin_fill()
forward(120)
rt(90)
pencolor('white')
forward(300)

pencolor('black')
rt(90)
forward(120)
rt(90)
forward(300)
end_fill()
penup()

rt(90)
forward(120)
rt(90)
forward(300)

# moving to centre

goto(0, 0)
fd(100)
pendown()
lt(90)
pencolor('#ffffff')
fillcolor('#ffffff')    # moon_color
begin_fill()
circle(100, 360)        # moon
end_fill()

# new circle to make half moon

penup()
fd(120)
lt(90)
fd(120)
pendown()

pencolor('#01411c')
fillcolor('#01411c')
begin_fill()
circle(90, 360)
end_fill()

# making star

pencolor('#ffffff')
penup()

lt(90)
fd(20)
pendown()

fillcolor('#ffffff')
begin_fill()

for i in range(5):
    fd(100)
    rt(144)

end_fill()


# fill the gap between the star with white color

speed(10)
fd(50)
rt(90)
fd(15)
dot(42)
penup()
rt(180)
fd(250)
pendown()
pencolor('black')
hideturtle()

write('Tawheed', font=("Ani", 30, 'bold'))

mainloop()
