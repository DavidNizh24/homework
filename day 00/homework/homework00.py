from turtle import * 





width(7)

#drowing square

color("purple")     
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drowing a door

forward(70)
color("yellow")
begin_fill()
left(90)
forward(100)
right(90) 
forward(60)
right(90)
forward(100)
end_fill()
# door is done

penup()
goto(200, 200)
pendown()

#drowing roof

color("orange")
begin_fill()
left(90)
forward(30)
left(130)
forward(200)
left(99)
forward(200)
left(130)
forward(30)
end_fill()

#roof is done

penup()

right(90)
forward(50)
left(90)
forward(20)

pendown()

# 1st window

color("brown")
begin_fill()
forward(45)
right(90)
forward(45)
right(90)
forward(45)
right(90)
forward(45)
end_fill()

penup()
goto(200, 200)

# 2nd window

left(180)
forward(50)
right(90)
forward(20)

pendown()
begin_fill()
forward(45)
left(90)
forward(45)
left(90)
forward(45) 
left(90) 
forward(45)   
end_fill()

#done

exitonclick()