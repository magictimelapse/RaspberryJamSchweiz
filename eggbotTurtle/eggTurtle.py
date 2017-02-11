import turtle
import math
import eggConfig
import eggBot

class EggTurtle(object):
    def __init__(self, simulation=True):
        self._turtle = turtle.Turtle()
        self._simulation = simulation
        if not self._simulation:
            self._eggbot = eggBot.EggBot()
            self._eggbot.sendEnableMotors(eggConfig.STEP_SCALE)

    def __del__(self):
        if not self._simulation:
            self._eggbot.sendDisableMotors()

    @property
    def pendown(self):
        if not self._simulation:
            self._eggbot.sendPenDown(eggConfig.LOWERINGPENDELAY)
        return self._turtle.pendown()

    @property
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
        startX, startY = self._turtle.pos()
        self._turtle.forward(distance)
        endX, endY = self._turtle.pos()
        if not self._simulation:
            self._eggbot.drawLine(startX,startY,endX,endY)

    def backward(self, distance):
        startX, startY = self._turtle.pos()
        self._turtle.backward(distance)
        endX, endY = self._turtle.pos()
        if not self._simulation:
            self._eggbot.drawLine(startX, startY, endX, endY)


def main():
    et = EggTurtle(simulation=True)
    rep = 12
    neck = 6
    for ii in range(rep):
        et.right(360/rep)
        for jj in range(neck):
            et.right(360/neck)
            et.forward(24)

if __name__ == "__main__":
    main()

