import turtle
import math
import eggConfig
class EggTurtle(object):
    def __init__(self):
        self._turtle = turtle.Turtle()
        self._eggbot = eggBot.EggBot()

    def pendown(self):
        
        return self._turtle.pendown()

    def penup(self):
        
        return self._turtle.penup()

    def right(self,angle):

        return self._turtle.right(angle)


    def left(self,angle):

        return self._turtle.left(angle)
    
    def forward(self, distance):
        ### move the motors ##
        heading = self._turtle.heading()
        headingRad = math.radians(heading)
        startX, startY = self._turtle.pos()
        self._turtle.forward(distance)
        endX, endY = self._turtle.pos()
        
    def backward(self,distance):
        
        return self._turtle.backward(distance)

    
