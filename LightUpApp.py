import LightUp as App
import time

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
