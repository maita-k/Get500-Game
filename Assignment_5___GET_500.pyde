'''
GET 500:
    A game where you move around the screen
    with the w,s,a and d keys to gain points
    until you reach a score of 500.
Author: Maita Kambarami
Student ID: 20068051
'''

#global values
xPos = 250
yPos = 250
xp=[random(470)]
yp=[random(470)]
p=[0]
diameter = 20
xchange=random(470)
ychange=random(470)

def setup():
    size(500, 500)
    background(255)
    frameRate(200)

def Box(): #places boxes on the screen
    global xp, yp
    fill(0)
    rect(xp[0],yp[0],30,30)

def draw(): 
    global xPos, yPos,xp,yp,p
    background(255)
    ''' these are your navigation keys!
    w= up      a=left
    s=down     d=right    '''
    if keyPressed:
        if key=='d':
            xPos = xPos + 1
        elif key=='a':
            xPos = xPos - 1
        elif key=='s':
            yPos = yPos + 1
        elif key=='w':
            yPos = yPos - 1
        ''' if you hit the edge of the screen you'll
        appear on the opposite side'''
        if xPos >= width + (diameter/2):
            xPos = -diameter/2
        elif  xPos <= -(diameter/2):
            xPos=width + (diameter/2)
        if yPos >= height + (diameter/2):
            yPos = -diameter/2
        elif  yPos <= -(diameter/2):
            yPos=height + (diameter/2)    
   
    Box()
    
    fill(255,0,0)
    ellipse(xPos, yPos, diameter, diameter)
    
    textSize(20)
    fill(255,0,255)
    text(sum(p),400,40) #shows your score
    
    if xPos>xp[0] and xPos<(xp[0]+diameter) and yPos>yp[0] and yPos<(yp[0]+diameter):
        #changes box position and your score of screen
            xp.remove(xp[0])
            xp.append(random(470))
            yp.remove(yp[0])
            yp.append(random(470))
            p.append(100)
            
    if len(p)==6: #when you reach 500 points you win!
        background(255,0,0)
        fill(0)
        text(sum(p),400,40)
        textSize(50)
        text("YOU WIN!",width/4,height/2)
            

