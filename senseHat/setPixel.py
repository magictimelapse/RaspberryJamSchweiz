from sense_hat import SenseHat
sense = SenseHat()
sense.clear()
farbe_rot = [255,0,0]
farbe_blau = [0,0,255]
farbe_gruen = [0,255,0]
sense.set_pixel(1,2,farbe_rot)
sense.set_pixel(6,4,farbe_gruen)
sense.set_pixel(2,5,farbe_blau)
