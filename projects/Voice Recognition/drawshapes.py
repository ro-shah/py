import turtle

class DrawShapes:
    def __init__(self, nofsides):
        self.length_of_side = 100
        self.number_of_sides = nofsides

    def setup(self):
        self.painter = turtle.Turtle()
        screen = turtle.Screen()
        screen.screensize(1000, 1000)
        self.drawShapes()

    def findAngle(self):
        self.total_angle = (self.number_of_sides - 2) * 180
        self.angle_turn = self.total_angle / self.number_of_sides
        self.angle_turn = 180 - self.angle_turn

    def clearScreen(self):
        turtle.clearscreen()

    def drawShapes(self):
        if self.number_of_sides != 0 and self.number_of_sides != 4.5:
            self.findAngle()
            for i in range(self.number_of_sides):
                self.painter.forward(self.length_of_side)
                self.painter.right(self.angle_turn)
        elif self.number_of_sides == 4.5:
            for i in range(2):
                self.painter.forward(self.length_of_side * 2)
                self.painter.right(90)
                self.painter.forward(self.length_of_side)
                self.painter.right(90)
        else:
            self.painter.circle(100)

        
