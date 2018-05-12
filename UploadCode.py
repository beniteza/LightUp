from pathlib import Path
from subprocess import call
import os
def upload():
    path = 'home/ubuntu/sketchbook/'

    dirPath = Path(path)

    if not dirPath.is_file()
        call('mkdir', 'sketchbook')  # Makes directory Assumes it doesn't exist

    call('sudo', 'apt-get', 'update')
    call('sudo', 'apt-get' 'install', 'arduino-mk')
    call('cd', 'sketchbook')

    #COPY BLINKY AND MAKEFILE TO SKETCHBOOK
    file1 = open('UploadTest/Blinky.ino', 'r')
    body1 = file1.read()

    #Poder Set el nombre del file creado cuando se crea en el programa
    name = os.path.basename('UploadTest/Blinky.ino')

    n = 1
    filePath = Path(path + 'Program' + n)

    while filePath.is_file():
        n = n + 1
        filePath = Path(path + 'Program' + n)


    newFile1 = open(filePath, 'w')
    filePath2 = Path(path + 'Makefile')

    if not filePath2.is_file():
        call('touch', 'Makefile')
        file2 = open('UploadTest/MakeFile', 'r')
        body2 = file2.read()
        newFile2 = open(path + 'Makefile', 'w')
        newFile2.write(body2)

    newFile1.write(body1)

    call('mkdir', 'libraries')
    call('make')
    call('make', 'upload', 'clean')



