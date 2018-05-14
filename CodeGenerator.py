import os
# import pyserial
import subprocess

initialCode = []
variables = {}
wheels = []
rainbows = []
rainbowCycles = []
theaterChaseRainbows = []
loop = []


def createVariable(command):
    variables[command[1]] = command[2]
    print(variables)


def animate(command):
    # Step 1: Default code
    createInitialCode()

    # Step 2: Check for variables
    animation = ""
    color = ""
    colorRGB = ()
    time = 0

    # a) Animation
    if command[1] not in variables:
        animation = command[1]
    else:
        animation = variables[command[1]]

    # b) Color
    if command[2] not in variables:
        if isinstance(command[2], tuple):
            colorRGB = command[2]
        else:
            color = command[2]
    elif isinstance(variables[command[2]], tuple):
        colorRGB = variables[command[2]]
    else:
        color = variables[command[2]]

    # c) Time
    if command[3] not in variables:
        time = command[3]
    else:
        time = variables[command[3]]

    # Step 3: Animation code
    if animation == "RAINBOW":
        if color != "":
            colorRGB = returnRGB(color)
        createRainbowAnimation(colorRGB, time)
    elif animation == "RAINBOW_CYCLE":
        if color != "":
            colorRGB = returnRGB(color)
        createRainbowCycleAnimation(colorRGB, time)
    elif animation == "THEATER_CHASE_RAINBOW":
        if color != "":
            colorRGB = returnRGB(color)
        createTheaterChaseRainbowAnimation(colorRGB, time)
    elif animation == "COLOR_WIPE":
        colorRGB = returnRGB(color)
        createColorWipeAnimation(colorRGB, time)
    elif animation == "THEATER_CHASE":
        colorRGB = returnRGB(color)
        createTheaterChaseAnimation(colorRGB, time)


# Pass rgb tuple for wheel creation and time delay
#Missing definition code
def createRainbowAnimation(colorRGB, time):
    wheelNumber = createColorWheel(colorRGB)
    #Animation method
    rainbowNumber = len(rainbows) + 1
    arduinoBlock = "void rainbow_"+ str(rainbowNumber) + "(uint8_t wait) {\n" \
                    "uint16_t i, j;\n" \
                    "\n" \
                    "for(j=0; j<256; j++) {\n" \
                    "for(i=0; i<strip.numPixels(); i++) {\n" \
                    "strip.setPixelColor(i, Wheel_"+ str(wheelNumber) + "((i+j) & 255));\n" \
                    "}\n" \
                    "strip.show();\n" \
                    "delay(wait);\n" \
                    "}\n" \
                    "}\n"

    rainbows.append(arduinoBlock)
    # Call the animation on the loop method
    arduinoLine = "  rainbow_"+ str(rainbowNumber) + "(" + time + ");\n"
    loop.append(arduinoLine)


#Missing definition code
def createRainbowCycleAnimation(colorRGB, time):
    wheelNumber = createColorWheel(colorRGB)
    #Animation method
    rainbowCycleNumber = len(rainbowCycles) + 1
    arduinoBlock = "void rainbowCycle_"+ str(rainbowCycleNumber) + "(uint8_t wait) {\n" \
                    "uint16_t i, j;\n" \
                    "\n" \
                    "for(j=0; j<256*5; j++) {\n" \
                    "for(i=0; i<strip.numPixels(); i++) {\n" \
                    "strip.setPixelColor(i, Wheel_"+ str(wheelNumber) + "(((i * 256 / strip.numPixels()) + j) & 255));\n" \
                    "}\n" \
                    "strip.show();\n" \
                    "delay(wait);\n" \
                    "}\n" \
                    "}\n"
    rainbowCycles.append(arduinoBlock)

    # Call the animation on the loop method
    arduinoLine = "  rainbowCycle_"+ str(rainbowCycleNumber) + "(" + time + ");\n"
    loop.append(arduinoLine)


#Missing definition code
def createTheaterChaseRainbowAnimation(colorRGB, time):
    wheelNumber = createColorWheel(colorRGB)
    #Animation method
    theaterCRainbowNumber = len(theaterChaseRainbows) + 1
    arduinoBlock = "void theaterChaseRainbow_"+ str(theaterCRainbowNumber) + "(uint8_t wait) {\n" \
                    "for (int j=0; j < 256; j++) {\n" \
                    "for (int q=0; q < 3; q++) {\n" \
                    "for (uint16_t i=0; i < strip.numPixels(); i=i+3) {\n" \
                    "strip.setPixelColor(i+q, Wheel_"+ str(wheelNumber) + "( (i+j) % 255));\n" \
                    "}\n" \
                    "strip.show();\n" \
                    "\n" \
                    "delay(wait);\n" \
                    "\n" \
                    "for (uint16_t i=0; i < strip.numPixels(); i=i+3) {\n" \
                    "strip.setPixelColor(i+q, 0);\n" \
                    "}\n" \
                    "}\n" \
                    "}\n" \
                    "}\n"

    theaterChaseRainbows.append(arduinoBlock)
    #Call the animation on the loop method
    arduinoLine = "  theaterChaseRainbow_"+ str(theaterCRainbowNumber) + "(" + time + ");\n"
    loop.append(arduinoLine)


# Pass color to be used and time delay
def createColorWipeAnimation(colorRGB, time):
    arduinoLine = "  colorWipe(strip.Color(" + str(colorRGB[0]) + "," + str(colorRGB[1]) + ", " + str(colorRGB[2]) + "), " + time + ");\n"
    loop.append(arduinoLine)


def createTheaterChaseAnimation(colorRGB, time):
    arduinoLine = "  theaterChase(strip.Color(" + str(colorRGB[0]) + "," + str(colorRGB[1]) + ", " + str(colorRGB[2]) + "), " + time + ");\n"
    loop.append(arduinoLine)


#Work in progress
def createColorWheel(colorRGB):
    wheelNumber = len(wheels) + 1
    arduinoBlock = "uint32_t Wheel_" + str(wheelNumber) + "(byte WheelPos) {\n" \
                   "   WheelPos = 255 - WheelPos;\n" \
                   "   if (WheelPos < 85)\n" \
                   "       {\n" \
                   "       return strip.Color(" + str(colorRGB[0]) + "- WheelPos * 3, 0, WheelPos * 3);\n" \
                   "       }" \
                   "   if (WheelPos < 170) {\n" \
                   "       WheelPos -= 85;\n" \
                   "       return strip.Color(0, WheelPos * 3, " + str(colorRGB[2]) + " - WheelPos * 3);\n" \
                   "   }\n" \
                   "   WheelPos -= 170;\n" \
                   "   return strip.Color(WheelPos * 3, " + str(colorRGB[1]) + " - WheelPos * 3, 0);\n" \
                   "}\n"
    wheels.append(arduinoBlock)
    return wheelNumber


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


# Generates the default Arduino code
def createInitialCode():
    defaultCode = "#include <Adafruit_NeoPixel.h> \n" \
                  "#ifdef __AVR__ \n" \
                  "  #include <avr/power.h> \n" \
                  "#endif \n" \
                  " \n" \
                  "#define PIN 6 \n" \
                  "    \n" \
                  "Adafruit_NeoPixel strip = Adafruit_NeoPixel(12, PIN, NEO_GRB + NEO_KHZ800); \n" \
                  "   \n" \
                  "void setup() { \n" \
                  "  #if defined (__AVR_ATtiny85__) \n" \
                  "    if (F_CPU == 16000000) clock_prescale_set(clock_div_1); \n" \
                  "  #endif \n" \
                  "  // End of trinket special code \n" \
                  "\n" \
                  "  strip.begin(); \n" \
                  "  strip.show(); // Initialize all pixels to 'off' \n" \
                  "} \n" \
                  "\n" \
                  "// Fill the dots one after the other with a color \n" \
                  "void colorWipe(uint32_t c, uint8_t wait) { \n" \
                  "  for(uint16_t i=0; i<strip.numPixels(); i++) { \n" \
                  "   strip.setPixelColor(i, c); \n" \
                  "    strip.show(); \n" \
                  "    delay(wait); \n" \
                  "  } \n" \
                  "} \n" \
                  "           \n" \
                  "void theaterChase(uint32_t c, uint8_t wait) { \n" \
                  "  for (int j=0; j<10; j++) {  //do 10 cycles of chasing \n" \
                  "    for (int q=0; q < 3; q++) { \n" \
                  "      for (uint16_t i=0; i < strip.numPixels(); i=i+3) { \n" \
                  "        strip.setPixelColor(i+q, c); \n" \
                  "      } \n" \
                  "      strip.show(); \n" \
                  "            \n" \
                  "      delay(wait); \n" \
                  "            \n" \
                  "      for (uint16_t i=0; i < strip.numPixels(); i=i+3) { \n" \
                  "        strip.setPixelColor(i+q, 0); \n" \
                  "     } \n" \
                  "    } \n" \
                  "  } \n" \
                  "}\n"

    initialCode.append(defaultCode)


#Creates the final code to be used and uploads it to the arduino
def upload():
    finalCode = initialCode[0]

    #Adds the wheel(s)
    for w in wheels:
        finalCode += w

    #Adds the animation methods
    #a. rainbow
    for r in rainbows:
        finalCode += r

    #b. rainbow cycle
    for rc in rainbowCycles:
        finalCode += rc

    #c. theater chase rainbow
    for tcr in theaterChaseRainbows:
        finalCode += tcr

    #Adds lines for the loop method
    finalCode += "void loop() {\n"

    for line in loop:
        finalCode += line

    finalCode += "}"

    #Create arduino file
    filePath = "arduinoCode.ino"
    arduinoCode = open(filePath, 'w')
    arduinoCode.write(finalCode)
    arduinoCode.close()


def terminalUpload():
    os.system("make upload clean")
