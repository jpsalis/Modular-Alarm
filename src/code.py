# AUTHOR: Joseph Salisbury
# Project Name: Annoying Alarm Clock

# General
import board
import displayio
import time

# Display
import i2cdisplaybus
import adafruit_displayio_ssd1306
from adafruit_display_text import label
import terminalio #Font

import adafruit_ds3231

WIDTH = 128
HEIGHT = 64
days = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")

displayio.release_displays()

#I2C
i2c = board.I2C()
display_bus = i2cdisplaybus.I2CDisplayBus(i2c, device_address=0x3c)
rtc = adafruit_ds3231.DS3231(i2c)

# DISPLAY
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=WIDTH, height=HEIGHT)

#SETUP DISPLAY GROUPS
splash = displayio.Group()
display.root_group = splash

# DRAW LABELS
main_label = label.Label(
    terminalio.FONT, scale = 2, color=0xFFFFFF,
    anchor_point=(0.5,0.5), anchored_position=(WIDTH // 2, (HEIGHT // 2 - 5))
)
left_label = label.Label(
    terminalio.FONT, text="SNOOZE", color=0xFFFFFF,
    anchor_point=(0,1), anchored_position=(2, HEIGHT - 2)
)
right_label = label.Label(
    terminalio.FONT, text="1-#-3-#", color=0xFFFFFF,
    anchor_point=(1,1), anchored_position=(WIDTH - 2, HEIGHT - 2)
)

splash.append(main_label)
splash.append(left_label)
splash.append(right_label)

day_label = label.Label(
    terminalio.FONT,
    color=0xFFFFFF,
    text="12:00 PM",
    anchor_point=(1,0),
    anchored_position=(WIDTH - 2, 2)
)
splash.append(day_label)

if False:
    #                     year, mon, date, hour, min, sec, wday, yday, isdst
    t = time.struct_time((2024,  5,   6,   13,  29,   0,   3,   -1,    -1))
    # you must set year, mon, date, hour, min, sec and weekday
    rtc.datetime = t

while True:
    t = rtc.datetime
    main_label.text = f'{t.tm_hour:02}:{t.tm_min:02}'
    
    # Update Screen
        # If received button update, determine 
    # Check event queue for new event
    
    # if new event, append to active event queue
    
    # for event in active event queue, 

    time.sleep(0.5) # wait a second


# Settings menu idea:
'''
    Sets a new root group which is constructed before screen transition to menu or alarm state
'''