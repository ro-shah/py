import turtle

# creating class to draw shapes using turtle
class Painter:
    # constructor
    def __init__(self, number_of_sides, side_length = None, side_width = None, radius = None, color = None):
        self.NumberOfSides = number_of_sides
        self.SideLength = side_length
        self.SideWidth = side_width
        self.Radius = radius
        self.Color = color
        self.drawer = turtle.Turtle()
        self.screen = turtle.Screen()

        # turtle setup
        self.drawer.hideturtle()
        self.drawer.speed(0)

    # function to find angle to turn to draw shape (uses math equation)
    def findAngle(self):
        self.TotalAngle = (self.NumberOfSides - 2) * 180
        self.Angle = self.TotalAngle / self.NumberOfSides
        self.Angle = 180 - self.Angle

    # function to draw regular polygon except for rectangles
    def polygon(self):
        self.findAngle() # calls fucntion which gives the angle needed to turn
        self.drawer.begin_fill()
        self.drawer.color(self.Color)
        for i in range(self.NumberOfSides): # finds shape using number of sides
            self.drawer.forward(self.SideLength) # length from input
            self.drawer.right(self.Angle) # angle from function
        self.drawer.end_fill()

    # function to draw circles
    def drawCircle(self):
        self.drawer.color(self.Color)
        self.drawer.begin_fill()
        self.drawer.circle(radius = self.Radius) # uses radius from input
        self.drawer.end_fill()
    
    # function to draw rectangles
    def rectangle(self):
        self.drawer.color(self.Color)
        self.drawer.begin_fill()
        for i in range(2):
            self.drawer.forward(self.SideLength) # uses length from input
            self.drawer.right(90)
            self.drawer.forward(self.SideWidth) # uses width from input
            self.drawer.right(90)
        self.drawer.end_fill()

# input to determine shape
nofsides = int(input("Enter number of sides to determine shape: "))
colorOfShape = input("What color would you like the shape to be?: ")

# if/else condition using shapes to call specific function & ask the specific inputs
if nofsides == 0:
    radius = int(input("Enter raduis of circle: ")) # radius for circle
    shape = Painter(number_of_sides = nofsides, radius = radius, color = colorOfShape) # adding info to class
    shape.drawCircle() # calling circle function
elif nofsides >= 3:
    if nofsides == 4:
        rectangle_or_square = input("Rectangle or Square?: ") # input when user types 4 sides
        if rectangle_or_square.capitalize() == "Square":
            sidelength = int(input("Enter length of sides: ")) # length for square
            shape = Painter(number_of_sides = nofsides, side_length = sidelength, color = colorOfShape) # adding info to class
            shape.polygon() # function called to draw sqaures
        elif rectangle_or_square.capitalize() == "Rectangle":
            sidewidth = int(input("Enter width of rectangle: ")) # width for rectangle
            sidelength = int(input("Enter length of rectangle: ")) # length for rectangle
            shape = Painter(side_length = sidelength, side_width = sidewidth, color = colorOfShape) # adding info to class
            shape.rectangle() # function to draw rectangle
    else:
        sidelength = int(input("Enter length of sides: ")) # length for polygon
        shape = Painter(number_of_sides = nofsides, side_length = sidelength, color = colorOfShape) # adding info to class
        shape.polygon() # function to draw polygon

turtle.done()