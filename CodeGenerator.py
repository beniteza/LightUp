arduinoCode = ""
variables = {}

def createVariable(command):
    variables[command[1]] = command[2]
    # print("New variable name: " + command[1])
    # print("Variable value: " + variables[command[1]])
    # print("Current variables:")
    print(variables)

def animate(command):
    #Step 1: Default code
    createInitialCode()

    #Step 2: Check for variables
    animation = ""
    color = ""
    colorRGB = ()
    time = 0

    #a) Animation
    if command[1] not in variables:
        animation = command[1]
    else:
        animation = variables[command[1]]

    #b) Color
    if command[2] not in variables:
        if isinstance(command[2], tuple):
            colorRGB = command[2]
        else:
            color = command[2]
    elif isinstance(variables[command[2]], tuple):
            colorRGB = variables[command[2]]
    else:
        color = variables[command[2]]

    #c) Time
    if command[3] not in variables:
        time = command[3]
    else:
        time = variables[command[3]]

    # print("Animation: " + animation)
    # print("Color: " + color)
    # print("ColorRGB: ")
    # print(colorRGB)
    # print("Time: ")
    # print(time)

    #Step 3: Animation code
    if animation == "RAINBOW":
        createRainbowAnimation(colorRGB, time)
    elif animation == "RAINBOW_CYCLE":
        createRainbowCycleAnimation(colorRGB, time)
    elif animation == "THEATER_CHASE_RAINBOW":
        createTheaterChaseRainbowAnimation(colorRGB, time)
    elif animation == "COLOR_WIPE":
        colorRGB = returnRGB(color)
        # print("The RGB is: ")
        # print(colorRGB)
        createColorWipeAnimation(colorRGB, time)
    elif animation == "THEATER_CHASE":
        colorRGB = returnRGB(color)
        # print("The RGB is: ")
        # print(colorRGB)
        createColorWipeAnimation(colorRGB, time)


#Pass rgb tuple for wheel creation and time delay
def createRainbowAnimation(colorRGB, time):
    pass
def createRainbowCycleAnimation(colorRGB, time):
    pass
def createTheaterChaseRainbowAnimation(colorRGB, time):
    pass
#Pass color to be used and time delay
def createColorWipeAnimation(colorRGB, time):
    pass
def createTheaterChaseAnimation(colorRGB, time):
    pass

def createColorWheel(colorRGB):
    pass

#Generates the default Arduino code
def createInitialCode():
    pass

def returnRGB(color):
    if color == 'RED':
        return (255, 0, 0)
    if color == 'BLUE':
        return (0, 0, 255)
    if color == 'GREEN':
        return (0, 255, 0)
    if color == 'YELLOW':
        return (255, 255, 0)
    if color == 'ORANGE':
        return (255, 165, 0)
    if color == 'PURPLE':
        return (128, 0, 128)
    if color == 'WHITE':
        return (255, 255, 255)