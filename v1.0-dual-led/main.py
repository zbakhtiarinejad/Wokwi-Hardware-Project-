from machine import Pin
from utime import sleep

sleep(0.01) 
print("Hello, Pi Pico!")

# Define LEDs
led1 = Pin(5, Pin.OUT)
led2 = Pin(4, Pin.OUT)

while True:
    led1.toggle()
    led2.toggle()
    sleep(0.5)  # Pause half a second between toggles
