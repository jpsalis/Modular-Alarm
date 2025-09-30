# AUTHOR: Joseph Salisbury
# Project Name: Annoying Alarm Clock

# General
import board
import displayio
import digitalio
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


'''
MenuDisplay
    Displays a splash screen with menu options based on set_items
    Set display.root_group to menu_display.splash to display contents
'''
class MenuDisplay:
    def __init__(self, width, height):
        self.options = []
        self.WIDTH = width
        self.HEIGHT = height

        self.FONT = terminalio.FONT
        
        self.OPTION_COUNT = 5
        # Centers text on the screen based on the line spacing
        self.line_spacing = 13
        self.vert_offset = (self.HEIGHT - self.line_spacing * (self.OPTION_COUNT - 1)) // 2
        
        
        # Create a splash screen that's initially just unused.
        self._splash = displayio.Group()
        
        self.items_label = label.Label(
            self.FONT,
            anchor_point=(0.0, 0.0), anchored_position=(10, 0),
            text = "Alarms\nSet Time\nOptions\nModules\nBack"
        )
        
        #self.cursor = label.Label(self.FONT, scale=self.SCALE, anchor_point=(0.0, 0.0), anchored_position=(0, 0), text=" \n\n>")
        
        self.cursor = label.Label(terminalio.FONT, anchor_point=(0, 0.5), anchored_position=(0, self.vert_offset), text=">")
        
        self.option_labels = [
            label.Label(self.FONT,
                        x = 10,
                        y = i * self.line_spacing + self.vert_offset)
            for i in range(self.OPTION_COUNT)]
                
        self.val_labels = [
            label.Label(self.FONT,
                        anchor_point=(1.0, 0.5),
                        anchored_position=(self.WIDTH, i * self.line_spacing + self.vert_offset))
            for i in range(self.OPTION_COUNT)]
        

        for l in self.option_labels:
            self._splash.append(l)
        
        for l in self.val_labels:
            self._splash.append(l)
        

        self._splash.append(self.cursor)
        
        

        
        
    ''' Gives MenuDisplay instance new options to display. Stored as list of strings.
        Also resets cursor position '''
    def set_options(self, options):
        pass
    
    ''' Returns index of currently selected option, or a tuple with the index and the value. -1 if invalid for whatever reason (Or back button?).
            TODO: Handle errors
    '''
    def get_cur_option(self):
        pass

    @property
    def splash(self):
        return self._splash
    
class Home:
    pass

class Button:
    def __init__(self, pin, pull = digitalio.Pull.DOWN):
        self.pin = digitalio.DigitalInOut(pin)
        self.pin.direction = pull
        self._value = self.pin.value
        self._changed = False
    
    def update(self):
        # Read button state and check for changes
        next_value = self.pin.value
        self._changed = True if next_value != self.value else False
        self._value = next_value
        
    # Can only be safely changed internally
    @property
    def changed(self):
        return self._changed
    
    @property
    def value(self):
        return self._value
    
def main():
    
    #SETUP DISPLAY GROUPS
    
    menu = MenuDisplay(WIDTH, HEIGHT)
    display.root_group = menu.splash
    while True:
        # Update buttons
        '''
        leftButton.update()
        rightButton.update()
        enter.update()
        '''
        
        
        # if button was updated:
            #Figure out 

        time.sleep(0.1)

if __name__ == "__main__":
    main()