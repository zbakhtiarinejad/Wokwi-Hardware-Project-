# Wokwi Hardware Project

## 📅 Date: August 11, 2026

### 🛠️ What I Built
* Wired two LEDs to GPIO Pin 4 and Pin 5 on a Raspberry Pi Pico board.
* Wrote a MicroPython script to send 3.3V power through output pins to control both LEDs at the same time.

### 🐛 Bug & Fix
* **Issue:** Hit a `NameError: name 'led1' isn't defined` when trying to turn on the lights.
* **Solution:** Realized I had overwritten the variable name `led` for both pins. Fixed it by declaring unique variables (`led1 = Pin(5)` and `led2 = Pin(4)`).

---

## 📅 Date: August 12, 2026

### 🛠️ What I Built
* Extended my Raspberry Pi Pico setup to control two red LEDs using a pushbutton as a physical input trigger.
* Programmed GP14 as a digital input pin (`Pin.IN`, `Pin.PULL_DOWN`) in MicroPython to read high/low states from the button.

### 🔍 Debugging
* **Issue:** The LEDs wouldn't illuminate when pressing the button, even though the code logic was running smoothly.
* **Root Cause Analysis:** Realized that 4-pin tactile buttons have internal connections across horizontal pairs. Connecting wires across the top pins didn't complete the circuit when pressed.
* **Solution:** Placed both connections on the left side (top-left for 3.3V power, bottom-left for GP14 signal). When pressed, the internal switch bridges the gap, taking GP14 high (1) and triggering both LEDs to turn on simultaneously.
