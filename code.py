# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

kbd = Keyboard(usb_hid.devices)

# define buttons. these can be any physical switches/buttons, but the values
# here work out-of-the-box with a CircuitPlayground Express' A and B buttons.
geleKnop = digitalio.DigitalInOut(board.GP0)
geleKnop.direction = digitalio.Direction.INPUT
geleKnop.pull = digitalio.Pull.UP

rodeKnop = digitalio.DigitalInOut(board.GP1)
rodeKnop.direction = digitalio.Direction.INPUT
rodeKnop.pull = digitalio.Pull.UP

blauweKnop = digitalio.DigitalInOut(board.GP2)
blauweKnop.direction = digitalio.Direction.INPUT
blauweKnop.pull = digitalio.Pull.UP

while True:
    if not(geleKnop.value):
        kbd.send(Keycode.LEFT_ARROW)

    elif not(rodeKnop.value):
        kbd.send(Keycode.SPACE)
    
    elif not(blauweKnop.value):
        kbd.send(Keycode.RIGHT_ARROW)

    time.sleep(0.1)
