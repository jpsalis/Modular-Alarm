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

# RTC
import rtc
r = rtc.RTC()

WIDTH = 128
HEIGHT = 64
BORDER = 3

displayio.release_displays()

#I2C
i2c = board.I2C()
display_bus = i2cdisplaybus.I2CDisplayBus(i2c, device_address=0x3c)

# DISPLAY
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=WIDTH, height=HEIGHT)

#SETUP DISPLAY GROUPS
splash = displayio.Group()
display.root_group = splash
'''
color_bitmap = displayio.Bitmap(WIDTH, HEIGHT, 1)
color_palette = displayio.Palette(2)
color_palette[0] = 0xFFFFFF  # White
bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
splash.append(bg_sprite)

inner_bitmap = displayio.Bitmap(WIDTH - BORDER * 2, HEIGHT - BORDER * 2, 1)
inner_palette = displayio.Palette(1)
inner_palette[0] = 0x000000  # Black
inner_sprite = displayio.TileGrid(
    inner_bitmap, pixel_shader=inner_palette, x=BORDER, y=BORDER
)
splash.append(inner_sprite)
'''
# Draw labels
main_label = label.Label(
    terminalio.FONT,
    text="12:00PM",
    scale = 2,
    color=0xFFFFFF,
    anchor_point=(0.5,0.5),
    anchored_position=(WIDTH // 2, (HEIGHT // 2))
)
splash.append(main_label)

left_label = label.Label(
    terminalio.FONT,
    text="Lorem",
    color=0xFFFFFF,
    anchor_point=(0,1),
    anchored_position=(2, HEIGHT - 2)
)
splash.append(left_label)

right_label = label.Label(
    terminalio.FONT,
    text="Lorem",
    color=0xFFFFFF,
    anchor_point=(1,1),
    anchored_position=(WIDTH - 2, HEIGHT - 2)
)
splash.append(right_label)

nav_label = label.Label(
    terminalio.FONT,
    text="Menu",
    color=0xFFFFFF,
    anchor_point=(1,0),
    anchored_position=(WIDTH - 2, 2)
)
splash.append(nav_label)

while True:
    pass