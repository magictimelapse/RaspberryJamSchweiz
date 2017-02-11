import serial
import gettext


class EggBot(object):
    def __init__(self):
        self._port = self.__openPort()

    def __findPort(self):
        # Find a single EiBotBoard connected to a USB port.
        try:
            from serial.tools.list_ports import comports
        except ImportError:
            comports = None
            return None
        if comports:
            comPortsList = list(comports())
            EBBport = None
            for port in comPortsList:
                # if port[1].startswith("EiBotBoard"):
                if port[1].startswith("Arduino Leonardo"):
                    EBBport = port[0]  # Success; EBB found by name match.
                    break  # stop searching-- we are done.
            if EBBport is None:
                for port in comPortsList:
                    if port[2].startswith("USB VID:PID=04D8:FD92"):
                        EBBport = port[0]  # Success; EBB found by VID/PID match.
                        break  # stop searching-- we are done.
            return EBBport

    def __testPort(self,comPort):
        '''
            Return a SerialPort object
            for the first port with an EBB (EiBotBoard; EggBot controller board).
            YOU are responsible for closing this serial port!
            '''
		assert isinstance(comPort, object)
		if comPort is not None:
            try:
                serialPort = serial.Serial(comPort, timeout=1.0)  # 1 second timeout!
                serialPort.write('v\r')
                strVersion = serialPort.readline()
                if strVersion and strVersion.startswith('EBB'):
                    return serialPort

                serialPort.write('v\r')
                strVersion = serialPort.readline()
                if strVersion and strVersion.startswith('EBB'):
                    return serialPort
                serialPort.close()
            except serial.SerialException:
                pass
            return None
        else:
            return None

    def __openPort(self):
        foundPort = self.__findPort()
        serialPort = self.__testPort(foundPort)
        if serialPort:
            return serialPort
        return None

    def __command(self, cmd):
        if (self._port is not None) and (cmd is not None):
            try:
                self._port.write(cmd)
                response = self._port.readline()
                if (response != 'OK\r\n'):
                    if (response != ''):
                        print('After command ' + cmd + ',')
                        print('Received bad response from EBB: ' + str(response) + '.')
                    else:
                        print(gettext.gettext('EBB Serial Timeout.'))
            except:
                pass
