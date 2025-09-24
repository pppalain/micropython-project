# micropython-project

Status LED
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

DCMotor Small library for a DC motor using the LM287 or DRV8871
usage:
from dcmotor import DCMotor
mymotor = DCMotor(1,0) #pass in pwm pins in this case 1 and 0
mymotor.direction(1,0,30000)  #  clockwise (depends on wiring) pwm = 30000/65535  - mode = 0
mymotor.direction(0,0,30000)  #  counterclockwise (depends on wiring) pwm = 30000/65535 - mode = 0
mymotor.run(0,-3000) #  run motor ccw at power 3000/65535
mymotor.run(0,4000) # run motor cw at power 4000/65535
mymotor.activeBreak() # actively breake motor
mymotor.coast() # stop power to motor but coast instead of breaking.
