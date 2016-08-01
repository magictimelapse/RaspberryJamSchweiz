#3Python 2.7.9 (default, Mar  8 2015, 00:52:26) 
#[GCC 4.9.2] on linux2
#5Type "copyright", "credits" or "license()" for more information.
from sense_hat import SenseHat
sense = SenseHat()
farbe_gelb = [255,255,0]
farbe_rot = [255,0,0]
#sense.show_message('hello', scroll_speed=0.05, text_colour=farbe_gelb, back_colour=farbe_rot)
sense.show_letter("R",text_colour=[255,0,0])
