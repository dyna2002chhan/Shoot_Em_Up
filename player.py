#IMPORT----------------------------------------------------------------------------------------
from tkinter import *
import random

#CONSTANT----------------------------------------------------------------------------------------
# startcode
root = Tk()

score =0
lives = 3

#VARIABLES----------------------------------------------------------------------------------------
w = 1200
h = 700
x= w//2
y = h//2


#FUNCTION----------------------------------------------------------------------------------------

def left(event):
  x=-10
  y=0
  my_canvas.move(my_circle,x,y)

def right(event):
  x=10 
  y=0
  my_canvas.move(my_circle,x,y)

def up(event):
  x=0
  y= -10
  my_canvas.move(my_circle,x,y)

def down(event):
  x=0
  y=10
  my_canvas.move(my_circle,x,y)


#GRAPHICS----------------------------------------------------------------------------------------
root = Tk()
root.geometry("1200x700")
root.title("SPACE INVADER")


# top = Canvas(root, width=1200, height= 50, bg="blue")
# top.pack(side = top)

#CANVAS
my_canvas =Canvas(root, width=w/3,height= h,bg="blue")
my_canvas.pack(side = LEFT)


my_canvasREd =Canvas(root, width=w,height= h, bg= "purple")
my_canvasREd.pack(side = RIGHT)

# bg = PhotoImage(file= "images//fly.png")
# mybg = my_canvasREd.create_image(0,0,image = bg)

# mybg.pack()
# Amount of killed enemies
scoreLabel=Label(my_canvasREd, text="Kills :" + str(score), bg="white", fg="black", font= 30)
scoreLabel.place(x=720,y=10)

# Amount of player's lives.
livesLabel= Label(my_canvas, text="Lives :" + str(lives), bg="white", fg="black", font= 30)
livesLabel.place(x=20,y=10) 
my_circle = my_canvas.create_oval(x-500,y,x-400,y+50, fill="white") 

#binding
root.bind("<Left>", left)
root.bind("<Right>", right)
root.bind("<Up>", up)
root.bind("<Down>", down)


root.mainloop()