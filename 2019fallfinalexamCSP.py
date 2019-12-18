#2019-20 Fall Computer Science Principles Final Exam

#Ms. Haubold


#Name
#Baraka Kagimbi
#Date
#12/18/19


#### INSTRUCTIONS ####
#Create an etch a sketch turtle game
#The turtle should move with the arrow keys (up, down, left and right), and draw
#Space should clear the screen
#o and p should make the pen size bigger and smaller
#u should pick the pen up or put the pen down
#All code must be commented
#BONUS
#Add a feature to change colors
#

#import required libraries
import turtle as trtl

#create turtle


bk = trtl.Turtle()
#movement functions
def bk_up():
    bk.setheading(90)    #Mmakes the turtle go up
    bk.forward(10)

def bk_down():
    bk.setheading(270)      #Makes the turtle go down
    bk.forward(10)

def bk_right():
    bk.setheading(0)      #make the turtle go right
    bk.forward(10)

def bk_left():
    bk.setheading(180)      #makes the turtle go left
    bk.forward(10)

def bk_space():           #makes the turle drawing be cleared
    bk.clear()

def bk_p():
    bk.pensize(+15)      #increase drawing pen size

def bk_o():
    bk.pensize(1)  #decrease pensize

def bk_u():
    bk.penup()       #was supposed to let you lift up the pen

def bk_q():
    bk.pendown()
    

#color/drawing functions



#create screen

#bind to keypresses
wn = trtl.Screen()
wn.onkeypress(bk_up,"Up")     #binds bk_(put anything here) to a key
wn.onkeypress(bk_down,"Down")
wn.onkeypress(bk_right,"Right")
wn.onkeypress(bk_left,"Left")
wn.onkeypress(bk_space,"space" )
wn.onkeypress(bk_p,"p")
wn.onkeypress(bk_o,"o")
wn.onkeypress(bk_u,"u" )
wn.onkeypress(bk_q,"q" )


#listen

wn.listen()

#mainloop
wn.mainloop()