# #IMPORT -----------------------------------------------------------------------------

# from tkinter import *
# import tkinter as tk
# import random

# #VARIABLES---------------------------------------------------------------------------

# w = 1200
# h = 700
# x= w//2
# y = h//2

# #CONSTANT----------------------------------------------------------------------------


# root= tk.Tk()
# root.title("cute")
# root.geometry("1300x800")
# canvas=tk.Canvas(root)
# score =0
# lives = 3

# #GRAPHIC------------------------------------------------------------------------------

# bg = tk.PhotoImage(file="spacebac.png")
# background = canvas.create_image(650,400,image=bg)
# root.title("SPACE INVADER")

# # Amount of killed enemies
# scoreLabel=Label(root, text="Kills :" + str(score), bg="white", fg="black", font= 50)
# scoreLabel.place(x=1220,y=20)

# # Amount of player's lives.
# livesLabel= Label(root, text="Lives :" + str(lives), bg="white", fg="black", font= 50)
# livesLabel.place(x=20,y=20) 
# # Create bullet
# bullets = tk.PhotoImage(file="missile.png")


# plane= tk.PhotoImage(file="spaceship.png")
# airplane_fly = canvas.create_image(100,y+40,image=plane) 


# # enemy
# planes= tk.PhotoImage(file="1enemy.png")
# my_circles= canvas.create_image(1100,y-200,image=planes) 

# plans= tk.PhotoImage(file="2enemy.png")
# my_circles= canvas.create_image(1100,y,image=plans) 

# # FUNCTIONS-------------------------------------------------------------------------

# def missile():

#     global leftBullet, rightBullet, middleBullet
#     canvas.move(leftBullet,30,0)
#     canvas.move(rightBullet, 35, 0)
#     canvas.move(middleBullet,40, 0)
#     myY = canvas.coords(leftBullet)[1]
#     Shooting = myY <= 0
    
#     if not Shooting:
#         canvas.after(60, lambda:missile())
#     else:
#         canvas.delete(leftBullet)
#         canvas.delete(rightBullet)
#         canvas.delete(middleBullet)
#         Shoot()


# def Shoot():

#     global airplane_fly, leftBullet, rightBullet,middleBullet
#     X1 = canvas.coords(airplane_fly)[0]
#     Y1 = canvas.coords(airplane_fly)[1]
#     leftBullet = canvas.create_image(X1 +120, Y1 -20, image = bullets)
#     middleBullet = canvas.create_image(X1 +150, Y1 , image = bullets)
#     rightBullet = canvas.create_image(X1 + 120, Y1 +20, image = bullets)
#     missile()
# # function move

# def moveLeft(event):
#     if canvas.coords(airplane_fly)[0] > 100:
#         canvas.move(airplane_fly, -20, 0)

# def moveRight(event):
#     if canvas.coords(airplane_fly)[0] < 1200:
#         canvas.move(airplane_fly, 20, 0)

# def moveUp(event):  
#     if canvas.coords(airplane_fly)[1] > 50:
#         canvas.move(airplane_fly, 0, -20)

# def moveDown(event):
#     if canvas.coords(airplane_fly)[1] < 750:
#         canvas.move(airplane_fly, 0, 20)

# #BINDING------------------------------------------------------------------------------

# Shoot()      
# root.bind_all("<Left>", moveLeft) 
# root.bind_all("<Right>", moveRight)
# root.bind("<Up>", moveUp)
# root.bind("<Down>", moveDown)

# canvas.pack(expand=True,fill="both")
# root.resizable(True,True)

# root.mainloop() 
# Import module  
from tkinter import *
  
# Create object  
root = Tk() 
wallImage = PhotoImage(file="best.png")
wallImageHeight = wallImage.height()
wallImageWidth = wallImage.width()  
# ENEMY
enemyImage=PhotoImage(file="testenemy.png")
# PLAYER
playerImage=PhotoImage(file="testplayer.png")
#Bullets
bullet=True
#ARRAY2D
array=[
    ["w","w","w","W","w","w","W","w","w","W","w","w","w","w","w","w"],
    ["W","0","0","0","0","0","0","0","0","0","0","0","0","0","0","w"],
    ["W","0","0","0","0","E","0","0","0","0","0","0","0","0","0","w"],
    ["W","0","0","0","w","w","w","0","0","0","0","0","0","0","0","w"],
    ["W","0","0","0","0","0","0","0","0","E","0","0","0","0","0","w"],
    ["W","0","0","0","0","0","0","0","w","w","0","0","0","0","0","w"],
    ["W","0","0","0","0","0","0","0","0","0","0","0","0","0","0",'w'],
    ["W","0","0","0","0","0","0","0","0","0","0","0","0","0","E",'w'],
    ["W","P","0","0","0","0","0","0","0","0","0","0","0","w","w",'w'],
    ["w","w","w","W","w","w","W","w","w","W","w","w","w","w","w",'w']
]

positionPlayer = []

screenHeight = wallImageHeight*len(array)
screenWidth = wallImageWidth*len(array[0])
print(screenWidth, screenHeight)

root.geometry = (str(screenHeight)+"x"+str(screenWidth))
# Create Canvas 
canvas = Canvas( root, width =screenWidth, height = screenHeight) 
canvas.pack(fill = "both", expand = True) 


# TESTING ARRAY2D
def playerRight(event):
    global array, positionPlayer
    position = []
    for n in range(len(array)):
        for index in  range(len(array[n])):
            if array[n][index]  == "P":
                position.append(index)
                position.append(n)
    if array[position[1]][position[0]+1] == "0":
        array[position[1]][position[0]+1] = "P"
        array[position[1]][position[0]] = "0"
    canvas.delete("player")
    for row in range(len(array)):
        for col in range(len(array[row])):
            if array[row][col]=="w" or array[row][col]=="W":
                canvas.create_image(wallImageWidth*col + wallImageWidth/2, wallImageHeight*row+wallImageHeight/2, image = wallImage)
            if array[row][col]=="E":
                canvas.create_image(wallImageWidth*col + wallImageWidth/2, wallImageHeight*row+wallImageHeight/2, image = enemyImage)
            if array[row][col]=="P":
                canvas.create_image(wallImageWidth*col + wallImageWidth/2, wallImageHeight*row+wallImageHeight/2, image = playerImage, tags="player")

def playerLeft(event):
    global array, positionPlayer
    position = []
    for n in range(len(array)):
        for index in  range(len(array[n])):
            if array[n][index]  == "P":
                position.append(index)
                position.append(n)
    if array[position[1]][position[0]-1] == "0":
        array[position[1]][position[0]-1] = "P"
        array[position[1]][position[0]] = "0"
    canvas.delete("player")
    for row in range(len(array)):
        for col in range(len(array[row])):
            if array[row][col]=="w" or array[row][col]=="W":
                canvas.create_image(wallImageWidth*col + wallImageWidth/2, wallImageHeight*row+wallImageHeight/2, image = wallImage)
            if array[row][col]=="E":
                canvas.create_image(wallImageWidth*col + wallImageWidth/2, wallImageHeight*row+wallImageHeight/2, image = enemyImage)
            if array[row][col]=="P":
                canvas.create_image(wallImageWidth*col + wallImageWidth/2, wallImageHeight*row+wallImageHeight/2, image = playerImage, tags="player")

def playerUp(event):
    global array, positionPlayer
    position = []
    for n in range(len(array)):
        for index in  range(len(array[n])):
            if array[n][index]  == "P":
                position.append(index)
                position.append(n)
    if array[position[1]-1][position[0]] == "0":
        array[position[1]-1][position[0]] = "P"
        array[position[1]][position[0]] = "0"
    canvas.delete("player")
    for row in range(len(array)):
        for col in range(len(array[row])):
            if array[row][col]=="w" or array[row][col]=="W":
                canvas.create_image(wallImageWidth*col + wallImageWidth/2, wallImageHeight*row+wallImageHeight/2, image = wallImage)
            if array[row][col]=="E":
                canvas.create_image(wallImageWidth*col + wallImageWidth/2, wallImageHeight*row+wallImageHeight/2, image = enemyImage)
            if array[row][col]=="P":
                canvas.create_image(wallImageWidth*col + wallImageWidth/2, wallImageHeight*row+wallImageHeight/2, image = playerImage, tags="player")

def playerDown(event):
    global array, positionPlayer
    position = []
    for n in range(len(array)):
        for index in  range(len(array[n])):
            if array[n][index]  == "P":
                position.append(index)
                position.append(n)
    if array[position[1]+1][position[0]] == "0":
        array[position[1]+1][position[0]] = "P"
        array[position[1]][position[0]] = "0"
    canvas.delete("player")
    for row in range(len(array)):
        for col in range(len(array[row])):
            if array[row][col]=="w" or array[row][col]=="W":
                canvas.create_image(wallImageWidth*col + wallImageWidth/2, wallImageHeight*row+wallImageHeight/2, image = wallImage)
            if array[row][col]=="E":
                canvas.create_image(wallImageWidth*col + wallImageWidth/2, wallImageHeight*row+wallImageHeight/2, image = enemyImage)
            if array[row][col]=="P":
                canvas.create_image(wallImageWidth*col + wallImageWidth/2, wallImageHeight*row+wallImageHeight/2, image = playerImage, tags="player")

def drawGrid():
    global array, wallImage, positionPlayer
    canvas.create_image( 0, 0, image = bg, anchor = "nw") 
    for row in range(len(array)):
        for col in range(len(array[row])):
            if array[row][col]=="w" or array[row][col]=="W":
                canvas.create_image(wallImageWidth*col + wallImageWidth/2, wallImageHeight*row+wallImageHeight/2, image = wallImage)
            if array[row][col]=="E":
                canvas.create_image(wallImageWidth*col + wallImageWidth/2, wallImageHeight*row+wallImageHeight/2, image = enemyImage)
            if array[row][col]=="P":
                canvas.create_image(wallImageWidth*col + wallImageWidth/2, wallImageHeight*row+wallImageHeight/2, image = playerImage, tags="player")
            positionPlayer.append(wallImageWidth*col + wallImageWidth/2)
            positionPlayer.append(wallImageHeight*row+wallImageHeight/2)


def createBullet(event):
    

## #Function

def remove(event):
    canvas.delete("remove")
    canvas.delete("delete")
    canvas.move("welcome", 0, 100)


def startNew(event):
    canvas.delete("all")
    drawGrid()
    # canvas.create_rectangle(0, 0, 1000, 600, fill="white", tags="remove")



def quitNew(event):
    canvas.move("welcome", 0, -100)
    canvas.create_rectangle(300, 100, 700, 500, fill="white", tags="delete")
    canvas.create_text(680, 120, text = "X", fill="black", font="Times 25 italic bold", tags="remove")
    canvas.create_text(350, 130, anchor=W, font="Purisa",text="Quit Game")

#Function move player
# def moveUp():
    
# Add image file 
bg = PhotoImage(file = "bg.png")


# Display image 
canvas.create_image( 0, 0, image = bg, anchor = "nw") 

# Add Text 
canvas.create_text(500, 150, text = "Start game!!!", fill="white", font="Times 35 italic bold", tags="welcome")

#Button START
canvas.create_rectangle(430, 220, 610, 280, fill="white", tags="start")
canvas.create_text(515, 250, text = "Start", fill="black", font="Times 35 italic bold", tags="start")
canvas.tag_bind("start", "<Button-1>", startNew)
#Button QUIT

canvas.create_rectangle(430, 420, 610, 480, fill="white", tags="quit")
canvas.create_text(515, 450, text = "Quit", fill="black", font="Times 35 italic bold", tags="quit")
canvas.tag_bind("quit", "<Button-1>", quitNew)

canvas.tag_bind("remove", "<Button-1>", remove)

#BUTTON FOR MOVE PLAYER
root.bind("<Right>", playerRight)
root.bind("<Left>", playerLeft)
root.bind("<Up>", playerUp)
root.bind("<Down>", playerDown)
root.bind("<Enter>",moveBullet)

# Display root 
root.mainloop()
