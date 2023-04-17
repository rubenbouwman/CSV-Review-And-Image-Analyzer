import os
from colorthief import ColorThief # >>> pip install colorthief <<<
# -------------------- Variables --------------------
Colors = []

# -------------------- Methods --------------------
def analyzeColors():
    print('Analyzing...')
    for filename in os.listdir('Images'):
        if filename == '.gitignore':
            continue
        color_thief = ColorThief(f'Images/{filename}')
        # get the dominant color
        dominant_color = color_thief.get_color(quality=1)
        print(f'File: {filename} >>> Dominant color: {dominant_color}')
        Colors.append(dominant_color)

# -------------------- run --------------------
analyzeColors()