
### write the training sample ###
import sys
import kuegelifarbe
kf = kuegelifarbe.KuegeliFarbe()
farbe = sys.argv[1]
with open(farbe,"a") as f:
    while True:
        rgb = kf.rgb()
        if rgb[0] != -1:
            output = "{0:.2f} {1:.2f} {2:.2f}\n".format(rgb[0],rgb[1],rgb[2]) 
            f.write(output)
