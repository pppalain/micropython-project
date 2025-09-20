# micropython-project
small library for a single neopixel status LED
Originally written for RP2040 pi Zero on pin 16
statusled.py

usage:
    pin: Pin
        The pin number of the neopixel LED
    pixel_type: str
        There are three types of LEDs 'RGB' 'GRB' or 'RGBW' is not case sensitive.
ledobject=statusLed(pin,pixel_type)

import statusled.py
LED = statusLed(16,"GRB") # instanciate LED object
LED.green()	
LED.green(level=10)
LED.green(level=100)
LED.red()
LED.orange()
LED.blue()
LED.white()
LED.off()
LED.blanc
LED.rouge
LED.vert
LED.bleu
