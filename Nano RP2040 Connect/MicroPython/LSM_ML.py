'''
IMU's are typically used to capture movement data of a device or a system. The onboard IMU of
the Nano RP2040 Connect, the LSM6DSOX from STMicroelectronics®, has an embedded hardware processing
engine dedicated to real-time machine learning computing; this means that some machine learning
algorithms were moved from the application processor to the LSM6DSOX directly. STMicroelectronics
named this embedded processing engine of the LSM6DSOX Machine Learning Core (MLC).

In the MLC, machine learning processing is implemented through a decision-tree logic. A decision
tree is a mathematical tool composed of a series of configurable nodes; each node is characterized
by an "if-then-else" condition where an input signal (represented by statistical parameters
calculated from the sensor data) is evaluated against a certain threshold. The decision tree results
can be read from the application processor at any time and there is also the possibility to generate
an interrupt for every change in the result in the decision tree.

For the vibration monitoring application, the LSM6DSOX accelerometer is configured with ±4g full
scale and a 26 Hz output data rate; any sensor orientation is allowed.

For the vibration monitoring application, just one feature has been used (peak-to-peak) and applied
to the accelerometer norm squared input. The MLC runs at 26 Hz, computing features on windows of
16 samples (more or less, every 0.6 seconds). One decision tree with just two nodes has been
configured to detect the different classes; an interrupt (pulsed and active high) is generated
every time a new vibration type is detected.
'''

import time
from lsm6dsox import LSM6DSOX
from machine import Pin, I2C

INT_MODE = True # enable interrupts
INT_FLAG = False # no pending interrupts

# interrupt handler
def imu_int_handler(pin):
    global INT_FLAG # access the variable defined in the global scope
    INT_FLAG = True # signal an interrupt was received

# external interrupt configuration
if (INT_MODE == True):
    int_pin = Pin(24)
    int_pin.irq(handler = imu_int_handler, trigger = Pin.IRQ_RISING)

# initialize I2C
i2c = I2C(0, scl=Pin(13), sda=Pin(12))

# model definition
UCF_FILE = "lsm6dsox_vibration_monitoring.ucf"
UCF_LABELS = {0: "no vibration", 1: "low vibration", 2: "high vibration"}

# initialize IMU
lsm = LSM6DSOX(i2c,
    gyro_odr = 26,
    accel_odr = 26,
    gyro_scale = 2000,
    accel_scale = 4,
    ucf = UCF_FILE)

print("\n--------------------------------")
print("- Vibration Monitoring Example -")
print("--------------------------------\n")
print("- MLC configured...\n")

while(True):
    if (INT_MODE):
        if (INT_FLAG):
            # interrupt detected
            INT_FLAG = False # clear the flag
            print("\n- ", UCF_LABELS[lsm.read_mlc_output()[0]])
    else:
        buf = lsm.read_mlc_output()
        if (buf != None):
            print(UCF_LABELS[buf[0]])
