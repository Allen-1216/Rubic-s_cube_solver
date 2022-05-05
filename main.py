#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import color
#import numpy as np
# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Initialize the EV3 Brick.
ev3 = EV3Brick()

motorA = Motor(Port.A) #A馬達 正值手臂抬起
motorB = Motor(Port.B) #B馬達 正值底盤順時針轉
motorC = Motor(Port.C) #C馬達 正值顏色手臂後退
ColorSensorS4 = ColorSensor(Port.S4)


cube_x, cube_y = 6, 9
cube3d = [[0 for j in range(cube_y)] for k in range(cube_x)] #儲存掃描完顏色的2維陣列
#print(cube3d) #顯示空的陣列 檢查用
print()
simulation_cube3d = cube3d.copy() #複製一個新陣列 模擬方塊當下的狀態
kociemba_cube3d = cube3d.copy() #複製一個新陣列 儲存符合kociemba排列順序

x, y, z = 0, 0, 0
def scan_color(): #讀取單顆顏色
    global x, y
    RGB = [0, 0, 0]
    RGB = ColorSensorS4.rgb()
    cube3d[x][y] = ColorSensorS4.color() #lego掃不到橘色，會把橘當成紅色，所以先把可辨認的顏色排除，留下紅色，再用RGB光反射作區別
    if cube3d[x][y] == Color.RED:
        if RGB[0] > 50:
            cube3d[x][y][z] = Color.ORANGE
        else:
            cube3d[x][y][z] = Color.RED
    y += 1
    if y >= 9:
        y = 0
        x += 1

def scan_plane():#讀取一面的各個顏色
    motorC.run_until_stalled(300,then=Stop.HOLD, duty_limit=None) #後退到最底 1
    motorC.run_angle(300, -235*3, then=Stop.HOLD, wait=True) #往前到中間 2
    scan_color()
    motorB.run_angle(300, -45*3, then=Stop.HOLD, wait=True)#逆時針轉45度
    motorC.run_angle(300, 60*3, then=Stop.HOLD, wait=True) #後退掃描角落的 3
    scan_color()
    for r in range (0, 3):
        motorB.run_angle(300, -45*3, then=Stop.HOLD, wait=True)
        motorC.run_angle(300, -30*3, then=Stop.HOLD, wait=True) #前進掃描邊邊中間4、6、8
        scan_color()
        motorB.run_angle(300, -45*3, then=Stop.HOLD, wait=True)
        motorC.run_angle(300, 30*3, then=Stop.HOLD, wait=True) #後退掃描角落5、7、9
        scan_color()
    motorB.run_angle(300, -45*3, then=Stop.HOLD, wait=True)
    motorC.run_angle(300, -30*3, then=Stop.HOLD, wait=True) #前進掃描邊邊中間 10
    scan_color()
    motorC.run_until_stalled(300,then=Stop.HOLD, duty_limit=None) #後退到最底 11

def roll_cube():#馬達A手臂翻轉方塊&抬起
    motorA.run_angle(250,110) #手臂推放到魔方上
    motorA.run_angle(250, 110)
    motorA.run_angle(250, -110)
    motorA.run_until_stalled(-300,then=Stop.HOLD, duty_limit=None) #手臂抬起



#掃描6面
scan_plane() #掃U

motorB.run_angle(300, 90*3, then=Stop.HOLD, wait=True)#底盤順時針轉90度
roll_cube()
scan_plane() #掃L
motorB.run_angle(300, 90*3, then=Stop.HOLD, wait=True)#底盤順時針轉90度
roll_cube()
scan_plane() #掃F
roll_cube()
scan_plane() #掃R
roll_cube()
scan_plane() #掃B
motorB.run_angle(300, -90*3, then=Stop.HOLD, wait=True)#底盤逆時針轉90度
roll_cube()
scan_plane() #掃D

simulation_cube3d =
str(cube3d[0][7]) + str(cube3d[0][8]) + str(cube3d[0][1]) + str(cube3d[0][6]) + str(cube3d[0][0]) + str(cube3d[0][2]) + str(cube3d[0][5]) + str(cube3d[0][4]) + str(cube3d[0][3])
+str(cube3d[1][3]) + str(cube3d[1][4]) + str(cube3d[1][5]) + str(cube3d[1][2]) + str(cube3d[1][0]) + str(cube3d[1][6]) + str(cube3d[1][1]) + str(cube3d[1][8]) + str(cube3d[1][7])
+str(cube3d[2][5]) + str(cube3d[2][6]) + str(cube3d[2][7]) + str(cube3d[2][4]) + str(cube3d[2][0]) + str(cube3d[2][8]) + str(cube3d[2][3]) + str(cube3d[2][2]) + str(cube3d[2][1])
+str(cube3d[3][5]) + str(cube3d[3][6]) + str(cube3d[3][7]) + str(cube3d[3][4]) + str(cube3d[3][0]) + str(cube3d[3][8]) + str(cube3d[3][3]) + str(cube3d[3][2]) + str(cube3d[3][1])
+str(cube3d[4][5]) + str(cube3d[4][6]) + str(cube3d[4][7]) + str(cube3d[4][4]) + str(cube3d[4][0]) + str(cube3d[4][8]) + str(cube3d[4][3]) + str(cube3d[4][2]) + str(cube3d[4][1])
+str(cube3d[5][7]) + str(cube3d[5][8]) + str(cube3d[5][1]) + str(cube3d[5][6]) + str(cube3d[5][0]) + str(cube3d[5][2]) + str(cube3d[5][5]) + str(cube3d[5][4]) + str(cube3d[5][3])

kociemba_cube3d =
str(cube3d[0][7]) + str(cube3d[0][8]) + str(cube3d[0][1]) + str(cube3d[0][6]) + str(cube3d[0][0]) + str(cube3d[0][2]) + str(cube3d[0][5]) + str(cube3d[0][4]) + str(cube3d[0][3])
+str(cube3d[3][5]) + str(cube3d[3][6]) + str(cube3d[3][7]) + str(cube3d[3][4]) + str(cube3d[3][0]) + str(cube3d[3][8]) + str(cube3d[3][3]) + str(cube3d[3][2]) + str(cube3d[3][1])
+str(cube3d[2][5]) + str(cube3d[2][6]) + str(cube3d[2][7]) + str(cube3d[2][4]) + str(cube3d[2][0]) + str(cube3d[2][8]) + str(cube3d[2][3]) + str(cube3d[2][2]) + str(cube3d[2][1])
+str(cube3d[5][7]) + str(cube3d[5][8]) + str(cube3d[5][1]) + str(cube3d[5][6]) + str(cube3d[5][0]) + str(cube3d[5][2]) + str(cube3d[5][5]) + str(cube3d[5][4]) + str(cube3d[5][3])
+str(cube3d[1][3]) + str(cube3d[1][4]) + str(cube3d[1][5]) + str(cube3d[1][2]) + str(cube3d[1][0]) + str(cube3d[1][6]) + str(cube3d[1][1]) + str(cube3d[1][8]) + str(cube3d[1][7])
+str(cube3d[4][5]) + str(cube3d[4][6]) + str(cube3d[4][7]) + str(cube3d[4][4]) + str(cube3d[4][0]) + str(cube3d[4][8]) + str(cube3d[4][3]) + str(cube3d[4][2]) + str(cube3d[4][1])

print(kociemba_cube3d)
print()
print(simulation_cube3d)
print()

#wait(5000)
#ev3.screen.clear()