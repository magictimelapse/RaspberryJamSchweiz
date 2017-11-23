from time import sleep
from MLAnwenden import gibFarbe
while True:
    farbe = gibFarbe()
    if farbe == "rot":
        print ("Das war rot!")
    print (farbe)
    sleep(1)

