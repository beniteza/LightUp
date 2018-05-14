import ply.yacc as yacc
import os
import CodeGenerator as generate


def runParser():
    def p_execute(p):
        '''
        execute : command
                | var_assign
                | empty
        '''
        print(p[1])

    def p_var_assign(p):
        '''
        var_assign : NAME EQUALS color
                   | NAME EQUALS rgb
                   | NAME EQUALS miliseconds
                   | NAME EQUALS animation
                   | NAME EQUALS button_pos
        '''
        p[0] = ('=', p[1], p[3])
        generate.createVariable(p[0])

    def p_command(p):
        '''
        command : ANIMATE animation color miliseconds
                | ANIMATE animation rgb miliseconds
                | START
                | END
        '''
        if p[1] == 'START':
            if os.path.isfile("arduinoCode.ino"):
                os.remove("arduinoCode.ino")
        elif p[1] == 'END':
            generate.upload()
            generate.terminalUpload()
        else:
            p[0] = (p[1], p[2], p[3], p[4])
            generate.animate(p[0])

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
        p[0] = p[1]
        # p[0] = ('var', p[1])

    def p_rgb(p):
      'rgb : LP NUMBER COMA NUMBER COMA NUMBER RP'
      p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + p[6] + p[7]

    def p_rgb_var(p):
        '''
        rgb : NAME
        '''
        p[0] = p[1]
        # p[0] = ('var', p[1])

    def p_miliseconds(p):
        '''
        miliseconds : NUMBER
        '''
        p[0] = p[1]

    def p_miliseconds_var(p):
        '''
        miliseconds : NAME
        '''
        p[0] = p[1]
        # p[0] = ('var', p[1])

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
        p[0] = p[1]
        # p[0] = ('var', p[1])

    def p_animation(p):
      '''
      animation : RAINBOW
                | RAINBOW_CYCLE
                | THEATER_CHASE_RAINBOW
                | COLOR_WIPE
                | THEATER_CHASE
      '''
      p[0] = p[1]

    def p_animation_var(p):
        '''
        animation : NAME
        '''
        p[0] = p[1]
        # p[0] = ('var', p[1])

    def p_empty(p):
        '''
        empty :
        '''
        p[0] = None

    def p_error(p):
        print("Syntax error found!")

    parser = yacc.yacc()

    def translateCode(p):
        try:
            LightUpSource = open(p, 'r')
        except IOError:
            print("Error opening file")
            exit()

        for line in LightUpSource:
            try:
                parser.parse(line)
            except IOError:
                print("Error opening file!")
                exit()

    file = 'LightUpCode.txt'
    translateCode(file)
