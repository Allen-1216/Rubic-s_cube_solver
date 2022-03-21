#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
#import numpy as np
# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Initialize the EV3 Brick.
ev3 = EV3Brick()

motorA = Motor(Port.A) #A馬達 正值手臂抬起
motorB = Motor(Port.B) #B馬達 正值底盤順時針轉
motorC = Motor(Port.C) #C馬達 正值顏色手臂後退
ColorSensorS4 = ColorSensor(Port.S4)


cube_x, cube_y, cube_z = 6, 3, 3
cube3d = [[[0 for i in range(cube_z)] for j in range(cube_y)] for k in range(cube_x)]
#cube3d = np.array(cube3d)
print(cube3d)
print()

x, y, z = 0, 0, 0
def scan():
    global x, y, z
    RGB = [0, 0, 0]
    RGB = ColorSensorS4.rgb()
    cube3d[x][y][z] = ColorSensorS4.color()
    if cube3d[x][y][z] == Color.RED:
        if RGB[0] > 50:
            cube3d[x][y][z] = ("Orange")
        else:
            cube3d[x][y][z] = ("RED")
    z += 1
    if z >= 3:
        z = 0
        y += 1
    if y >= 3:
        y = 0
        x += 1
          

 #掃描一面
ev3.speaker.beep()
motorC.run_until_stalled(300,then=Stop.HOLD, duty_limit=None) #後退到最底 1
ev3.speaker.beep()
motorC.run_angle(300, -235*3, then=Stop.HOLD, wait=True) #往前到中間 2
scan()
motorB.run_angle(300, -45*3, then=Stop.HOLD, wait=True)
motorC.run_angle(300, 60*3, then=Stop.HOLD, wait=True) #後退掃描角落的 3
scan()
for r in range (0, 3):
    motorB.run_angle(300, -45*3, then=Stop.HOLD, wait=True)
    motorC.run_angle(300, -30*3, then=Stop.HOLD, wait=True) #前進掃描邊邊中間4、6、8
    scan()
    motorB.run_angle(300, -45*3, then=Stop.HOLD, wait=True)
    motorC.run_angle(300, 30*3, then=Stop.HOLD, wait=True) #後退掃描角落5、7、9
    scan()
motorB.run_angle(300, -45*3, then=Stop.HOLD, wait=True)
motorC.run_angle(300, -30*3, then=Stop.HOLD, wait=True) #前進掃描邊邊中間 10
scan()
motorC.run_until_stalled(300,then=Stop.HOLD, duty_limit=None) #後退到最底 11
ev3.speaker.beep()

print(cube3d)


#wait(5000)
#ev3.screen.clear()