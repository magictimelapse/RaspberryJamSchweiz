import serial
class SerialStepperControl(object):

    def __init__(self,port="/dev/ttyACM0"):
        self.ser = serial.Serial("/dev/ttyACM0",timeout=1.)
        self.flushBuffer()
        self.ser.close()
        self.ser = serial.Serial("/dev/ttyACM0")
        
    def flushBuffer(self):
        while self.ser.readline() != b'':
            pass

        
    def setSpeed(self, speed):
        command = "speed {0}\n".format(speed)
        self.ser.write(bytes(command,'utf-8'))
        return self.ser.readline()

    def step(self, steps):
        command = "step {0}\n".format(steps)
        self.ser.write(bytes(command,'utf-8'))
        return self.ser.readline()

    def torque(self, torque):
        command = "torque {0}\n".format(torque)
        self.ser.write(bytes(command,'utf-8'))
        return self.ser.readline()

    def stop(self):
        command = "stop\n"
        self.ser.write(bytes(command,'utf-8'))
        return self.ser.readline()

    def button(self):
        command = "button\n"
        self.ser.write(bytes(command,'utf-8'))
        ans =int(self.ser.readline())
        if ans == 0:
            return False
        else:
            return True
        
