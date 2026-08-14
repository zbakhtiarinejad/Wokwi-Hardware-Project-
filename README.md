# Wokwi-Hardware-Project-
Date: August 11, 2026

What I Built:​
Wired two LEDs to GPIO Pin 4 and Pin 5 on a Raspberry Pi Pico board.​Wrote a MicroPython script to send 3.3V power through output pins to control both LEDs at the same time.​
Bug & Fix:
​Issue: Hit a NameError: name 'led1' isn't defined when trying to turn on the lights. 
Solution: Realized I had overwritten the variable name led for both pins. Fixed it by declaring unique variables (led1 = Pin(5) and led2 = Pin(4)).


