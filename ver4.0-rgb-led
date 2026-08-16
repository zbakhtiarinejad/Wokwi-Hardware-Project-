from machine import Pin, PWM
from utime import sleep


led1 = Pin(5, Pin.OUT)
led2 = Pin(4, Pin.OUT)
button = Pin(14, Pin.IN, Pin.PULL_DOWN)


r_pwm = PWM(Pin(20))  # Red wire
g_pwm = PWM(Pin(19))  # Green wire
b_pwm = PWM(Pin(18))  # Blue wire


r_pwm.freq(1000)
g_pwm.freq(1000)
b_pwm.freq(1000)


def set_color(r, g, b):
    r_pwm.duty_u16(65535 - int(r * 257))
    g_pwm.duty_u16(65535 - int(g * 257))
    b_pwm.duty_u16(65535 - int(b * 257))


colors = [
    (255, 0, 0),      # Red
    (0, 255, 0),      # Green
    (0, 0, 255),      # Blue
    (255, 255, 0),    # Yellow
    (128, 0, 128),    # Purple
    (0, 255, 255)     # Cyan
]

color_index = 0
timer = 0

sleep(0.01) 
print("Hello, Pi Pico!")
print("System is ready! Press the button...")

set_color(255, 0, 0)

while True:
    if button.value() == 1:
        led1.on()
        led2.on()
    else:
        led1.off()
        led2.off()

    timer += 1

    if timer >= 20:
        current_color = colors[color_index]
        set_color(current_color[0], current_color[1], current_color[2])
        color_index = (color_index + 1) % len(colors)
        timer = 0

    sleep(0.05)
