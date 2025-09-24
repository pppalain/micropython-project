"""MIT license
Copyright 2025 Alain Pelletier

This library is written for a DC motor using the LM298 or the DRV8871

usage:
>>>from dcmotor import DCMotor
>>>mymotor = DCMotor(1,0) #pass in pwm pins in this case 1 and 0
>>>mymotor.direction(1,0,30000)  #  clockwise (depends on wiring) pwm = 30000/65535  - mode = 0
>>>mymotor.direction(0,0,30000)  #  counterclockwise (depends on wiring) pwm = 30000/65535 - mode = 0
>>>mymotor.run(0,-3000) #  run motor ccw at power 3000/65535
>>>mymotor.run(0,4000) # run motor cw at power 4000/65535
>>>mymotor.activeBreak() # actively breake motor
>>>mymotor.coast() # stop power to motor but coast instead of breaking.

"""

from machine import PWM

class DCMotor:
    """DC motor 
        
    Attributes
    ----------
    pin: pwm0, pwm1
        The pin number motor driver
    """
    
    def __init__(self,pwm0,pwm1):
        self.p0 = PWM(pwm0, freq=20000)
        self.p1 = PWM(pwm1, freq=20000)
        
    def direction(self,direction,mode,power):
        """turn motor in a direction with a power
        
        
        parameters
        ----------
        mode: 0 - pwm pin is active high which means that pwm 0% makes both pins low
              1 - pwm pin is active low which means that pwm at 0% both pins high
        power: valid values are 0x0 to 0xffff -> 0 to 100% duty cycle 
        direction: 1 or 0 for clockwise / counterclockwise
        """
        if mode: direction ^= 1 	# toggle direction if mode 1 is selected
        mode = 0xffff * mode
        if mode: power = 0xffff-power

        if direction :
            self.p0.duty_u16(power)
            self.p1.duty_u16(mode)
        else:
            self.p0.duty_u16(mode)
            self.p1.duty_u16(power)

    def run(self, mode, power):
        """run motor
        same as direction but takes the looks at the sign of the power to determine
        cw or ccw

        parameters
        ----------
        mode: 0 - pwm pin is active high which means that pwm 0% makes both pins low
              1 - pwm pin is active low which means that pwm at 0% both pins high
        power: valid values are -0xffff to 0xffff -> -100% to 100% duty cycle 
        """
        
        if power < 0:
            self.direction(0,mode,int(abs(power)))
        else:
            self.direction(1,mode,int(abs(power)))
    
    def activeBreak(self):
        """puts motor in active breaking mode
        LM298 actively breaks if both pins are equal
        DRV8871 actively breaks if both input pins are high
        """
        self.p0.duty_u16(65535)
        self.p1.duty_u16(65535)

    def coast(self):
        """puts motor in coast mode
        DRV8871 coasts if both pins are low
        function is not valid for LM298 actively breaks if both pins are equal, enable would have to be toggled
        """
        self.p0.duty_u16(0)
        self.p1.duty_u16(0)
        