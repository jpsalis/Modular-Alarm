# SPDX-FileCopyrightText: Copyright (c) 2022 Erik Hess
#
# SPDX-License-Identifier: MIT

import board
import time
import digitalio
from hx711.hx711_gpio import HX711_GPIO

gpio_data = digitalio.DigitalInOut(board.D5)

gpio_clk = digitalio.DigitalInOut(board.D6)

hx = HX711_GPIO(gpio_data, gpio_clk, scalar = 25, tare=True)

while True:
    reading = hx.read(2)
    #reading_raw = hx.read_raw()
    print(
        f"{reading: 8.2f} g occupied: {reading >= 250}")

    time.sleep(1)