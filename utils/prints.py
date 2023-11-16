# Prints the line given with the specified color in RBG
def color_print(cad, color_code):
    print(f"\033[{color_code}m{str(cad)}\033[0m")

# Prints the line given in red
def red_print(cad):
    color_print(cad, 91)

# Prints the line given in green
def green_print(cad):
    color_print(cad, 92)

# Prints the line given in yellow
def yellow_print(cad):
    color_print(cad, 93)

# Prints the line given in blue
def blue_print(cad):
    color_print(cad, 94)

# Prints the line given in magenta
def magenta_print(cad):
    color_print(cad, 95)

# Prints the line given in cyan
def cyan_print(cad):
    color_print(cad, 96)

# Prints the line given in white
def white_print(cad):
    color_print(cad, 97)
