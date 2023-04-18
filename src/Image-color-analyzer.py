# Code used for RGB Code to Name is by Mir AbdulHaseeb (colorToText method)
# https://medium.com/codex/rgb-to-color-names-in-python-the-robust-way-ec4a9d97a01f

import os
import numpy as np
import pandas as pd
from colorthief import ColorThief
from scipy.spatial import KDTree
from webcolors import (CSS3_HEX_TO_NAMES, hex_to_rgb,)

# -------------------- Variables --------------------
ColorCodes = []
ColorNames = []

namesDictionary = []
rgb_values = []
# -------------------- Color Analyze Methods --------------------
# Fills the namesDictionary and rgb_values lists with the contents from the css3 dictionary
def createColorNames():
    # a dictionary of all the hex and their respective names in css3
    css3_db = CSS3_HEX_TO_NAMES
    for color_hex, color_name in css3_db.items():
        namesDictionary.append(color_name)
        rgb_values.append(hex_to_rgb(color_hex))

# This method assigns a matching name to the given RGB color code
def colorToText(rgb_tuple):
    kdt_db = KDTree(rgb_values)
    distance, index = kdt_db.query(rgb_tuple)
    return namesDictionary[index]

# returns the RGB color code of the most dominant color within the image
def getDominantColor(filename):
    color_thief = ColorThief(f'Images/{filename}')
    # get the dominant color
    dominant_color = color_thief.get_color(quality=1)
    return dominant_color

# Analyzes all images in the 'Images' folder and puts the results in ArrayLists
def analyzeColors():
    print('Analyzing...')
    for filename in os.listdir('Images'):
        colorCode = getDominantColor(filename)
        colorName = colorToText(colorCode)
        print(f'Analyzing file... {filename} >>> Dominant color: {colorCode}   Color name: {colorName}')
        ColorNames.append(colorName)
        ColorCodes.append(colorCode)
        return {'filename':filename, 'dominant_color': colorCode, 'color_name': colorName}

# -------------------- Count Methods --------------------
def countColors():
        print(pd.value_counts(np.array(ColorNames)))

def createCSV():
     df = pd.DataFrame(analyzeColors())
     df.to_csv('Output/results.csv', index=False)

# -------------------- run --------------------
createColorNames()
createCSV()