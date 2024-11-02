# importing Required modules
# For More Projects Visit :
# Codewithcurious.com/projects
import turtle
import colorsys
# Create window to Display Pattern
t = turtle.Turtle()
s = turtle.Screen()
# Setting Background color
s.bgcolor("black")
# Speed of turtle to draw pattern
t.speed(8)
h = 200

# Loop for drawing Pattern
for i in range(80):
    c = colorsys.hsv_to_rgb(h,1,0.9)
    h+=1/h
    t.color(c)
    t.left(120)

for j in range(100):
    t.forward(200)
    t.left(230)
