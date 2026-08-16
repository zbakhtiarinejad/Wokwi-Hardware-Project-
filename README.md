# Wokwi Hardware Project

## Date: August 11, 2026

### What I Built
* Wired two LEDs to GPIO Pin 4 and Pin 5 on a Raspberry Pi Pico board.
* Wrote a MicroPython script to send 3.3V power through output pins to control both LEDs at the same time.

### Bug & Fix
* **Issue:** Hit a `NameError: name 'led1' isn't defined` when trying to turn on the lights.
* **Solution:** Realized I had overwritten the variable name `led` for both pins. Fixed it by declaring unique variables (`led1 = Pin(5)` and `led2 = Pin(4)`).

---

## Date: August 12, 2026

### What I Built
* Extended my Raspberry Pi Pico setup to control two red LEDs using a pushbutton as a physical input trigger.
* Programmed GP14 as a digital input pin (`Pin.IN`, `Pin.PULL_DOWN`) in MicroPython to read high/low states from the button.

### Debugging
* **Issue:** The LEDs wouldn't illuminate when pressing the button, even though the code logic was running smoothly.
* **Root Cause Analysis:** Realized that 4-pin tactile buttons have internal connections across horizontal pairs. Connecting wires across the top pins didn't complete the circuit when pressed.
* **Solution:** Placed both connections on the left side (top-left for 3.3V power, bottom-left for GP14 signal). When pressed, the internal switch bridges the gap, taking GP14 high (1) and triggering both LEDs to turn on simultaneously.


## Date: August 15, 2026

## Recent Updates & Enhancements

### What Was Added
* **Safety Resistor:** Added a resistor to the LED ground path to restrict current flow, protecting both the LEDs and the Raspberry Pi Pico GPIO pins from overcurrent damage.
### Debugging:

### Issue: LEDs Failed to Turn On After Adding the Resistor

#### Problem Identification
After introducing the resistor into the circuit, neither the cyan nor the magenta LED would light up when pressing the pushbutton. 

#### Root Cause Analysis
1. **Disconnected Resistor Lead (Floating Component):** The right leg of the resistor was not properly snapped into the board headers in Wokwi, leaving it hanging in the air and breaking the ground path.
2. **Incomplete Ground Circuit:** Current could not return to the Pico's ground line, preventing the circuit loop from closing.

#### Solution
1. Connected a wire directly from the right terminal of the resistor to the **GND** pin (**GND2) on the Raspberry Pi Pico.
2. Verified that both LED cathodes (short legs) connect to the left side of the resistor.
3. Confirmed that both LEDs successfully illuminate through the resistor when the pushbutton is held down.

### What Was Added
This update expands the Raspberry Pi Pico embedded control system by integrating a Common-Cathode RGB LED using multi-channel Pulse Width Modulation (PWM). The microcontroller concurrently handles GPIO input polling for standard indicator LEDs while executing a non-blocking color transition sequence across a predefined 8-bit RGB color palette.

---

## Technical Challenges & Engineering Solutions

### 1. Circuit Polarity Mismatch

* **Problem:** The RGB LED initially remained unlit despite active MicroPython PWM signals.
* **Root Cause:** The Wokwi simulator component was set to **Common Anode**, which requires a constant 3.3V rail on the common terminal and inverted logic (`LOW` = ON). Driving standard active-HIGH PWM signals resulted in 0V potential difference across the LED channels.
* **Fix:** Reconfigured the Wokwi component attribute to **Common Cathode** (`"common": "cathode"`) and wired the common terminal to Pico **GND**. This restored expected active-HIGH 16-bit PWM behavior (`0` = OFF, `65535` = full intensity).

### 2. MicroPython Type Errors & Invalid API Parameters

* **Problem:** Script execution threw runtime errors on initialization.
* **Root Cause:** Capitalization syntax errors (`pin` instead of `Pin`) and passing a `Pin` object into `.freq()` rather than a numeric integer value in Hertz.
* **Fix:** Standardized class imports from `machine` and updated PWM frequency calls to `r_pwm.freq(1000)` across all three channels.

### 3. Execution Blocking & Sequential Loop Halts

* **Problem:** Placing the pushbutton reading logic in a separate `while True` loop below the RGB loop caused the code to block permanently inside the first loop.
* **Fix:** Unified system logic into a single, non-blocking main execution loop. The pushbutton state is polled continuously every 50ms without halting the timer sequence.

### 4. Interval Timing Drift

* **Problem:** Incrementing `timer += 1` after resetting `timer = 0` created an off-by-one timing shift (0.95 seconds instead of 1.0 second per color transition).
* **Fix:** Adjusted loop counter execution sequence so `timer += 1` runs prior to evaluating `if timer >= 20:`. This guarantees precise 1.0-second state updates (20 × 0.05s) while resetting the counter cleanly to prevent unbounded integer memory growth.
