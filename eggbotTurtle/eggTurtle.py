#!/usr/bin/env python
import turtle
import math
import eggConfig
import eggBot

class EggTurtle(object):
    factor = 10
    def __init__(self, simulation=True):
        self._turtle = turtle.Turtle()
        self._simulation = simulation
        if not self._simulation:
            self._eggbot = eggBot.EggBot()
            self._eggbot.sendEnableMotors(eggConfig.STEP_SCALE)

    def __del__(self):
        if not self._simulation:
            self._eggbot.sendDisableMotors()


    def pendown(self):
        if not self._simulation:
            self._eggbot.sendPenDown(eggConfig.LOWERINGPENDELAY)
        return self._turtle.pendown()


    def penup(self):
        if not self._simulation:
            self._eggbot.sendPenUp(eggConfig.RAISINGPENDELAY)
        return self._turtle.penup()

    def right(self, angle):
        return self._turtle.right(angle)

    def left(self, angle):
        return self._turtle.left(angle)

    def forward(self, distance):
        ### move the motors ##
        startX, startY = self.factor * self._turtle.pos()
        self._turtle.forward(distance)
        endX, endY = self.factor * self._turtle.pos()
        if not self._simulation:
            self._eggbot.drawLine(startX,startY,endX,endY)

    def backward(self, distance):
        startX, startY = self.factor * self._turtle.pos()
        self._turtle.backward(distance)
        endX, endY = self.factor * self._turtle.pos()
        if not self._simulation:
            self._eggbot.drawLine(startX, startY, endX, endY)


def main():
    et1 = EggTurtle(simulation=True)
    factor = et1.factor
    ### first draw a rectangle showing the drawing canvas ##
    MAXX = eggConfig.MAXX
    MAXY = eggConfig.MAXY
    et1.penup()
    et1.forward(eggConfig.MAXX/2/factor)
    et1.right(90)
    et1.pendown()
    et1.forward(eggConfig.MAXY/factor/2)
    et1.right(90)
    et1.forward(eggConfig.MAXX/factor)
    et1.right(90)
    et1.forward(eggConfig.MAXY/factor)
    et1.right(90)
    et1.forward(eggConfig.MAXX / factor)
    et1.right(90)
    et1.forward(eggConfig.MAXY/2 / factor)
    ## draw drawing rectangle
    et = EggTurtle(simulation=False)
    et.pendown()
    rep = 100
    neck = 10
    et.penup()
    et.left(90)
    et.forward(10)
    et.right(90)
    et.pendown()
    for ii in range(rep):
        #et.left(360/neck)
        et.forward(5)
        #et.right(360/neck)
        #et.right(360/rep)
        for jj in range(neck):
            et.right(360/neck)
            et.forward(9)
        #et.right(180)
        #et.forward(6)
        #et.right(180)
    et.penup()
if __name__ == "__main__":
    main()

