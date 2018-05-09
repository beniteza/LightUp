import ply.lex as lex
import ply.yacc as yacc
import sys

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
    # Variable Name
    'NAME'
]

t_NUMBER = r'[0-9]+'
t_LP = r'\('
t_RP = r'\)'
t_COMA = r'\,'
t_EQUALS = r'\='
t_ignore = ' \t\n'

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

# lexer.input("ANIMATE (RAINBOW YELLOW 50)")
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
    '''
    p[0] = ('=', p[1], p[3])

def p_command(p):
    '''
    command : ANIMATE animation color miliseconds
            | ANIMATE animation rgb miliseconds
    '''
    p[0] = (p[1], p[2], p[3], p[4])

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

while True:
    try:
        s = input('>>')
    except EOFError:
        break
    parser.parse(s)