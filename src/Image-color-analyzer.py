# Code for RGB Code to Name is by Mir AbdulHaseeb
# https://medium.com/codex/rgb-to-color-names-in-python-the-robust-way-ec4a9d97a01f

import os
from colorthief import ColorThief # >>> pip install colorthief <<<
from scipy.spatial import KDTree
from webcolors import (
    CSS3_HEX_TO_NAMES,
    hex_to_rgb,
)
# -------------------- Variables --------------------
ColorCodes = []
ColorNames = []

# -------------------- Methods --------------------
def colorToText(rgb_tuple):
    # a dictionary of all the hex and their respective names in css3
    css3_db = CSS3_HEX_TO_NAMES
    names = []
    rgb_values = []
    for color_hex, color_name in css3_db.items():
        names.append(color_name)
        rgb_values.append(hex_to_rgb(color_hex))
    
    kdt_db = KDTree(rgb_values)
    distance, index = kdt_db.query(rgb_tuple)
    return names[index]

def analyzeColors():
    print('Analyzing...')
    for filename in os.listdir('Images'):
        color_thief = ColorThief(f'Images/{filename}')
        # get the dominant color
        dominant_color = color_thief.get_color(quality=1)
        colorName = colorToText(dominant_color)
        print(f'File: {filename} >>> Dominant color: {dominant_color}   Color name: {colorName}')
        ColorNames.append(colorName)
        ColorCodes.append(dominant_color)

# -------------------- run --------------------
analyzeColors()