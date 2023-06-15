from os import system
from colorsys import hsv_to_rgb
from time import sleep

hue = 0.0

def hsv2rgb(h,s,v):
    return tuple(round(i * 255) for i in hsv_to_rgb(h,s,v))

while True:
    color = hsv2rgb(hue , 1 ,1)
    color = '#{:02x}{:02x}{:02x}'.format(color[0], color[1], color[2])
    system(f'bspc config focused_border_color "{color}"')
    sleep(0.08)
    hue += 0.05
    continue
