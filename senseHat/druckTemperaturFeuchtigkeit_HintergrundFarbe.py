from sense_hat import SenseHat
sense = SenseHat()

while True:
        t = sense.get_temperature()
        p = sense.get_pressure()
        h = sense.get_humidity()
        
        t = round(t, 1)
        p = round(p, 1)
        h = round(h, 1)

        if t < 20 and t < 26.7:
            hintergrundFarbe = [255,0,0]
        else:
            hintergrundFarbe = [0,255,0]

        msg = "Temperature = %s, Pressure=%s, Humidity=%s" % (t, p, h)
        sense.show_message(msg, scroll_speed=0.05, back_colour=hintergrundFarbe)
