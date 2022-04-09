import machine
import utime

LED = machine.Pin(25, machine.Pin.OUT)

while True:
    LED.toggle()
    utime.sleep_ms(500)