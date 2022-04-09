'''
Setup Requires a Button
Lower leg connected to Pin 37 - 3.3v
Upper leg connected to Pin 1 - GP0
'''

import machine

LED = machine.Pin(25, machine.Pin.OUT) # set PIN 25 as an output pin. This is the onboard LED
Button = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_DOWN) # set PIN 0 as an input pin. Note the use of PULL_DOWN to read it as off when the circuit is open

while True:
    LED.value(Button.value()) # the LED remains off when the button isn't pressed. 