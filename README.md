# pico_circuitpython_hid
CircuitPython program for the raspberry pi pico to emulate a keyboard

## One time setup
Install MicroPython on your raspberry pi pico: https://learn.adafruit.com/getting-started-with-raspberry-pi-pico-circuitpython/circuitpython

## Wiring it up
* Connect three buttons to the `GND`.
* Connect the other sides of the buttons to GP0, GP1 and GP2.
* The program pulls the GPIO pins high. Pressing a button pulls them down to ground, which we check for in the program.

## Uploading the program

* Plug in your raspberry pi pico
* On your pc open Thonny
* In Thonny select Execute -> Configure Interpreter -> CircuitPython (generic)
* Open View -> Files
* Browse to folder where you have cloned or downloaded this repository
* Right click the `adafruit_hid` folder and select `Copy to \`.
* Right click `main.py` and select `Copy to \`.
* Whenever the pico is connected to USB it will execute the main.py program.

## Editing the program
* Follow the steps above under "Uploading the program"
* Edit main.py
* For testing: select the run button in Thonny
* To persist your program to the pico when you are ready: Right click `main.py` and select `Copy to \`.
