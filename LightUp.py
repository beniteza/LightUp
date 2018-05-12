import ply.lex as lex
import ply.yacc as yacc
import sys
import os
import subprocess

######################### LEXER #########################

tokens = [
    #Equals
    'EQUALS',
    #Color
    'RED', 'BLUE', 'GREEN', 'YELLOW', 'ORANGE', 'PURPLE', 'WHITE',
    # #RGB Color
    # 'RGB',
    #Animation Type
    'RAINBOW', 'RANDOW_CYCLE', 'THEATER_CHASE_RAINBOW', 'COLOR_WIPE', 'THEATER_CHASE',
    #Number
    'NUMBER',
    #Parenthesis and coma
    'LP', 'RP', 'COMA',
    #Animate
    'ANIMATE',
    #Button Position
    'BUTTON_UP', 'BUTTON_DOWN',
    # Variable Name
    'NAME',
    #NEW LINE
    'NEW_LINE'
]

t_NUMBER = r'[0-9]+'
t_LP = r'\('
t_RP = r'\)'
t_COMA = r'\,'
t_EQUALS = r'\='
# t_ignore = ' '
t_ignore = ' \t\n'

# def t_NEW_LINE(t):
#     r'\n'
#     t.value = 'NEW_LINE'
#     return t

def t_BUTTON_UP(t):
    r'BUTTON_UP'
    t.value = 'BUTTON_UP'
    return t

def t_BUTTON_DOWN(t):
    r'BUTTON_DOWN'
    t.value = 'BUTTON_DOWN'
    return t

def t_RED(t):
    r'RED'
    t.value = 'RED'
    return t

def t_BLUE(t):
    r'BLUE'
    t.value = 'BLUE'
    return t

def t_GREEN(t):
    r'GREEN'
    t.value = 'GREEN'
    return t

def t_YELLOW(t):
    r'YELLOW'
    t.value = 'YELLOW'
    return t

def t_ORANGE(t):
    r'ORANGE'
    t.value = 'ORANGE'
    return t

def t_PURPLE(t):
    r'PURPLE'
    t.value = 'PURPLE'
    return t

def t_WHITE(t):
    r'WHITE'
    t.value = 'WHITE'
    return t

def t_RGB(t):
    r'RGB'
    t.value = 'RGB'
    return t

def t_RAINBOW(t):
    r'RAINBOW'
    t.value = 'RAINBOW'
    return t

def t_RAINBOW_CYCLE(t):
    r'RAINBOW_CYCLE'
    t.value = 'RAINBOW_CYCLE'
    return t

def t_THEATER_CHASE_RAINBOW(t):
    r'THEATER_CHASE_RAINBOW'
    t.value = 'THEATER_CHASE_RAINBOW'
    return t

def t_COLOR_WIPE(t):
    r'COLOR_WIPE'
    t.value = 'COLOR_WIPE'
    return t

def t_THEATER_CHASE(t):
    r'THEATER_CHASE'
    t.value = 'THEATER_CHASE'
    return t

def t_ANIMATE(t):
    r'ANIMATE'
    t.value = 'ANIMATE'
    return t

def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = 'NAME'
    return t

def t_error(t):
    print("Illegal character '%s'" % t.value[0])

lexer = lex.lex()

# lexer.input("ANIMATE (RAINBOW YELLOW 50) \n =")
#
# while True:
#     tok = lexer.token()
#     if not tok:
#         break
#     print(tok)

######################### Parser #########################

precedence = (
    ()
)

def p_execute(p):
    '''
    execute : command
            | var_assign
            | empty
    '''
    print(p[1])
    # print(run(p[1]))

def p_var_assign(p):
    '''
    var_assign : NAME EQUALS color
               | NAME EQUALS rgb
               | NAME EQUALS miliseconds
               | NAME EQUALS animation
               | NAME EQUALS button_pos
    '''
    p[0] = ('=', p[1], p[3])

# def p_command_recursive(p):
#     '''
#     command : command command
#             | empty
#     '''

def p_command(p):
    '''
    command : ANIMATE animation color miliseconds
            | ANIMATE animation rgb miliseconds
    '''
    p[0] = (p[1], p[2], p[3], p[4])

def p_button_pos(p):
    '''
    button_pos : BUTTON_UP
               | BUTTON_DOWN
    '''
    p[0] = p[1]

def p_button_pos_var(p):
    '''
    button_pos : NAME
    '''
    p[0] = ('var', p[1])

def p_rgb(p):
  'rgb : LP NUMBER COMA NUMBER COMA NUMBER RP'
  p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + p[6] + p[7]

def p_rgb_var(p):
    '''
    rgb : NAME
    '''
    p[0] = ('var', p[1])

def p_miliseconds(p):
    '''
    miliseconds : NUMBER
    '''
    p[0] = p[1]

def p_miliseconds_var(p):
    '''
    miliseconds : NAME
    '''
    p[0] = ('var', p[1])

def p_color(p):
  '''
  color : RED
        | BLUE
        | GREEN
        | YELLOW
        | ORANGE
        | PURPLE
        | WHITE
  '''
  p[0] = p[1]

def p_color_var(p):
    '''
    color : NAME
    '''
    p[0] = ('var', p[1])

def p_animation(p):
  '''
  animation : RAINBOW
            | RANDOW_CYCLE
            | THEATER_CHASE_RAINBOW
            | COLOR_WIPE
            | THEATER_CHASE
  '''
  p[0] = p[1]

def p_animation_var(p):
    '''
    animation : NAME
    '''
    p[0] = ('var', p[1])

def p_empty(p):
    '''
    empty :
    '''
    p[0] = None

def p_error(p):
    print("Syntax error found!")

parser = yacc.yacc()

env = {}

def run(p):
    global env
    if type(p) == tuple:
        if p[0] == '=':
            env[p[1]] = run(p[2])
            print(env)
        elif p[0] == 'var':
            if p[1] not in env:
                return 'Undeclared variable found!'
            else:
                return env[p[1]]
        print(p)
    else:
        return p

# while True:
#     try:
#         s = input('>>')
#     except EOFError:
#         break
#     parser.parse(s)

def translateCode(p):
    try:
        LightUpSource = open(p, 'r')
    except IOError:
        print("Error opening file")
        exit()

    # fileText = LightUpSource.read()
    #
    # parser.parse(fileText)

    for line in LightUpSource:
        try:
            parser.parse(line)
        except IOError:
            print("Error opening file")
            exit()

file = 'LightUpCode.txt'
translateCode(file)

# def openArduino():
#     try:
#         # subprocess.Popen('/usr/share/applications/Arduino IDE')
#         os.system('/home/ubuntu/Downloads/arduino-1.8.5/arduino')
#     except Exception:
#         print("Cannot open Arduino IDE")
#
# openArduino()

######################### INTERMEDIATE CODE #########################
arduinoCode = []

defaultCode = "#include <Adafruit_NeoPixel.h> \n" \
              "#ifdef __AVR__ \n" \
              "#include <avr/power.h> \n" \
              "#endif \n" \
              "#define PIN 6 Adafruit_NeoPixel strip = Adafruit_NeoPixel(60, PIN, NEO_GRB + NEO_KHZ800); \n" \
              "void setup() \n" \
              "{ \n" \
              "#if defined (__AVR_ATtiny85__) \n" \
              "if (F_CPU == 16000000) clock_prescale_set(clock_div_1); \n" \
              "#endif \n" \
              "// End of trinket special code \n" \
              "strip.begin(); \n" \
              "strip.show(); \n" \
              "// Initialize all pixels to 'off' \n" \
              "} \n" \
              "// Fill the dots one after the other with a color \n" \
              "void colorWipe(uint32_t c, uint8_t wait) \n" \
              "{ \n" \
              "for(uint16_t i=0; i<strip.numPixels(); i++) { \n" \
              "strip.setPixelColor(i, c); strip.show(); \n" \
              "delay(wait); \n" \
              "} \n" \
              "} \n" \
              "void rainbow(uint8_t wait) \n" \
              "{ \n" \
              "uint16_t i, j; \n" \
              "for(j=0; j<256; j++) { \n" \
              "for(i=0; i<strip.numPixels(); i++) { \n" \
              "strip.setPixelColor(i, Wheel((i+j) & 255)); \n" \
              "} \n" \
              "strip.show(); \n" \
              "delay(wait); \n" \
              "} \n" \
              "} \n" \
              "void theaterChase(uint32_t c, uint8_t wait) \n" \
              "{ \n" \
              "for (int j=0; j<10; j++) { \n" \
              "//do 10 cycles of chasing \n" \
              "for (int q=0; q < 3; q++) { \n" \
              "for (uint16_t i=0; i < strip.numPixels(); i=i+3) { \n" \
              "strip.setPixelColor(i+q, c); \n" \
              "} \n" \
              "strip.show(); \n" \
              "delay(wait); \n" \
              "for (uint16_t i=0; i < strip.numPixels(); i=i+3) { \n" \
              "strip.setPixelColor(i+q, 0); \n" \
              "} \n" \
              "} \n" \
              "} \n" \
              "}"

filePath = "test.ino"
test = open(filePath, 'w')
test.write(defaultCode)
test.close()

