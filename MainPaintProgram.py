#Paint Program
#By: Andre Tran

"""
#############################################################################################################################
#############################################################################################################################
###########################|----------------------|##########################################################################
###########################|    Paint Program     |##########################################################################
###########################|----------------------|##########################################################################
#############################################################################################################################
#############################################################################################################################
"""

"""
#############################################################################################################################
############################ Tips and Things to Remember ####################################################################
#############################################################################################################################
"""

#-> screen.subsurface(rect).copy() ----> copies a an area listed inside the rectangle

#-> Screen.get_at((mx,my)) ----> gets the RGB colour value at a specific point (like the mouse)

#-> Certain file types for pictures support transparancy, .png is an example of one.  Jpeg does not support transparancy.

#-> If making a toggle between more than 2 things with the same Key, use 'time.wait(150)' to make sure that the program
#   does not register the key more than once when pressed

#-> Globaling a variable in a function allows for changes to that variable in the whole program, so other functions can
#   use it while passing it through peramaters (making it local) is like making a copy of the same variable that exists
#   only inside the function and will not do any changes to the original variable that the whole program uses, but
#   try not to global as much and sometimes use the "return....." to return something as a variable.

#-> Good to pass functions through perameters so it's easier to understand what the function uses.

#-> Round Spraypaint ----> use the circle formula and check if the value is outside of the circle
#   Ex. (mx-dotx)**2+(my-doty)**2<=spraysize**2  ---> mx and my is centre

#-> Always use dividers in a big program (like the green section divider) either by using quotes or ###'s
#   this will help simplify finding things in your program much simplier.  Use multi-line dividers as Main Section
#   dividers while single-line ones are for subdividing

#-> May be a good idea to make the main loop into a drawScene function so the Real main loop is much more simple
#   and can do other important functions like finding the position of the mouse.

#-> When using screen.copy() function with the screen.blit function, make sure to put it into all functions that changes
#   the screen so that it doesn't revert to the previous screen in other parts of the program.

#-> When making a program, make sure the size of the program is not so large that it can't fit on school monitors

"""
#############################################################################################################################
############################ Keyboard Controls ##############################################################################
#############################################################################################################################
"""

#Key F5 exits the program
#Keys 1,2,3,4,5,6,7,8,9,0 are tools
#1=Pencil, 2=Eraser, 3=Paintbrush, 4=Paintbucket, 5=Spraypaint, 6=Eye Dropper, 7=Line Tool, 8=Rectangle Tool
#9=Oval Tool, 0=Selector Tool
#Key C changes the colour selecter from one to the other
#Key F1 clears the whole canvas back to white
#Key Left Shift changes the current option to the next one

"""
#############################################################################################################################
############################ Instructions ###################################################################################
#############################################################################################################################
"""

print """
Welcome to Andre Tran's Paint!!

############################################################
########## Controls ########################################
############################################################

Key F5 exits the program

Keys 1,2,3,4,5,6,7,8,9,0 are tools
1=Pencil, 2=Eraser, 3=Paintbrush, 4=Paintbucket, 5=Spraypaint, 6=Eye Dropper, 7=Line Tool, 8=Rectangle Tool
9=Oval Tool, 0=Selector Tool

Key C changes the colour selecter from one to the other

Key F1 clears the whole canvas back to white

Key Left Shift changes the current option to the next one

############################################################
########## Tools ###########################################
############################################################

Pencil - Left click on the canvas to draw with a pencil
Eraser - Left click on the canvas to erase things
Paintbrush - Left click on the canvas to draw paint strokes
Spraypaint - Left click on the canvas to create a spray effect
Eye Dropper - Left click on a certain colour on the canvas to get that colour for drawing
Line Tool - Left click and hold to draw a straight line from where you held the mouse to where you released it
Rectangle Tool - Left click and hold to draw a rectangle from where you held the mouse to where you released it
Oval Tool - Left click and hold to draw an oval from where you held the mouse to where you released it
Selector Tool - Left click and hold to make a selection by making a rectangle.  After making the selection, left click and
                hold on the highlighted rectangle to move it.  Left click outside of the highlighted rectangle to stop
                the selection
Stamps - After clicking on one of the stamps pictures, left click and hold on the canvas to display the stamp, release to
         finalize the stamp
                
############################################################
########## Colours #########################################
############################################################

-Left click anywhere on the colour grid on the bottom left to get the colour that you clicked on
-Change the colour in use to the second colour by clicking the unhighlighted colour rectangle on the far left side of the program

############################################################
########## Other Things ####################################
############################################################

-Change tools by clicking on the tool buttons on the left side of the program
-Pick the stamps by clicking on the stamps near the bottom of the program
-To save the picture on the canvas, left click on the save button on the bottom right of the program.  Then type the file name.
 The shift key can be used to toggle between capital letters.  Press the Enter key to save the file.  All files are saved as a
 bitmap file.
-To load the picture on the canvas, left click on the load button on the bottom right of the program.  Then type the file name,
 including the file extension.  The shift key can be used to toggle between capital letters.  Press the Enter key to load the file.
-Left click on the Clear button on the top right of the program to clear the canvas to a completely white screen.

############################################################
########## Created by: Andre Tran ##########################
############################################################


"""

"""
#############################################################################################################################
#############################################################################################################################
#######################--------------------##################################################################################
####################### The Actual Program ##################################################################################
#######################--------------------##################################################################################
#############################################################################################################################
#############################################################################################################################
"""

from pygame import *
from random import *
from colours import *

init()
size=width,height=1000,700
screen=display.set_mode(size)

"""
#############################################################################################################################
##### Some Variables ########################################################################################################
#############################################################################################################################
"""

LeftToolBarY=[]         #a list to hold all the Y coordinates of the Left toolbar
RightToolBarY=[]        #a list to hold all the Y coordinates of the Right toolbar
SizeMenuBarY=[]         #a list to hold all the Y coordinates of the size menu
tool="Pencil"           #makes the default tool pencil
oldx=oldy=0
mhold="up"              #makes the default status of the mouse as up (meaning the left click on the mouse is not held)
loadbox=Rect(890,592,100,45)
savebox=Rect(890,648,100,45)
StampX=[]               #a list to hold all the X coordinates of the stamp boxes       

"""
########## Colour Variables #################################################################################################
"""

colour=black        #sets the colour in use to black
colourswitch=0      #sets the default colour in use as colour1
colour1=black       #colour1 is black
colour2=gray77      #colour2 is gray

"""
########## Text Variables/Setup #############################################################################################
"""

saveloadfont=font.SysFont("Arial",30,True,True)             #makes the fonts and sizes
saveboxfont=font.SysFont("Arial",18,True,True)
loadboxfont=font.SysFont("Arial",16,True,True)
filenamefont=font.SysFont("Arial",22,True,True)
loadtextpic=saveloadfont.render("Load",False,(0,0,0))       #makes the text picture
savetextpic=saveloadfont.render("Save",False,(0,0,0))
clearfont=font.SysFont("Arial",24,True,True)
cleartextpic=clearfont.render("Clear",False,(0,0,0))
saveinstruction=saveboxfont.render("Enter the file name to save ('Return' - Enter, 'ESC' - Quit, 'Left Shift' - CAPS): ",False,(0,0,0))
loadinstruction=loadboxfont.render("Enter the file name to load w/ the extension ('Return' - Enter, 'ESC' - Quit, 'Left Shift' - CAPS): ",False,(0,0,0))

"""
########## Options Variables ################################################################################################
"""

optionswitch=0
OSactivate=0
optionsrect1=Rect(150,30,100,45)
optionsrect2=Rect(150,84,100,45)
optionsrect3=Rect(150,138,100,45)

"""
#############################################################################################################################
##### Size/Fill Variables ###################################################################################################
#############################################################################################################################
"""

pencilsize=1                #default size of all the different options (lowest setting)
brushsize=8
spraysize=12
erasersize=10
rectfill=0

"""
#############################################################################################################################
##### Load Images ###########################################################################################################
#############################################################################################################################
"""

backgroundpic=image.load("background.png")
flowerpic=image.load("flower2.png")
vinepic=image.load("vine.png")
vinelongpic=image.load("vinelong.png")
colourgrid=image.load("colourgrid.bmp")             #this section loads all the images
pencilpic=image.load("pencil.bmp")
eraserpic=image.load("eraser.bmp")
paintbrushpic=image.load("paintbrush.bmp")
paintbucketpic=image.load("paintbucket.bmp")
spraypaintpic=image.load("spraypaint.bmp")
eyedropperpic=image.load("eyedropper.bmp")
spraypaints1pic=image.load("spraypaints1.png")
spraypaints2pic=image.load("spraypaints2.png")
spraypaints3pic=image.load("spraypaints3.png")
recttoolpic=image.load("recttool.png")
ovaltoolpic=image.load("ovaltool.png")
linetoolpic=image.load("linetool.png")
selectortoolpic=image.load("selectortool.png")
brianpbjpic=image.load("brianpbj.png")
evilmonkeypic=image.load("evilmonkey.png")
konpic=image.load("kon.png")
lightningmcqueenpic=image.load("lightningmcqueen.png")
pikachupic=image.load("pikachu.png")
pooppic=image.load("poop.png")

"""
#############################################################################################################################
##### Menu Setup ############################################################################################################
#############################################################################################################################
"""

screen.blit(backgroundpic,(0,0))
optionsbackrect=screen.subsurface(Rect(143,22,114,168)).copy()      #makes the picture for the background of the options menu for the nooptions function
canvas=[270,60,720,520]              #dimensions of the canvas
Rectcanvas=Rect(canvas)             #makes the canvas into a Rect
draw.rect(screen,black,Rect(canvas[0]-3,canvas[1]-3,canvas[2]+5,canvas[3]+5),4)    #draws black highlight for the canvas
draw.rect(screen,white,canvas)      #draws the canvas

screen.blit(vinepic,Rect(0,0,290,22))      #blits the vine picture above the tool area
screen.blit(vinelongpic,Rect(255,675,320,22))   #blits the vine picture at the bottom of the program
screen.blit(vinelongpic,Rect(565,675,320,22))   #blits the vine picture at the bottom of the program
screen.blit(flowerpic,Rect(625,1,250,55))  #blits the flower picture beside the title


ccrect=Rect(5,30,20,495)
ccrect1=Rect(5,30,20,247)
ccrect2=Rect(5,277,20,248)
draw.rect(screen,colour1,ccrect1)          #draws the current colour1 indicator box
draw.rect(screen,colour2,ccrect2)         #draws the current colour2 indicator box
draw.rect(screen,green,ccrect1,5)       #draws the first highlight for the first colour
draw.rect(screen,white,Rect(3,28,24,499),3)  #draws highlight for the current colour indicator

colourrect=Rect(6,540,244,150)
screen.blit(colourgrid,colourrect)  #blits the colour grid onto the screen
draw.rect(screen,black,Rect(3,537,249,155),4) #draws highlight around the colour grid to indicate the colour chosen

draw.rect(screen,gray90,loadbox)   #draws the load image box
screen.blit(loadtextpic,Rect(910,592,80,45))    #blits the "Load" text
draw.rect(screen,black,Rect(888,590,104,49),3)  #draws the load image box highlight
draw.rect(screen,gray90,savebox)   #draws the save image box
screen.blit(savetextpic,Rect(910,648,80,45))    #blits the "Save" text
draw.rect(screen,black,Rect(888,646,104,49),3)  #draws the save image box highlight

draw.rect(screen,gray90,Rect(890,10,100,35))    #draws the gray box for the clear option
draw.rect(screen,black,Rect(890,10,100,35),3)   #draws the highlight for the gray box
screen.blit(cleartextpic,(915,10))          #blits the words "Clear" onto the box

"""
#############################################################################################################################
##### Toolbar/Menu ##########################################################################################################
#############################################################################################################################
"""

for y in range(30,520,85):     #draws left toolbar
    draw.rect(screen,gray90,Rect(35,y,100,70))
    LeftToolBarY.append(y)    #remembers the Y coordinates for the toolbar (X coordinate is 30 for each Rectangle)
    draw.rect(screen,black,Rect(33,y-2,104,74),3)

for y in range(200,520,85):     #draws the right toolbar
    draw.rect(screen,gray90,Rect(150,y,100,70))
    RightToolBarY.append(y)     #remembers the Y coordinates for the right toolbar (X is 150 for each rectangle)
    draw.rect(screen,black,Rect(148,y-2,104,74),3)

for y in range(30,139,54):      #draws the options menu
    draw.rect(screen,gray90,Rect(150,y,100,45))
    SizeMenuBarY.append(y)      #remembers the Y coordinates for the options menu (X is 150 for each rectangle)

count=0
stamppics=[lightningmcqueenpic,pooppic,pikachupic,evilmonkeypic,brianpbjpic,konpic]      #a list of all the stamp pictures
for i in range(295,771,95):
    StampX.append(i)
    draw.rect(screen,gray90,Rect(i,590,80,80))  #draws the background gray for each stamp
    screen.blit(stamppics[count],(i,590))       #blits one of the pictures from the list of stamp variables
    draw.rect(screen,black,Rect(i,590,80,80),3) #draws the highlight for the stamp rectangle
    count+=1
    
"""    
#############################################################################################################################
##### Tools #################################################################################################################
##### 0=Pencil , 1=Eraser , 2=Paint Brush, 3=Paint Bucket ###################################################################
##### 4=Spray Paint , 5=Eye Dropper ,6=Line Tool ############################################################################
##### 7=Rect tool , 8=Oval Tool , 9=Selector Tool ###########################################################################
#############################################################################################################################
"""   

def Pencil(screen,colour,Rectcanvas,mx,my,pencilsize):
    screen.set_clip(Rectcanvas)     #only allows the canvas pixels to be changed
    global screenCopy
    global oldx,oldy         #keeps track of old values (remembers them from one part to the other)
    mx,my=mouse.get_pos()
    if mb==1:                   #draws a line to the previous point if mouse is clicked
        draw.line(screen,colour,(oldx,oldy),(mx,my),pencilsize)
        screenCopy=screen.copy()
    oldx,oldy=mx,my


def Eraser(screen,Rectcanvas,mx,my,erasersize):
    screen.set_clip(Rectcanvas)     #only allows the canvas pixels to be changed
    global screenCopy
    global oldx,oldy                #keeps track of old values (remembers them from one part to the other)
    screen.blit(screenCopy,(0,0))
    if mb==1:
        draw.rect(screen,white,(mx-(erasersize/2),my-(erasersize/2),erasersize,erasersize))
        draw.line(screen,white,(oldx,oldy),(mx,my),erasersize)          #connects each rectangle by a line
        screenCopy=screen.copy()
    draw.rect(screen,black,(mx-(erasersize/2),my-(erasersize/2),erasersize,erasersize),2)  #draws the rectangle cursor
    oldx,oldy=mx,my

    
def Paintbrush(screen,colour,Rectcanvas,mx,my,brushsize):
    screen.set_clip(Rectcanvas)     #only allows the canvas pixels to be changed
    global screenCopy
    global oldx,oldy         #keeps track of old values (remembers them from one part to the other)
    mx,my=mouse.get_pos()
    if mb==1:                   #draws a line to the previous point if mouse is clicked
        draw.circle(screen,colour,(mx,my),brushsize)
        draw.line(screen,colour,(oldx,oldy),(mx,my),brushsize+12)   #connects each circle by a line
        screenCopy=screen.copy()
    oldx,oldy=mx,my


def Paintbucket(screen,colour,Rectcanvas,mx,my):
    screen.set_clip(Rectcanvas)     #only allows the canvas pixels to be changed
    global screenCopy
    if mb==1:
        draw.rect(screen,colour,Rectcanvas)
        screenCopy=screen.copy()  

def Spraypaint(screen,colour,Rectcanvas,mx,my,spraysize):
    screen.set_clip(Rectcanvas)     #only allows the canvas pixels to be changed
    global screenCopy
    if mb==1:
        for i in range(220):         #number for how dense a single spray is
            dotx,doty=randint(mx-spraysize,mx+spraysize), randint(my-spraysize,my+spraysize)  #makes dotx and doty a random integer inside a rectangle around the mouse
            if (mx-dotx)**2+(my-doty)**2<=spraysize**2:     #checks if dotx and doty are inside a circle around the mouse
                screen.set_at((dotx,doty),colour)       #draws the dot
                display.update((dotx-1,doty-1,2,2))    #updates just the area around the dot
        screenCopy=screen.copy()


def Eyedropper(screen,mx,my,colourswitch):
    global screenCopy
    global colour,colour1,colour2
    if mb==1:
        if colourswitch==0:
            colour1=Pickcolour(screen,mx,my)          #picks the colour
            CIrect(screen,colour1,colour2,0)         #draws the the new colour indicator for the first colour
            colour=colour1                          #main colour used in programs becomes the first colour
        if colourswitch==1:
            colour2=Pickcolour(screen,mx,my)
            CIrect(screen,colour1,colour2,1)       #draws the the new colour indicator for the second colour
            colour=colour2                        #main colour used in programs becomes the second colour
        draw.rect(screen,colour,Rect(3,537,249,155),4) #draws highlight around the colour grid to indicate the colour chosen
        screenCopy=screen.copy()


def Linetool(screen,colour,Rectcanvas,oldx,oldy,mx,my,mhold,pencilsize):
    global screenCopy
    screen.set_clip(Rectcanvas)
    if mhold=="up":     #finalizes the picture when the left click button on the mouse is not held
        screenCopy=screen.copy()
    if mhold=="down":   #only runs when the left click button on the mouse is held down
        screen.blit(screenCopy,(0,0))
        draw.line(screen,colour,(oldx,oldy),(mx,my),pencilsize)


def Recttool(screen,colour,Rectcanvas,oldx,oldy,mx,my,mhold,rectfill):
    global screenCopy
    screen.set_clip(Rectcanvas)
    if mhold=="up":     #finalizes the picture when the left click button on the mouse is not held
        screenCopy=screen.copy()
    if mhold=="down":   #only runs when the left click button on the mouse is held down
        screen.blit(screenCopy,(0,0))
        draw.rect(screen,colour,Rect(oldx,oldy,mx-oldx,my-oldy),rectfill)


def Ovaltool(screen,colour,Rectcanvas,oldx,oldy,mx,my,mhold,rectfill):
    global screenCopy
    screen.set_clip(Rectcanvas)
    if mhold=="up":     #finalizes the picture when the left click button on the mouse is not held
        screenCopy=screen.copy()
    if mhold=="down":   #only runs when the left click button on the mouse is held down
        screen.blit(screenCopy,(0,0))
        width=abs(mx-oldx)
        height=abs(my-oldy)
        x=min(mx,oldx)
        y=min(my,oldy)
        if rectfill!=5 and width>4 and height>4:        #these "if"s makes sure the width and height is not
            draw.ellipse(screen,colour,Rect(x,y,width,height),rectfill) #more than the rectfill variable
        if rectfill==5 and width>9 and height>9:                        #so it doesn't crash
            draw.ellipse(screen,colour,Rect(x,y,width,height),rectfill)


def Stamps(screen,Rectcanvas,mx,my,stampnumber,stamppics):
    global screenCopy
    global mhold
    screen.set_clip(Rectcanvas)
    if mhold=="up":     #finalizes the picture when the left click button on the mouse is not held
        mouse.set_visible(True)
        screenCopy=screen.copy()
    if mhold=="down":   #only runs when the left click button on the mouse is held down
        mouse.set_visible(False)
        mx,my,mb=getmouse()
        screen.blit(screenCopy,(0,0))
        screen.blit(stamppics[stampnumber],(mx-40,my-40))


def Selector(screen,colour,Rectcanvas,oldx,oldy,mx,my,rectfill):
    global screenCopy 
    global selection
    global mhold
    global running
    newrect=Rect(0,0,0,0)
    breakloop2=True         #the flag to break the function of the second part of the Selector tool
    firstloop=True          #the flag to break the first loop
    screen.set_clip(Rectcanvas)
    if mhold=="up":
        screenCopy=screen.copy()
    if mhold=="down":   #only runs when the left click button on the mouse is held down
        while firstloop:
            if not Rectcanvas.collidepoint(mx,my) and mb==1:        #breaks if the mouse is clicked outside the canvas
                breakloop2=False
                break
            for evnt in event.get():
                if evnt.type==QUIT or key.get_pressed()[K_F5]==1:     #quits the program if the X is hit on the program or the "F5" key is pressed
                    running=False           #sets a flag to close the program
                    breakloop2=False        #sets the flag to break the next loop
                    firstloop=False         #sets the flag to break the current while loop
            mx,my,mb=getmouse()     #gets the position and status of the mouse
            if mhold=="up" and mouse.get_pressed()[0]==1:       #if the mouse is pressed and mhold is "up", it'll make mhold "down" so it shows that the mouse is being held.
                mhold="down"
            if mhold=="down" and mouse.get_pressed()[0]==0:     #switches the mhold back to "up" if the mouse is no longer pressed and the mhold is
                mhold="up"                                      #registered as "down"
            if mhold=="up":
                break
            if Rectcanvas.collidepoint(mx,my):
                screen.blit(screenCopy,(0,0))
                width=abs(mx-oldx)              #gets the total width of the rectangle
                height=abs(my-oldy)             #gets the total height of the rectangle
                x=min(mx,oldx)              #finds out which of the 2 points (mx,oldx) is the closest one to the top left
                y=min(my,oldy)              #finds out which of the 2 points (my,oldy) is the closest one to the top left
                draw.rect(screen,black,Rect(x-2,y-2,width+3,height+3),2)   #draws the rectangle to show what is being selected
                newrect=Rect(x,y,width,height)
                selection=screen.subsurface(newrect).copy()
                display.flip()
        Selector2(screen,colour,Rectcanvas,newrect,selection,breakloop2,x,y,width,height)       #the second part of the selector tool
        

def Selector2(screen,colour,Rectcanvas,newrect,selection,breakloop2,x,y,width,height):      #second part of the selector tool function (does the dragging)
    global screenCopy 
    global mhold
    global running
    secondloop=True             #sets the flag to break the second loop
    screen.blit(screenCopy,(0,0))
    screenCopy2=screen.copy()       #makes a copy of the screen without the rectangle highlight (This one sets the default screenCopy2 variable)
    if breakloop2==True:        #only runs if the variable breakloop2 is True
        oldnewrect=newrect
        while secondloop:
            event.get()         #gets all the inputted keys
            mx,my,mb=getmouse()
            checkmhold()
            draw.rect(screen,black,Rect(x-2,y-2,width+3,height+3),2)   #draws the rectangle to show what is being selected
            display.flip()
            for evnt in event.get():
                if evnt.type==QUIT or key.get_pressed()[K_F5]==1:     #quits the program if the X is hit on the program or the "F5" key is pressed
                    running=False           #sets a flag to close the program  
                    secondloop=False        #sets the flag to break the current while loop
                    
            if Rectcanvas.collidepoint(mx,my):      #only runs if the mouse is on the canvas
                distance=[mx-x,my-y]
                if newrect.collidepoint(mx,my) and mhold=="down":
                    while True:
                        mx,my,mb=getmouse()
                        checkmhold()
                        print ""      #this is put into the selector tool so that it doesn't crash (glitch with python)
                        if mhold=="up":
                            break
                        screen.blit(screenCopy,(0,0))
                        draw.rect(screen,white,oldnewrect)      #draws a white rectangle where the selected rectangle used to be
                        screen.blit(selection,(mx-distance[0],my-distance[1]))      #blits the selected rectangle
                        screenCopy2=screen.copy()
                        x=mx-distance[0]            #gets the new x coordinate for the top left corner of the selection
                        y=my-distance[1]            #gets the new y coordinate for the top left corner of the selection
                        newrect=Rect(mx-distance[0],my-distance[1],width,height)    #makes a varibale for the new selected rectangle
                        display.flip()
                    screenCopy2=screen.copy()       #makes a copy of the screen without the rectangle highlight
            if mouse.get_pressed()[0]==1 and not newrect.collidepoint(mx,my):   #breaks the loop if the mouse isn't clicked on the selection
                screen.blit(screenCopy2,(0,0))          #blits the copy of the screen without the rectangle highlight
                screenCopy=screen.copy()                #after blitting screenCopy2, the final copy of the screen is taken by this function
                time.wait(150)      #makes the program wait so that the mouse click is not registered and the selector tool is used again
                break
        
"""
#############################################################################################################################
##### Important Functions ###################################################################################################
#############################################################################################################################            
"""

def checkkeys():        #checks the some of the keys to activate certain tools or do a certain thing
    global screenCopy,tool,colour,colourswitch
    mouse.set_visible(True)
    if key.get_pressed()[K_F1]==1:                   #F1 clears the canvas to complete white
        draw.rect(screen,white,Rectcanvas)
        screenCopy=screen.copy()
        display.flip()
    if key.get_pressed()[K_1]==1:                   #these check if the number keys on the keyboard are pressed
        screen.blit(screenCopy,(0,0))               #and activates the coresponding tool
        tool=Picktool(tool,0)
    if key.get_pressed()[K_2]==1:
        screen.blit(screenCopy,(0,0))
        tool=Picktool(tool,1)
    if key.get_pressed()[K_3]==1:
        screen.blit(screenCopy,(0,0))
        tool=Picktool(tool,2)
    if key.get_pressed()[K_4]==1:
        screen.blit(screenCopy,(0,0))
        tool=Picktool(tool,3)
    if key.get_pressed()[K_5]==1:
        screen.blit(screenCopy,(0,0))
        tool=Picktool(tool,4)
    if key.get_pressed()[K_6]==1:
        screen.blit(screenCopy,(0,0))
        tool=Picktool(tool,5)
    if key.get_pressed()[K_7]==1:
        screen.blit(screenCopy,(0,0))
        tool=Picktool(tool,6)
    if key.get_pressed()[K_8]==1:
        screen.blit(screenCopy,(0,0))
        tool=Picktool(tool,7)
    if key.get_pressed()[K_9]==1:
        screen.blit(screenCopy,(0,0))
        tool=Picktool(tool,8)
    if key.get_pressed()[K_0]==1:
        screen.blit(screenCopy,(0,0))
        tool=Picktool(tool,9)
    if key.get_pressed()[K_c]==1:           #this checks if the "C" button is pressed to change the colour that is going to be used
        if colourswitch==0:
            colourswitch=1              #changes the colour in use to colour2
            colour=colour2              #makes the colour in use as colour2
            screen.blit(screenCopy,(0,0))
            selectcolour2(ccrect1,ccrect2)             #function to draw and highlight the indicator box for the second colour
        elif colourswitch==1:
            colourswitch=0              #changes the colour in use to colour1
            colour=colour1              #makes the colour in use as colour1
            screen.blit(screenCopy,(0,0))
            selectcolour1(ccrect1,ccrect2)             #function to draw and highlight the indicator box for the first colour
        screenCopy=screen.copy()
        display.flip
        time.wait(200)          #delays the program so the button "C" is not registered more than once when pressed

"""
########## Mouse Functions ##################################################################################################
"""

def getmouse():
    mx,my=mouse.get_pos()        #gets the position of the mouse
    mb=mouse.get_pressed()[0]     #gets the status of the left click button
    return (mx,my,mb)


def checkmhold():       #this part will check if the mouse is being held or not 
    global screenCopy
    global mhold
    global oldx,oldy
    if mhold=="up" and mouse.get_pressed()[0]==1:       #if the mouse is pressed and mhold is "up", it'll make mhold "down" so it shows that
        oldx,oldy=mouse.get_pos()                       #the mouse is being held.
        mhold="down"
    if mhold=="down" and mouse.get_pressed()[0]==0:     #switches the mhold back to "up" if the mouse is no longer pressed and the mhold is
        mhold="up"                                      #registered as "down"

"""
########## Colour Functions #################################################################################################
"""

def Pickcolour(screen,mx,my):
    colour=screen.get_at((mx,my))   #gets an RGB value from where the mouse is
    return colour


def checkcolour(colourswitch):          #checks for any attempts to change the colour
    global screenCopy
    global colour
    global colour1
    global colour2
    checkcolourswitch(screen,mb,ccrect1,ccrect2,colour1,colour2)
    if colourrect.collidepoint(mx,my) and mb==1:         #checks if the mouse clicks on the colour grid
        if colourswitch==0:
            colour1=Pickcolour(screen,mx,my)          #picks the colour
            CIrect(screen,colour1,colour2,0)         #draws the the new colour indicator for the first colour
            colour=colour1                          #main colour used in programs becomes the first colour
        if colourswitch==1:
            colour2=Pickcolour(screen,mx,my)
            CIrect(screen,colour1,colour2,1)       #draws the the new colour indicator for the second colour
            colour=colour2                        #main colour used in programs becomes the second colour
        draw.rect(screen,colour,Rect(3,537,249,155),4) #draws highlight around the colour grid to indicate the colour chosen
        screenCopy=screen.copy()


def selectcolour1(ccrect1,ccrect2):             #function to draw and highlight the indicator box for the first colour
    draw.rect(screen,colour2,ccrect2)           #clears the other colour of it's highlight
    draw.rect(screen,green,ccrect1,5)           #draws the highlight for the first colour if clicked
    draw.rect(screen,white,Rect(3,28,24,499),3)  #draws highlight for the current colour indicator
    draw.rect(screen,colour,Rect(3,537,249,155),4) #draws highlight around the colour grid to indicate the colour chosen


def selectcolour2(ccrect1,ccrect2):             #function to draw and highlight the indicator box for the second colour
    draw.rect(screen,colour1,ccrect1)           #clears the other colour of it's highlight
    draw.rect(screen,green,ccrect2,5)           #draws the highlight for the second colour if clicked
    draw.rect(screen,white,Rect(3,28,24,499),3)  #draws highlight for the current colour indicator
    draw.rect(screen,colour,Rect(3,537,249,155),4) #draws highlight around the colour grid to indicate the colour chosen

    
def checkcolourswitch(screen,mb,ccrect1,ccrect2,colour1,colour2):       #checks if the 2 different colour memory boxes are clicked on
    global colourswitch
    global colour
    global screenCopy
    if ccrect1.collidepoint(mx,my) and mb==1:
        colourswitch=0
        colour=colour1              #main colour used in programs becomes the first colour
        selectcolour1(ccrect1,ccrect2)
        screenCopy=screen.copy()
    elif ccrect2.collidepoint(mx,my) and mb==1:
        colourswitch=1
        colour=colour2              #main colour used in programs becomes the second colour
        selectcolour2(ccrect1,ccrect2)
        screenCopy=screen.copy()
        

def CIrect(screen,colour1,colour2,colourswitch):       #function to draw the new current colour indicator rectangle
    if colourswitch==0:
        draw.rect(screen,colour1,ccrect1)
        draw.rect(screen,green,ccrect1,5)           #draws the highlight for the first colour
    elif colourswitch==1:
        draw.rect(screen,colour2,ccrect2)
        draw.rect(screen,green,ccrect2,5)           #draws the highlight for the second colour
    draw.rect(screen,white,Rect(3,28,24,499),3)  #draws highlight for the current colour indicator

"""
########## Option Functions ################################################################################################
"""

def defaultsize():      #makes all the sizes back to the smallest size (defualt size)
    global pencilsize
    global brushsize
    global spraysize
    global erasersize
    global rectfill
    pencilsize=1
    brushsize=8
    spraysize=12
    erasersize=15
    rectfill=0


def nooptions(screen):      #draws a box to clear the options menu for certain tools
    screen.blit(optionsbackrect,(143,22,114,168))       #draws the background where the options menu is
    screenCopy=screen.copy()


def options(screen,tool,SizeMenuBarY):
    defaultsize()       #changes the sizes back to the first one
    for i in SizeMenuBarY:
        draw.rect(screen,gray90,Rect(150,i,100,45))
    if tool=="Pencil" or tool=="Linetool":
        draw.line(screen,black,(170,52),(230,52),1)    #draws the first pencil size pic
        draw.line(screen,black,(170,106),(230,106),3)  #draws the second pencil size pic
        draw.line(screen,black,(170,160),(230,160),6)  #draws the third pencil size pic
    elif tool=="Eraser":
        draw.rect(screen,white,(200-(15/2),52-(15/2),15,15))        #draws the first eraser Size Pic
        draw.rect(screen,black,(200-(15/2),52-(15/2),15,15),2)
        draw.rect(screen,white,(200-(23/2),105-(23/2),23,23))     #draws the second eraser Size Pic
        draw.rect(screen,black,(200-(23/2),105-(23/2),23,23),2)
        draw.rect(screen,white,(200-(30/2),160-(30/2),30,30))        #draws the third eraser Size Pic
        draw.rect(screen,black,(200-(30/2),160-(30/2),30,30),2)
    elif tool=="Paintbrush":
        draw.line(screen,black,(170,52),(230,52),10)    #draws the first paintbrush size pic       
        draw.line(screen,black,(170,106),(230,106),15)  #draws the second paintbrush size pic
        draw.line(screen,black,(170,160),(230,160),18)  #draws the third paintbrush size pic
    elif tool=="Spraypaint":
        screen.blit(spraypaints1pic,Rect(155,32,90,40))     #blits the first spraypaint size pic
        screen.blit(spraypaints2pic,Rect(155,86,90,40))     #blits the second spraypaint size pic
        screen.blit(spraypaints3pic,Rect(155,140,90,40))    #blits the third spraypaint size pic
    elif tool=="Recttool":
        draw.rect(screen,red3,(170,40,60,25))           #draws the first rectangle tool size pic
        draw.rect(screen,red3,(170,94,60,25),2)         #draws the second rectangle tool size pic
        draw.rect(screen,red3,(170,148,60,25),5)        #draws the second rectangle tool size pic
    elif tool=="Ovaltool":
        draw.ellipse(screen,(120,176,230),(165,35,70,35))           #draws the first oval tool size pic
        draw.ellipse(screen,(120,176,230),(165,89,70,35),2)         #draws the second oval tool size pic
        draw.ellipse(screen,(120,176,230),(165,143,70,35),5)        #draws the second oval tool size pic


def HighlightOptions(screen,optionsrect):       #Highlights the option boxes
    optionsrect1=Rect(150,30,100,45)
    optionsrect2=Rect(150,84,100,45)
    optionsrect3=Rect(150,138,100,45)
    options(screen,tool,SizeMenuBarY)
    draw.rect(screen,white,Rect(145,24,110,164),5)
    draw.rect(screen,black,Rect(148,28,104,157),3)  #draws the highlight for the options menu
    draw.line(screen,black,(147,75+4),(252,75+4),3)     #draws the first divider line for the options
    draw.line(screen,black,(147,129+4),(252,129+4),3)   #draws the second divider line for the options
    if optionsrect==optionsrect1:
        draw.rect(screen,green,Rect(151,31,98,43),3)
    if optionsrect==optionsrect2:
        draw.rect(screen,green,Rect(151,85,98,43),3)
    if optionsrect==optionsrect3:
        draw.rect(screen,green,Rect(151,139,98,43),3)
        

def checkoptions():             #checks the option menus for mouse selection
    global pencilsize,brushsize,spraysize,erasersize,rectfill,screenCopy,OSactivate,optionswitch
    optionsrect1=Rect(150,30,100,45)
    optionsrect2=Rect(150,84,100,45)
    optionsrect3=Rect(150,138,100,45)
    if optionsrect1.collidepoint(mx,my) and mb==1 or OSactivate==1 and optionswitch==0:     #selects the option if the mouse clicks on the box or the button C is pressed
        HighlightOptions(screen,optionsrect1)
        defaultsize()            #makes all the sizes the default sizes (smallest size)
    elif optionsrect2.collidepoint(mx,my) and mb==1 or OSactivate==1 and optionswitch==1:     #selects the option if the mouse clicks on the box or the button C is pressed
        HighlightOptions(screen,optionsrect2)
        pencilsize=3            #second set of sizes
        brushsize=13
        spraysize=18
        erasersize=30
        rectfill=2
    elif optionsrect3.collidepoint(mx,my) and mb==1 or OSactivate==1 and optionswitch==2:     #selects the option if the mouse clicks on the box or the button C is pressed
        HighlightOptions(screen,optionsrect3)
        pencilsize=6            #third set of sizes
        brushsize=16
        spraysize=22
        erasersize=50
        rectfill=5
    screenCopy=screen.copy()


def checkoptionswitch():                #checks if the Left Shift button has been pressed to change the current option to the next
    global optionswitch,OSactivate
    if key.get_pressed()[K_LSHIFT]==1:
        screen.blit(screenCopy,(0,0))
        OSactivate=1                    #a switch variable, used to activate another function after this one
        if optionswitch==2:
            optionswitch=0
        else:
            optionswitch+=1
        checkoptions()
        time.wait(200)              #delays the program so the Left Shift key is not registered more than once when pressed

        
"""
########## Tool Functions ###################################################################################################
"""

def drawtoolpics():         #draws the pictures for the tools on the screen
    screen.blit(pencilpic,Rect(52,32,65,65))          #blits the tool pictures onto the screen
    screen.blit(eraserpic,Rect(52,117,65,65))
    screen.blit(paintbrushpic,Rect(52,202,65,65))
    screen.blit(paintbucketpic,Rect(52,287,65,65))
    screen.blit(spraypaintpic,Rect(52,372+4,65,65))
    screen.blit(eyedropperpic,Rect(52,457,65,65))
    screen.blit(recttoolpic,Rect(150,285,100,70))
    screen.blit(ovaltoolpic,Rect(150,370,100,70))
    screen.blit(linetoolpic,Rect(150,200,100,70))
    screen.blit(selectortoolpic,Rect(150,455,100,70))


def checkstamps(mb,StampX):
    global stampnumber
    global tool
    global screenCopy
    for i in range(len(StampX)):
        StampRect=Rect(StampX[i],590,80,80)
        if StampRect.collidepoint(mx,my) and mb==1:
            tool="Stamp"
            stampnumber=i
            Highlightstamp(screen,StampX,stampnumber)
            screenCopy=screen.copy()


def Highlightstamp(screen,StampX,stampnumber):
    nooptions(screen)           #displays no options
    drawstamps(StampX,stamppics)        #draws the stamps to get rid of the highlights
    drawltoolbar(screen,LeftToolBarY)       #draws the regular Left Toolbar to get rid of highlights
    drawrtoolbar(screen,RightToolBarY)      #draws the regular Right Toolbar to get rid of highlights
    drawtoolpics()          #draws all the pictures for the Tools back on the toolbars
    draw.rect(screen,green,Rect(StampX[stampnumber]+2,592,76,76),3)
    display.flip()
    
    
def checkrtoolbar(RightToolBarY):       #a function to check for any mouse selections on the right toolbar
    global toolnumber
    global tool
    global screenCopy
    for i in range(len(RightToolBarY)):     #loops to check every box
        RToolbox=Rect(150,RightToolBarY[i],100,70)
        if RToolbox.collidepoint(mx,my) and mb==1:
            toolnumber=i+6              #adds 6 to the tool number to indicate that it is on the right toolbar
            tool=Picktool(tool,toolnumber)
            screenCopy=screen.copy()


def checkltoolbar(LeftToolBarY):        #a function to check for any mouse selections on the left toolbar
    global toolnumber
    global tool
    global screenCopy
    for i in range(len(LeftToolBarY)):      #loops to check every box
        LToolbox = Rect(30,LeftToolBarY[i],100,70)
        if LToolbox.collidepoint(mx,my) and mb==1:
            toolnumber=i            #this variable is used to identify the correct tool in other functions and which box to highlight from a list
            tool=Picktool(tool,toolnumber)
            screenCopy=screen.copy()


def Highlighttoolbox(screen,toolnumber):       #Draws a highlight on the first column toolbars on the left
    if toolnumber<=5:           #runs only when the selected tool is on the left toolbar (toolnumber of less than or equal to 5)
        drawltoolbar(screen,LeftToolBarY)
        drawrtoolbar(screen,RightToolBarY)
        drawtoolpics()
        draw.rect(screen,green,Rect(36,LeftToolBarY[toolnumber]+1,98,68),3)
    if toolnumber>=6:           #runs only when the selected tool is on the right toolbar (toolnumber of more than 5)
        drawltoolbar(screen,LeftToolBarY)
        drawrtoolbar(screen,RightToolBarY)
        drawtoolpics() 
        toolnumber-=6    #subtracts 6 from the toolnumber to allow it to work with finding the Y coordinates from the list
        draw.rect(screen,green,Rect(151,RightToolBarY[toolnumber]+1,98,68),3)
    display.flip()
    

def Picktool(tool,toolnumber):          #the function that chooses the tool
    global screenCopy
    Highlighttoolbox(screen,toolnumber)    #highlights the button for the selected tool
    drawstamps(StampX,stamppics)
    if toolnumber==0:
        options(screen,tool,SizeMenuBarY)       #draws the options for the Pencil   
        HighlightOptions(screen,optionsrect1)
        tool="Pencil"
    elif toolnumber==1:
        options(screen,tool,SizeMenuBarY)       #draws the options for the Eraser
        HighlightOptions(screen,optionsrect1)
        tool="Eraser"
    elif toolnumber==2:
        options(screen,tool,SizeMenuBarY)       #draws the options for the Paintbrush
        HighlightOptions(screen,optionsrect1)
        tool="Paintbrush"
    elif toolnumber==3:
        nooptions(screen)       #displays no options
        tool="Paintbucket"
    elif toolnumber==4:
        options(screen,tool,SizeMenuBarY)       #draws the options for the Spraypaint
        HighlightOptions(screen,optionsrect1)
        tool="Spraypaint"
    elif toolnumber==5:
        nooptions(screen)       #displays no options
        tool="Eyedropper"
    elif toolnumber==6:
        options(screen,"Pencil",SizeMenuBarY)    #draws the options for the Linetool (Same as Pencil options)
        HighlightOptions(screen,optionsrect1)
        tool="Linetool"
    elif toolnumber==7:
        HighlightOptions(screen,optionsrect1)   #draws the options for the Recttool
        tool="Recttool"
    elif toolnumber==8:
        HighlightOptions(screen,optionsrect1)   #draws the options for the Ovaltool
        tool="Ovaltool"
    elif toolnumber==9:
        nooptions(screen)       #displays no options
        tool="Selector"
    screenCopy=screen.copy()
    return tool 


def usetool():   #initiates the tool
    global mhold
    global oldx,oldy
    checkmhold()                    #checks if the mouse is being held (this helps to make sure that random tools aren't selected when one is in use)
    if tool=="Pencil":
        Pencil(screen,colour,Rectcanvas,mx,my,pencilsize)
    elif tool=="Eraser":
        mouse.set_visible(False)
        Eraser(screen,Rectcanvas,mx,my,erasersize)
    elif tool=="Paintbrush":
        Paintbrush(screen,colour,Rectcanvas,mx,my,brushsize)
    elif tool=="Paintbucket":
        Paintbucket(screen,colour,Rectcanvas,mx,my)
    elif tool=="Spraypaint":
        Spraypaint(screen,colour,Rectcanvas,mx,my,spraysize)
    elif tool=="Eyedropper":
        Eyedropper(screen,mx,my,colourswitch)
    elif tool=="Linetool":
        Linetool(screen,colour,Rectcanvas,oldx,oldy,mx,my,mhold,pencilsize)
    elif tool=="Recttool":
        Recttool(screen,colour,Rectcanvas,oldx,oldy,mx,my,mhold,rectfill)
    elif tool=="Ovaltool":
        Ovaltool(screen,colour,Rectcanvas,oldx,oldy,mx,my,mhold,rectfill)
    elif tool=="Stamp":
        Stamps(screen,Rectcanvas,mx,my,stampnumber,stamppics)
    elif tool=="Selector":
        Selector(screen,colour,Rectcanvas,oldx,oldy,mx,my,rectfill)
    
"""
#############################################################################################################################
##### Other Functions #######################################################################################################
#############################################################################################################################
"""

def drawltoolbar(screen,LeftToolBarY):      #function to draw the left toolbar
    for y in LeftToolBarY:     #draws the left toolbar
        draw.rect(screen,gray90,(35,y,100,70))


def drawrtoolbar(screen,RightToolBarY):     #function to draw the right toolbar
    for y in range(200,520,85):     #draws the right toolbar
        draw.rect(screen,gray90,(150,y,100,70))


def drawstamps(StampX,stamppics):
    for i in range(len(StampX)):
        draw.rect(screen,gray90,Rect(StampX[i],590,80,80))  #draws the background gray for each stamp
        screen.blit(stamppics[i],(StampX[i],590))       #blits one of the pictures from the list of stamp variables
        draw.rect(screen,black,Rect(StampX[i],590,80,80),3) #draws the highlight for the stamp rectangle


def defaultsaveloadbox(savebox,loadbox):
    global screenCopy
    draw.rect(screen,gray90,loadbox)   #draws the load image box
    screen.blit(loadtextpic,Rect(910,592,80,45))
    draw.rect(screen,black,Rect(888,590,104,49),3)  #draws the load image box highlight
    draw.rect(screen,gray90,savebox)   #draws the save image box
    screen.blit(savetextpic,Rect(910,648,80,45))
    draw.rect(screen,black,Rect(888,646,104,49),3)  #draws the save image box highlight
    screenCopy=screen.copy()


def checksave(screen,Rectcanvas,savebox,loadtextpic):
    if savebox.collidepoint(mx,my) and mb==1:   #checks if the mouse clicks on the save box
        draw.rect(screen,green,savebox)   #draws the green save image box
        screen.blit(savetextpic,Rect(910,648,80,45))    #blits the "Save" text
        draw.rect(screen,black,Rect(888,646,104,49),3)  #draws the save image box highlight
        display.flip()
        saveimage(screen,Rectcanvas)
        defaultsaveloadbox(savebox,loadbox)      #makes the save and load back to their default colour


def checkload(screen,Rectcanvas,loadbox,savetextpic):
    if loadbox.collidepoint(mx,my) and mb==1:   #checks if the mouse clicks on the load box
        draw.rect(screen,green,loadbox)   #draws the green load image box
        screen.blit(loadtextpic,Rect(910,592,80,45))    #blits the "Load" text
        draw.rect(screen,black,Rect(888,590,104,49),3)  #draws the load image box highlight
        display.flip()
        loadimage(screen,Rectcanvas)
        defaultsaveloadbox(savebox,loadbox)      #makes the save and load back to their default colour


def drawfilenametext(screen,filenamefont,filename):
    draw.rect(screen,white,Rect(280,620,580,35))            #draws the white box where the filename goes
    filenametextpic=filenamefont.render(filename,False,(0,0,0))     #renders the filename into a text pic
    screen.blit(filenametextpic,(282,622))      #blits the filename pic onto the white box
    display.flip()

        
def saveimage(screen,Rectcanvas):       #function that saves the image on the canvas
    global Stamparea
    global running
    global screenCopy
    filename=""
    shift="off"
    badcharacters=""" \/:*?"<>\ """         #characters that can't be used in the filename of windows
    Stamparea=screen.subsurface(Rect(265,585,606,86)).copy()        #makes a copy of the original area where the stamps are
    canvassave=screen.subsurface(Rectcanvas).copy()         #makes a copy of the canvas for saving purposes
    draw.rect(screen,yellow,Rect(270,590,600,80))           #draws the yellow box for saving
    draw.rect(screen,black,Rect(270,590,600,80),3)          #draws the outline for the yellow box
    draw.rect(screen,white,Rect(280,620,580,35))            #draws the white box where the filename goes
    screen.blit(saveinstruction,(280,590))              #blits the instructions for saving
    display.flip()
    saveloop=True
    while saveloop:
        for evnt in event.get():
            if key.get_pressed()[K_LSHIFT]==1:          #turns on and off Capital letters
                if shift=="off":
                    shift="on"
                elif shift=="on":
                    shift="off"
            elif key.get_pressed()[K_ESCAPE]==1:  #quits the save if the ESC key is pressed on the keyboard
                screen.blit(Stamparea,(265,585))            #clears the stamp area back to the original picture of it
                screenCopy=screen.copy()
                saveloop=False
                
            elif evnt.type==QUIT:     #quits the program if the X is hit on the program
                saveloop=False
                running=False
                
            elif key.get_pressed()[K_RETURN]==1:
                image.save(canvassave,filename+".bmp")          #always saves the image as a bitmap file
                print "Image saved as","'",filename+".bmp'"
                print ""
                screen.blit(Stamparea,(265,585))            #clears the stamp area back to the original picture of it
                saveloop=False
                
            elif key.get_pressed()[K_SPACE]==1 and len(filename)!=50:       #maximum character limit is 50 so it doesn't go off the box
                filename+=" "
                drawfilenametext(screen,filenamefont,filename)          #draws the text for the filename
                
            elif key.get_pressed()[K_BACKSPACE]==1 and len(filename)!=0:
                filename=filename[0:len(filename)-1]
                drawfilenametext(screen,filenamefont,filename)          #draws the text for the filename
                
            elif evnt.type==KEYDOWN and key.get_pressed()[K_BACKSPACE]!=1 and len(filename)!=50:    #maximum character limit is 50 so it doesn't go off the box makes sure that backspace key is not pressed so it doesn't register weird codes
                character=chr(evnt.key)
                if character not in badcharacters and shift=="on":
                    filename+=character.upper()             #makes the letter capitalized
                if character not in badcharacters and shift=="off":
                    filename+=character    
                drawfilenametext(screen,filenamefont,filename)          #draws the text for the filename


def loadimage(screen,Rectcanvas):       #function that loads an image onto the canvas
    global Stamparea
    global running
    global screenCopy
    filename=""
    shift="off"
    badcharacters=""" \/:*?"<>\ """         #characters that can't be used in the filename of windows
    Stamparea=screen.subsurface(Rect(265,585,606,86)).copy()        #makes a copy of the original area where the stamps are
    draw.rect(screen,yellow,Rect(270,590,600,80))           #draws the yellow box for loading
    draw.rect(screen,black,Rect(270,590,600,80),3)          #draws the outline for the yellow box
    draw.rect(screen,white,Rect(280,620,580,35))            #draws the white box where the filename goes
    screen.blit(loadinstruction,(280,590))              #blits the instructions for loading
    display.flip()
    saveloop=True
    while saveloop:
        for evnt in event.get():
            if key.get_pressed()[K_LSHIFT]==1:          #turns on and off Capital letters
                if shift=="off":
                    shift="on"
                elif shift=="on":
                    shift="off"
            elif key.get_pressed()[K_ESCAPE]==1:  #quits the save if the ESC key is pressed on the keyboard
                screen.blit(Stamparea,(265,585))            #clears the stamp area back to the original picture of it
                screenCopy=screen.copy()
                saveloop=False
                
            elif evnt.type==QUIT:     #quits the program if the X is hit on the program
                saveloop=False
                running=False
                
            elif key.get_pressed()[K_RETURN]==1:        #loads the picture if Return key is pressed
                screen.set_clip(Rectcanvas)
                newimage=image.load(filename)
                screen.blit(newimage,(canvas[0],canvas[1]))
                print "Loaded image","'",filename,"'"
                print ""
                screen.set_clip(Rect(0,0,1000,700))      #allows all pixels to be changed
                screen.blit(Stamparea,(265,585))            #clears the stamp area back to the original picture of it
                saveloop=False
                
            elif key.get_pressed()[K_SPACE]==1 and len(filename)!=50:       #maximum character limit is 50 so it doesn't go off the box
                filename+=" "
                drawfilenametext(screen,filenamefont,filename)          #draws the text for the filename
                
            elif key.get_pressed()[K_BACKSPACE]==1 and len(filename)!=0:
                filename=filename[0:len(filename)-1]
                drawfilenametext(screen,filenamefont,filename)          #draws the text for the filename
                
            elif evnt.type==KEYDOWN and key.get_pressed()[K_BACKSPACE]!=1 and len(filename)!=50:    #maximum character limit is 50 so it doesn't go off the box makes sure that backspace key is not pressed so it doesn't register weird codes
                character=chr(evnt.key)
                if character not in badcharacters and shift=="on":
                    filename+=character.upper()             #makes the letter capitalized
                if character not in badcharacters and shift=="off":
                    filename+=character     
                drawfilenametext(screen,filenamefont,filename)          #draws the text for the filename

"""
#############################################################################################################################    
##### drawScene (Basically the Main Loop) ###################################################################################
#############################################################################################################################
"""

def drawScene(screen,Rectcanvas,mx,my,mb):        #basically like the main loop
    global tool             #keeps track of the value of tool
    global colour           #keeps track of the value of colour
    global screenCopy       #keeps track of the previous screen
    global mhold            #keeps track of the status of the left click button on the mouse
    global OSactivate

    screen.set_clip(Rect(0,0,1000,700))      #allows all pixels to be changed
    checkkeys()         #checks if certain keys are pressed
    if tool=="Pencil" or tool=="Eraser" or tool=="Paintbrush" or tool=="Spraypaint" or tool=="Linetool" or tool=="Recttool" or tool=="Ovaltool":
        checkoptionswitch()     #checks if the Left Shift button is switched to change the current option to the next
        OSactivate=0        #changes the status of a switch for the options
        
    if not Rectcanvas.collidepoint(mx,my):      #only does the functions below if the mouse position is not on the canvas
        screen.blit(screenCopy,(0,0))
        if mhold=="down" and mouse.get_pressed()[0]==0:     #switches the mhold back to "up" if the mouse is no longer pressed and the mhold is
            mhold="up"                                      #registered as "down"
            
        if mhold=="up":     #this makes sure that random functions off the canvas are not being activated when users uses the tool
            checkcolour(colourswitch)       #checks for colour selection
            checkltoolbar(LeftToolBarY)     #checks the left toolbar for mouse selection
            checkrtoolbar(RightToolBarY)    #checks the right toolbar for mouse selection
            if Rect(890,10,100,35).collidepoint(mx,my) and mb==1:
                draw.rect(screen,white,Rectcanvas)
                screenCopy=screen.copy()
            checkstamps(mb,StampX)
            if tool=="Pencil" or tool=="Eraser" or tool=="Paintbrush" or tool=="Spraypaint" or tool=="Linetool" or tool=="Recttool" or tool=="Ovaltool":
                checkoptions()          #checks the options menu for mouse selection
            checksave(screen,Rectcanvas,savebox,loadtextpic)        #checks if the save button is clicked on
            checkload(screen,Rectcanvas,loadbox,savetextpic)        #checks if the load button is clicked on
        mouse.set_visible(True)     #allows us to see the mouse curser
        
    if Rectcanvas.collidepoint(mx,my):               #checks if the mouse is on the canvas, it then initiates the tool
        usetool()
        
    display.flip()

"""       
#############################################################################################################################    
##### Main Loop #############################################################################################################
#############################################################################################################################
""" 

Picktool(tool,0)  #makes the default tool pencil
Highlighttoolbox(screen,0) #Highlights for the first tool
options(screen,tool,SizeMenuBarY)   #draws the options menu with pictures
HighlightOptions(screen,optionsrect1)  #highlights the first option box
screenCopy=screen.copy()

running=True                    #the variable that allows the whole program to run
myClock=time.Clock()
while running:
    for evnt in event.get():
        if evnt.type==QUIT or key.get_pressed()[K_F5]==1:     #quits the program if the X is hit on the program or the "ESC" key is pressed
            running=False

    mx,my,mb=getmouse()     #gets the position and status of the mouse
    drawScene(screen,Rectcanvas,mx,my,mb)     #runs the main loop
    
    myClock.tick(60)
quit()
