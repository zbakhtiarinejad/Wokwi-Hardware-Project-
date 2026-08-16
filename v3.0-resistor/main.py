from machine import Pin
from utime import sleep

sleep(0.01) 
print("Hello, Pi Pico!")

led1 = Pin(5, Pin.OUT)
led2 = Pin(4, Pin.OUT)

button = Pin(14, Pin.IN, Pin.PULL_DOWN)
print("system is ready!press the button...")

while True:
    if button.value() == 1:
        led1.on()
        led2.on()
    else:
        led1.off()
        led2.off()

    sleep(0.05)
