import machine
import utime

LED = machine.Pin(26, machine.Pin.OUT)

while True:
    LED.toggle()
    utime.sleep_ms(500)