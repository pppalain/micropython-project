"""MIT license
Copyright 2025 Alain Pelletier
Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the “Software”),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the Software
is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE
OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

This library is written for a single neopixel status LED
it was originally written for the PICO zero on pin 16

usage:
LED = statusLed(16,"GRB") # instanciate LED object
LED.green()	
LED.green(level=10)
LED.green(level=100)
LED.red()
LED.orange()
LED.blue()
LED.white()
LED.off()
"""

from machine import Pin
import neopixel
import utime

class statusLed:
    """A single neopixel status indicator
        
    Attributes
    ----------
    pin: Pin
        The pin number of the neopixel LED
    pixel_type: str
        There are three types of LEDs 'RGB' 'GRB' or 'RGBW' is not case sensitive.
    """

    def __init__(self, pin, pixel_type = "RGB"):
        """
        Parameters
        ----------
        self.G: int
            position of the G in the color tuple
        self.R: int
            position of the R in the color tuple
        self.pixel: neopixel
            object neopixel
        """
        
        w = 0
        pixel_type = pixel_type.lower()
        self.G=0
        self.R=0
        if pixel_type.startswith("grb"):
            self.R = 1
        elif pixel_type.startswith('rgb'):
            self.G = 1
            if pixel_type.endswith('w'):
                w = 1
        self.pixel = neopixel.NeoPixel(Pin(pin),1,bpp = 3+w)
           
        self.pixel[0]=(0,0,0)
        self.pixel.write()
        
    
    def red(self, level = 100):
        """ Displays red status
        
        Parameters
        ----------
        level: int, optional
            The brightness level (default is 100)
        """
        
        color = [0,0,0]  # create a list for the color tuple in order to change it later
        color[self.R] = level # change list member 
        self.pixel[0]=(tuple(color))
        self.pixel.write()
        
    def rouge(self,level=100):
        self.green(level)

    def green(self, level = 100):
        """ Displays green status
        
        Parameters
        ----------
        level: int, optional
            The brightness level (default is 100)
        """

        color = [0,0,0]  # create a list for the color tuple in order to change it later
        color[self.G] = level # change list member 
        self.pixel[0]=(tuple(color))
        self.pixel.write()

    def vert(self,level=100):
        self.green(level)

    def blue(self, level = 100):
        """ Displays blue status
        
        Parameters
        ----------
        level: int, optional
            The brightness level (default is 100)
        """

        self.pixel[0]=(0,0,level)
        self.pixel.write()
        
    def bleu(self,level=100):
        self.blue(level)

    def orange(self, level = 50):
        """ Displays orange status
        
        Parameters
        ----------
        level: int, optional
            The brightness level (default is 50)
        """

        self.pixel[0]=(level,level,0)
        self.pixel.write()

    def off(self):
        """ turns off status LED
        """

        self.pixel[0]=(0,0,0)
        self.pixel.write()
    
        
    def white(self,level = 33):
        """ Displays white status
        
        Parameters
        ----------
        level: int, optional
            The brightness level (default is 30)
        """

        self.pixel[0]=(level, level, level)
        self.pixel.write()
        
    def blanc(self,level = 33):
        self.white(level)


LED = statusLed(16,"GRB") # instanciate LED object

LED.blanc(level=100)


    