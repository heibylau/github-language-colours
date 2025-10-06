'''
Luminance formula: https://stackoverflow.com/questions/3942878/how-to-decide-font-color-in-white-or-black-depending-on-background-color
'''

def get_font_colour(hex):
    hex = hex[1:]

    # Convert hex to RGB integers
    r = int(hex[0:2], 16)
    g = int(hex[2:4], 16)
    b = int(hex[4:6], 16)

    luminance = (0.299 * r + 0.587 * g + 0.114 * b)

    return 'black' if luminance > 186 else 'white'