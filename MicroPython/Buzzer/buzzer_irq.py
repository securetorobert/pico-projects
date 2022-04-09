'''
This requires two buttons and a piezo buzzer

ButtonA - GP0 and Pin 36 - 3.3V
ButtonB - GP1 and Pin 36 - 3.3V
Buzzer - GP15 and GND
'''

import machine

# set up two digital inputs for buttons
ButtonA = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_DOWN)
ButtonB = machine.Pin(1, machine.Pin.IN, machine.Pin.PULL_DOWN)

# set up a PWM output
Buzzer = machine.PWM(machine.Pin(15))
Buzzer.duty_u16(32767) # 50% duty cycle = 32767/65535
Frequency = 1000 # 1kHz

def ButtonIRQHandler(pin):
    global Frequency # access the variable from the global scope
    
    if pin == ButtonA:
        if Frequency < 2000:
            Frequency += 50
    elif pin == ButtonB:
        if Frequency > 100:
            Frequency -= 50

# set up the IRQ and hook it up to the handler
ButtonA.irq(trigger = machine.Pin.IRQ_RISING, handler = ButtonIRQHandler)
ButtonB.irq(trigger = machine.Pin.IRQ_RISING, handler = ButtonIRQHandler)

while True:
    Buzzer.freq(Frequency)
