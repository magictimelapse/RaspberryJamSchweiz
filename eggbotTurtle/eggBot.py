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

    def __command(self,cmd):
	if (self._port is not None) and (cmd is not None):
		try:
			self._port.write( cmd )
			response = self._port.readline()
			if ( response != 'OK\r\n' ):
				if ( response != '' ):
					print( 'After command ' + cmd + ',' )
					print( 'Received bad response from EBB: ' + str( response ) + '.' )
				else:
					print( gettext.gettext( 'EBB Serial Timeout.') )
		except:
			pass 

    def query( self, cmd ):
            if (self.__port is not None) and (cmd is not None):
                    response = ''
                    try:
                            self.__port.write( cmd )
                            response = self.__port.readline()
                            unused_response = self.__port.readline() #read in extra blank/OK line
                    except:
                            print( gettext.gettext( "Error reading serial data." ) )
                    return response
            else:
                    return None


    def doTimedPause( self, nPause ):
            if (self._port is not None):
                    while ( nPause > 0 ):
                            if ( nPause > 750 ):
                                    td = int( 750 )
                            else:
                                    td = nPause
                                    if ( td < 1 ):
                                            td = int( 1 ) # don't allow zero-time moves
                            self.__command( 'SM,' + str( td ) + ',0,0\r')		
                            nPause -= td


    def sendEnableMotors( self, Res ):
            if (Res < 0):
                    Res = 0
            if (Res > 5):
                    Res = 5	
            if (self._port is not None):
                    self.__command(  'EM,' + str(Res) + ',' + str(Res) + '\r' )
                    # If Res == 0, -> Motor disabled
                    # If Res == 1, -> 16X microstepping
                    # If Res == 2, -> 8X microstepping
                    # If Res == 3, -> 4X microstepping
                    # If Res == 4, -> 2X microstepping
                    # If Res == 5, -> No microstepping

    def sendDisableMotors( self):
            if (self._port is not None):
                    self.__command(  'EM,0,0\r')	

    def QueryPRGButton( self ):
            if (self._port is not None):
                    return self.query(  'QB\r' )

    def TogglePen( self ):
            if (self._port is not None):
                    self.__command(  'TP\r')		

    def sendPenUp( self, PenDelay ):
            if (self._port is not None):
                    self.__command(  'SP,1\r')		
                    if (PenDelay > 0):
                            self.doTimedPause( PenDelay)

    def sendPenDown( self, PenDelay ):
            if (self._port is not None):
                    self.__command(  'SP,0\r')	
                    if (PenDelay > 0):
                            self.doTimedPause( PenDelay)	
