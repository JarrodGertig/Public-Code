from random import *
from time import sleep

grid = []
for i in range(9):
    grid.append([])
    for j in range(9):
        grid[i].append([])
subgrid  = []
subgrid1 = []
subgrid2 = []
subgrid3 = []
subgrid4 = []
subgrid5 = []
subgrid6 = []
subgrid7 = []
subgrid8 = []
subgrid9 = []

def rebuild_subgrids():
    global subgrid1,subgrid2,subgrid3,subgrid4,subgrid5,subgrid6,subgrid7,subgrid8,subgrid9,column1,column2,column3,row1,row2,row3,grid
    subgrid1 = [[grid[0][0:2]],
                [grid[1][0:2]],
                [grid[2][0:2]]]
    subgrid2 = [[grid[0][3:5]],
                [grid[1][3:5]],
                [grid[2][3:5]]]
    subgrid3 = [[grid[0][6:8]],
                [grid[1][6:8]],
                [grid[2][6:8]]]
    subgrid4 = [[grid[3][0:2]],
                [grid[4][0:2]],
                [grid[5][0:2]]]
    subgrid5 = [[grid[3][3:5]],
                [grid[4][3:5]],
                [grid[5][3:5]]]
    subgrid6 = [[grid[3][6:8]],
                [grid[4][6:8]],
                [grid[5][6:8]]]
    subgrid7 = [[grid[6][0:2]],
                [grid[7][0:2]],
                [grid[8][0:2]]]
    subgrid8 = [[grid[6][3:5]],
                [grid[7][3:5]],
                [grid[8][3:5]]]
    subgrid9 = [[grid[6][6:8]],
                [grid[7][6:8]],
                [grid[8][6:8]]]

def diffic(sett):
    if sett > 2:
        print("Mmmm, daring, are we?")
        return [27,3]
    elif sett == 2:
        print("Good luck.")
        return [30,4]
    elif sett == 1:
        print("Have fun!")
        return [33,5]
    elif sett == 0:
        print("Mmmm, wimp, eh? Fine...")
        return [36,6]
    else:
        print("Auto-solving a table for you")
        return [81,10]

def assign_rand(data):
    global grid
    pre_pos,max_type=data[0],data[1]
    while True:
        x=randint(0,8)
        y=randint(0,8)
        num=randint(1,9)
        adder=True
        while incompatible(x,y,num):
            if num<9 and adder:
                num+=1
                adder=True
            elif num>0 and (not adder):
                num-=1
            elif num<=0:
                x=randint(0,8)
                y=randint(0,8)
                num=randint(1,9)
                adder=True
            else:
                adder=False
        if pre_pos>=1:
            if grid[y][x]==[]:
                u=0
                for u in range(num):
                    u+=1
                grid[y][x]=[u]
                pre_pos-=1
        else:
            break

def col_compat(x,v):
    print("checking col "+str(x))
    for i in range(len(grid)):
        if grid[i][x]==[v]:
            return False
        else:
            return True

def row_compat(y,v):
    print("checking row "+str(y))
    for i in range(len(grid[y])):
        if grid[y][i]==[v]:
            return False
        else:
            return True

def sub_compat(x,y,v):
    tempgrid=subgridding(x,y)
    print("checking subgrid")
    for i in range(len(tempgrid)):
        for j in range(len(tempgrid[i])):
            if tempgrid[i][j]==[v]:
                return False
            else:
                return True

def incompatible(x,y,v):
    if col_compat(x,v):
        if row_compat(y,v):
            if sub_compat(x,y,v):
                return False
    return True

def subgridding(x,y):
    return {
        (0,0):subgrid1,
        (0,1):subgrid1,
        (0,2):subgrid1,
        (0,3):subgrid2,
        (0,4):subgrid2,
        (0,5):subgrid2,
        (0,6):subgrid3,
        (0,7):subgrid3,
        (0,8):subgrid3,
        (1,0):subgrid1,
        (1,1):subgrid1,
        (1,2):subgrid1,
        (1,3):subgrid2,
        (1,4):subgrid2,
        (1,5):subgrid2,
        (1,6):subgrid3,
        (1,7):subgrid3,
        (1,8):subgrid3,
        (2,0):subgrid1,
        (2,1):subgrid1,
        (2,2):subgrid1,
        (2,3):subgrid2,
        (2,4):subgrid2,
        (2,5):subgrid2,
        (2,6):subgrid3,
        (2,7):subgrid3,
        (2,8):subgrid3,
        (3,0):subgrid4,
        (3,1):subgrid4,
        (3,2):subgrid4,
        (3,3):subgrid5,
        (3,4):subgrid5,
        (3,5):subgrid5,
        (3,6):subgrid6,
        (3,7):subgrid6,
        (3,8):subgrid6,
        (4,0):subgrid4,
        (4,1):subgrid4,
        (4,2):subgrid4,
        (4,3):subgrid5,
        (4,4):subgrid5,
        (4,5):subgrid5,
        (4,6):subgrid6,
        (4,7):subgrid6,
        (4,8):subgrid6,
        (5,0):subgrid4,
        (5,1):subgrid4,
        (5,2):subgrid4,
        (5,3):subgrid5,
        (5,4):subgrid5,
        (5,5):subgrid5,
        (5,6):subgrid6,
        (5,7):subgrid6,
        (5,8):subgrid6,
        (6,0):subgrid7,
        (6,1):subgrid7,
        (6,2):subgrid7,
        (6,3):subgrid8,
        (6,4):subgrid8,
        (6,5):subgrid8,
        (6,6):subgrid9,
        (6,7):subgrid9,
        (6,8):subgrid9,
        (7,0):subgrid7,
        (7,1):subgrid7,
        (7,2):subgrid7,
        (7,3):subgrid8,
        (7,4):subgrid8,
        (7,5):subgrid8,
        (7,6):subgrid9,
        (7,7):subgrid9,
        (7,8):subgrid9,
        (8,0):subgrid7,
        (8,1):subgrid7,
        (8,2):subgrid7,
        (8,3):subgrid8,
        (8,4):subgrid8,
        (8,5):subgrid8,
        (8,6):subgrid9,
        (8,7):subgrid9,
        (8,8):subgrid9,
        }.get((x,y),subgrid)

def build_Sudoku():
    assign_rand(diffic(difficulty_setting))

print("Enter difficulty Easy(0), Medium(1), Hard(2), or Very Hard(3)")
difficulty_setting=int(input())
rebuild_subgrids()
build_Sudoku()
for i in range(9):
    for j in range(9):
        if grid[i][j]==[]:
            grid[i][j]=[0]
print("Grid:")
for i in range(len(grid)):
    print(grid[i])
        
