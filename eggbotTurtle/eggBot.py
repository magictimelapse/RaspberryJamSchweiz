import serial
import gettext
import eggConfig
import math
class EggBot(object):
    

    def __init__(self):
        self._port = self.__openPort()
        self.__ServoSetup()
        self.__penisup = False

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
            # type: (object, object) -> object
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

    def __ServoSetup( self ):
        print "hello"
        # Pen position units range from 0% to 100%, which correspond to
        # a timing range of 6000 - 30000 in units of 1/(12 MHz).
        # 1% corresponds to 20 us, or 240 units of 1/(12 MHz).

        intTemp = 240 * ( eggConfig.PENUPPOSTION + 25 )
        self.__command( 'SC,4,' + str( intTemp ) + '\r' )

        intTemp = 240 * ( eggConfig.PENDOWNPOSITION + 25 )
        self.__command(  'SC,5,' + str( intTemp ) + '\r'  )

        # Servo speed units are in units of %/second, referring to the
        # percentages above.  The EBB takes speeds in units of 1/(12 MHz) steps
        # per 21 ms.  Scaling as above, 1% in 1 second corresponds to
        # 240 steps/s, which corresponds to 0.240 steps/ms, which corresponds
        # to 5.04 steps/21 ms.  Rounding this to 5 steps/21 ms is correct
        # to within 1 %.

        intTemp = 5 * eggConfig.SERVOUPSPEED
        self.__command(  'SC,11,' + str( intTemp ) + '\r' )
        intTemp = 5 * eggConfig.SERVODOWNSPEED
        self.__command(  'SC,12,' + str( intTemp ) + '\r' )


    def __doTimedPause(self, nPause):
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
            self.__penisup = not self.__penisup
            if (self._port is not None):
                    self.__command(  'TP\r')		

    def sendPenUp( self, PenDelay ):
            self.__penisup = True
            if (self._port is not None):
                    self.__command(  'SP,1\r')		
                    if (PenDelay > 0):
                            self.__doTimedPause( PenDelay)

    def sendPenDown( self, PenDelay ):
            self.__penisup = False
            if (self._port is not None):
                    self.__command(  'SP,0\r')	
                    if (PenDelay > 0):
                            self.__doTimedPause( PenDelay)



    def drawLine(self, startX, startY, stopX, stopY):
        nDeltaX = stopX - startX
        nDeltaY = stopY - startY
        if self.__penisup:
            fspeed = eggConfig.PENUPSPEED
        else:
            fspeed = eggConfig.PENDDOWNSPEED

        nTime = int( math.ceil( 1000 / fspeed * math.sqrt(nDeltaX*nDeltaX + nDeltaY*nDeltaY) ) )
        while ( ( abs( nDeltaX ) > 0 ) or ( abs( nDeltaY ) > 0 ) ):
				if ( nTime > 750 ):
					xd = int( round( ( 750.0 * nDeltaX ) / nTime ) )
					yd = int( round( ( 750.0 * nDeltaY ) / nTime ) )
					td = int( 750 )
				else:
					xd = nDeltaX
					yd = nDeltaY
					td = nTime
					if ( td < 1 ):
						td = 1		# don't allow zero-time moves.
				yd2 = -yd
				xd2 = xd
				strOutput = ','.join( ['SM', str( td ), str( yd2 ), str( xd2 )] ) + '\r'
				self.__command( strOutput )
				nDeltaX -= xd
				nDeltaY -= yd
				nTime -= td