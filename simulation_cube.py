
class Cube:
    def __init__(self,cube):
        self.cube = cube

    def faceMove(self, x): #面順轉
        self.cube[x][0], self.cube[x][6], self.cube[x][8], self.cube[x][2] = self.cube[x][6], self.cube[x][8], self.cube[x][2], self.cube[x][0]
        self.cube[x][1], self.cube[x][7], self.cube[x][5], self.cube[x][3] = self.cube[x][3], self.cube[x][5], self.cube[x][1], self.cube[x][7]
        return

    def faceMove_reverse(self, x): #面逆轉
        self.cube[x][0], self.cube[x][2], self.cube[x][8], self.cube[x][6] = self.cube[x][2], self.cube[x][8], self.cube[x][6], self.cube[x][0]
        self.cube[x][1], self.cube[x][3], self.cube[x][5], self.cube[x][7] = self.cube[x][5], self.cube[x][1], self.cube[x][7], self.cube[x][3]
        return

    def swap(self, x1, x2, x3, x4, y1, y2, y3, y4): #4顆顏色交換
        self.cube[x1][y1], self.cube[x2][y2], self.cube[x3][y3], self.cube[x4][y4] = self.cube[x2][y2], self.cube[x3][y3], self.cube[x4][y4], self.cube[x1][y1]
    
    def roll(self): #拉推模擬
        self.faceMove_reverse(2)
        self.faceMove_reverse(4)
        self.swap(1, 0, 3, 5, 6, 0, 2, 8)
        self.swap(1, 0, 3, 5, 7, 3, 1, 5)
        self.swap(1, 0, 3, 5, 8, 6, 0, 2)
        self.swap(1, 0, 3, 5, 3, 1, 5, 7)
        self.swap(1, 0, 3, 5, 4, 4, 4, 4)
        self.swap(1, 0, 3, 5, 5, 7, 3, 1)
        self.swap(1, 0, 3, 5, 0, 2, 8, 6)
        self.swap(1, 0, 3, 5, 1, 5, 7, 3)
        self.swap(1, 0, 3, 5, 2, 8, 6, 0)

    def baseMove(self): #底盤順轉模擬 90度為一單位
        self.faceMove(0)
        self.faceMove(5)
        self.swap(1, 2, 3, 4, 0, 0, 0, 0)
        self.swap(1, 2, 3, 4, 1, 1, 1, 1)
        self.swap(1, 2, 3, 4, 2, 2, 2, 2)
        self.swap(1, 2, 3, 4, 3, 3, 3, 3)
        self.swap(1, 2, 3, 4, 4, 4, 4, 4)
        self.swap(1, 2, 3, 4, 5, 5, 5, 5)
        self.swap(1, 2, 3, 4, 6, 6, 6, 6)
        self.swap(1, 2, 3, 4, 7, 7, 7, 7)
        self.swap(1, 2, 3, 4, 8, 8, 8, 8)

    def baseMove_reverse(self): #底盤逆轉模擬 90度為一單位
        self.faceMove_reverse(0)
        self.faceMove_reverse(5)
        self.swap(4, 3, 2, 1, 0, 0, 0, 0)
        self.swap(4, 3, 2, 1, 1, 1, 1, 1)
        self.swap(4, 3, 2, 1, 2, 2, 2, 2)
        self.swap(4, 3, 2, 1, 3, 3, 3, 3)
        self.swap(4, 3, 2, 1, 4, 4, 4, 4)
        self.swap(4, 3, 2, 1, 5, 5, 5, 5)
        self.swap(4, 3, 2, 1, 6, 6, 6, 6)
        self.swap(4, 3, 2, 1, 7, 7, 7, 7)
        self.swap(4, 3, 2, 1, 8, 8, 8, 8)

def move(cube, m, x):
    # Need to do 3 swaps based on the move
    if (m == 'U'):
        cube.faceMove(x)
        cube.swap(1, 2, 3, 4, 0, 0, 0, 0)
        cube.swap(1, 2, 3, 4, 1, 1, 1, 1)
        cube.swap(1, 2, 3, 4, 2, 2, 2, 2)
    elif (m == "U'"):
        cube.faceMove_reverse(x)
        cube.swap(1, 4, 3, 2, 0, 0, 0, 0)
        cube.swap(1, 4, 3, 2, 1, 1, 1, 1)
        cube.swap(1, 4, 3, 2, 2, 2, 2, 2)
    elif (m == 'U2'):
        move(cube, 'U', x)
        move(cube, 'U', x)
    elif (m == 'D'):
        cube.faceMove(x)
        cube.swap(4, 3, 2, 1, 6, 6, 6, 6)
        cube.swap(4, 3, 2, 1, 7, 7, 7, 7)
        cube.swap(4, 3, 2, 1, 8, 8, 8, 8)
    elif (m == "D'"):
        cube.faceMove_reverse(x)
        cube.swap(1, 2, 3, 4, 6, 6, 6, 6)
        cube.swap(1, 2, 3, 4, 7, 7, 7, 7)
        cube.swap(1, 2, 3, 4, 8, 8, 8, 8)
    elif (m == 'D2'):
        move(cube, 'D', x)
        move(cube, 'D', x)
    elif (m == 'R'):
        cube.faceMove(x)
        cube.swap(0, 2, 5, 4, 2, 2, 2, 6)
        cube.swap(0, 2, 5, 4, 5, 5, 5, 3)
        cube.swap(0, 2, 5, 4, 8, 8, 8, 0)
    elif (m == "R'"):
        cube.faceMove_reverse(x)
        cube.swap(5, 2, 0, 4, 2, 2, 2, 6)
        cube.swap(5, 2, 0, 4, 5, 5, 5, 3)
        cube.swap(5, 2, 0, 4, 8, 8, 8, 0)
    elif (m == 'R2'):
        move(cube, 'R', x)
        move(cube, 'R', x)
    elif (m == 'L'):
        cube.faceMove(x)
        cube.swap(0, 4, 5, 2, 6, 8, 6, 6)
        cube.swap(0, 4, 5, 2, 3, 5, 3, 3)
        cube.swap(0, 4, 5, 2, 0, 2, 0, 0)
    elif (m == "L'"):
        cube.faceMove_reverse(x)
        cube.swap(5, 4, 0, 2, 6, 8, 6, 6)
        cube.swap(5, 4, 0, 2, 3, 5, 3, 3)
        cube.swap(5, 4, 0, 2, 0, 2, 0, 0)
    elif (m == 'L2'):
        move(cube, 'L', x)
        move(cube, 'L', x)
    elif (m == 'F'):
        cube.faceMove(x)
        cube.swap(0, 1, 5, 3, 8, 2, 0, 6)
        cube.swap(0, 1, 5, 3, 7, 5, 1, 3)
        cube.swap(0, 1, 5, 3, 6, 8, 2, 0)
    elif (m == "F'"):
        cube.faceMove_reverse(x)
        cube.swap(0, 3, 5, 1, 8, 6, 0, 2)
        cube.swap(0, 3, 5, 1, 7, 3, 1, 5)
        cube.swap(0, 3, 5, 1, 6, 0, 2, 8)
    elif (m == 'F2'):
        move(cube, 'F', x)
        move(cube, 'F', x)
    elif (m == 'B'):
        cube.faceMove(x)
        cube.swap(0, 3, 5, 1, 0, 2, 8, 6)
        cube.swap(0, 3, 5, 1, 1, 5, 7, 3)
        cube.swap(0, 3, 5, 1, 2, 8, 6, 0)
    elif (m == "B'"):
        cube.faceMove_reverse(x)
        cube.swap(0, 1, 5, 3, 0, 6, 8, 2)
        cube.swap(0, 1, 5, 3, 1, 3, 7, 5)
        cube.swap(0, 1, 5, 3, 2, 0, 6, 8)
    elif (m == 'B2'):
        move(cube, 'B', x)
        move(cube, 'B', x)


