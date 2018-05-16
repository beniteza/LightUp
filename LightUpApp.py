import LightUp as App
import time

#   SPRING 2018 PL PROJECT
#
#   AXVIEL BENITEZ
#   JUAN AGOSTO
#   EDUARDO PEREZ
#   CRISTIAN ROSADO

print("Running LightUp\n")
time.sleep(0.25)
print("Processing Code...\n")
time.sleep(0.25)

file = 'LightUpCode.txt'

try:
    App.translateCode(file)
    time.sleep(5)
    print("Arduino file succesfully writen and uploaded!\n")
except:
    print("Errors were encountered\n")
