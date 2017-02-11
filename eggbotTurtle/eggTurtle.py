import turtle
import math
import eggConfig
import eggBot

class EggTurtle(object):
    def __init__(self):
        self._turtle = turtle.Turtle()
        self._eggbot = eggBot.EggBot()
        self._eggbot.sendEnableMotors(eggConfig.STEP_SCALE)

    def __del__(self):
        self._eggbot.sendDisableMotors()

    @property
    def pendown(self):
        self._eggbot.sendPenDown(eggConfig.PENDOWNPOSITION)
        return self._turtle.pendown()

    @property
    def penup(self):
        self._eggbot.sendPenUp(eggConfig.PENUPPOSTION)
        return self._turtle.penup()

    def right(self, angle):
        return self._turtle.right(angle)

    def left(self, angle):
        return self._turtle.left(angle)

    def forward(self, distance):
        ### move the motors ##
        startX, startY = self._turtle.pos()
        self._turtle.forward(distance)
        endX, endY = self._turtle.pos()


    def backward(self, distance):
        startX, startY = self._turtle.pos()
        self._turtle.backward(distance)
        endX, endY = self._turtle.pos()


