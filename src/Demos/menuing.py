import board
import time
import microcontroller
from digitalio import DigitalInOut, Direction, Pull
from adafruit_debouncer import Debouncer

import displayio
import i2cdisplaybus
import adafruit_displayio_ssd1306

from fruity_menu import menu, builder

import rotaryio

import rtc

# DISPLAY
WIDTH = 128
HEIGHT = 64

displayio.release_displays() # Is this needed?

#I2C
i2c = board.I2C()
display_bus = i2cdisplaybus.I2CDisplayBus(i2c, device_address=0x3c)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=WIDTH, height=HEIGHT)

# MENU
menu = menu.Menu(display, width=WIDTH, height=HEIGHT, title='Main Menu')
    
# RTC
r = rtc.RTC()

btn = DigitalInOut(board.D9)
btn.direction = Direction.INPUT
btn.pull = Pull.UP
deb_btn = Debouncer(btn)

# ROTARY ENCODER
encoder = rotaryio.IncrementalEncoder(board.D6, board.D5)



# Navigation system
# When navigation queue is empty, displays clock
def main():
    
    menu_items = {
        'Shut down': microcontroller.reset,
        'Settings': {
            'Screen brightness': builder.Value(round(display.brightness * 100), update_brightness, scroll_factor=5, min_val=0, max_val=100)
        }
    }
    builder.build_menu(menu, menu_items)
    
    
    last_position = encoder.position
    last_button = None
    menu.show_menu()
    while True:
        position = encoder.position
        deb_btn.update()
        
        
        if position != last_position:
            menu.scroll(position - last_position)
            last_position = position
            menu.show_menu()
            
        elif deb_btn.fell:
            menu.click()
            
        last_button = deb_btn.value
        
    
def update_brightness(brightness):
    display.brightness = brightness / 100
    
if __name__ == "__main__":
    main()