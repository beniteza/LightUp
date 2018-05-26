# LightUp

## Introduction

Animated LEDs are fantastic for decorating kitchens, personal computer desks, the outside of a house, bottom side of vehicles, cosplays, and many more things. Unfortunately the code that one has to create tends to be long and very confusing to those who aren’t programmers. LightUp aims to make animating LEDs as simple as possible.

## Language Tutorial

### Terminal Commands and Python Libraries to Install
Commands:
1. sudo apt-get update
2. sudo apt-get install arduino-mk
3. sudo usermod -a -G dialout *ubuntu_username*
4. sudo chmod a+rw /dev/ttACM0
5. export PYTHONPATH=$PYTHONPATH: /host/Python35/Lib/site-packages

Libraries:
1. PLY
2. pyserial

### How to Use
1. Open the LightUpCode.txt file and write START on the first line. 
2. (Optional) Create a variable to hold a color value. Acceptable colors are: RED, BLUE, GREEN, ORANGE, PURPLE, WHITE, YELLOW
3. (Optional) Create a variable to hold a time delay (measured in milliseconds). 
4. Call the animate function by writing: ANIMATE. 
5. Choose an animation. Acceptable animations are: THEATER_CHASE_RAINBOW, RAINBOW, RAINBOW_CYCLE, COLOR_WIPE, THEATER_CHASE. 
6. Add the color and time variable after the selected animation. 
7. Write END to close the code to be translated.

### Video Demonstration
...link...

## Reference Manual

TODO

## Language Development

TODO

## Conclusion

LightUp makes animating LEDs an easy task. It removes the barrier of understanding the C porgramming language and takes the user straight to what they want to do. This porgramming language can also serve as an introdcution to programming for those users that have never touched the subject at all. 

SPRING 2018 ICOM4036/CIIC4030 PL PROJECT
