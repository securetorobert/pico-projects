'''
This code is handy for detecting any I2C devices connected to your board.
I2C uses only two wires, so it's easy to know what pins they are connected to

The Inter-Integrated Circuit (I2C) Protocol is a protocol intended to allow multiple
"peripheral" digital integrated circuits ("chips") to communicate with one or more "controller" chips.
Like the Serial Peripheral Interface (SPI), it is only intended for short distance
communications within a single device. Like Asynchronous Serial Interfaces (such as RS-232 or UARTs),
it only requires two signal wires to exchange information.
'''
import machine

sda = machine.Pin(4) # serial data pin
scl = machine.Pin(1) # serial clock pin
freq = 400000 # 400kHz. could also be 100kHz
channel = 0 # 0 or 1 depending on the pins in use. Please use the Pico pinout diagram to determine the right channel

i2c = machine.I2C(channel, sda=sda, scl=scl, freq=freq)

print('Scanning I2C bus ...')
devices = i2c.scan()

if len(devices) == 0:
    print('No I2C devices found')
else:
    print('{} I2C device(s) found'.format(len(devices)))
    
    for d in devices:
        print('Decimal address: {}, Hex address: {}'.format(d, hex(d)))
