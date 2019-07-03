add_library('minim')
minim = Minim(this)

def setup():
    player = minim.loadFile("Super Mario Bros. Soundtrack (1).mp3")
    player.play()
    size(700,700) 
    
    x = 35
    y = 35
    a = 35
    b = 80
    global x
    global y
    global a
    global b

def draw():
    background(0,0,0)
    
    gameBoard()
    ghost(255,0,0,a,b)
    pacMan(x,y)
    
    
def gameBoard():
    background(0,0,0)
    
    stroke(255,255,255)
    strokeWeight(5)
    noFill()
    
    line(0,0,700,0) #outermost lines
    line(0,0,0,700)
    line(700,0,700,700)
    line(0,700,700,700)

    line(10,690,690,690) #2nd layer of lines
    line(10,10,10,200)
    line(10,200,50,200)
    line(50,200,50,360)
    line(50,360,10,360)
    line(10,360,10,690)
    line(10,10,690,10)
    line(690,10,690,200)
    line(690,200,625,200)
    line(625,200,625,360)
    line(625,360,690,360)
    line(690,360,690,690)
    
    line(200,270,200,290) #square in the C
    line(170,270,200,270)
    line(170,270,170,290)
    line(170,290,200,290)
    
    line(60,60,250,60) #shape in top right corner
    line(60,60,60,150)
    line(60,150,110,150)
    line(110,150,110,130)
    line(110,130,80,130)
    line(80,130,80,80)
    line(80,80,250,80)
    line(250,80,250,60)
    
    line(160,150,540,150) #upside down t at the top (middle)
    line(160,150,160,130)
    line(160,130,300,130)
    line(300,130,300,60)
    line(540,150,540,130)
    line(540,130,320,130)
    line(320,130,320,60)
    line(320,60,300,60)
    
    line(370,60,640,60) #shape in the top left corner
    line(370,60,370,80)
    line(370,80,620,80)
    line(590,130,590,150)
    line(590,150,640,150)
    line(640,150,640,60)
    line(620,80,620,130)
    line(620,130,590,130)
    
    line(60,410,60,500) #shape underneath the C
    line(60,410,150,410)
    line(60,500,80,500)
    line(80,500,80,430)
    line(80,430,150,430)
    line(150,430,150,410)
    
    line(60,550,60,640) #shape in the bottom left corner
    line(60,550,80,550)
    line(80,550,80,620)
    line(60,640,150,640)
    line(80,620,150,620)
    line(150,620,150,640)
    
    line(130,480,150,480) #bar 1
    line(130,480,130,570)
    line(130,570,150,570)
    line(150,480,150,570)
    
    line(550,410,640,410) #shape under the I
    line(640,410,640,500)
    line(640,500,620,500)
    line(620,500,620,430)
    line(620,430,550,430)
    line(550,430,550,410)
    
    line(550,620,620,620) #shape in the bottom right corner
    line(620,620,620,550)
    line(620,550,640,550)
    line(640,550,640,640)
    line(640,640,550,640)
    line(550,640,550,620)
    
    line(550,480,570,480) #bar 2
    line(570,480,570,570)
    line(570,570,550,570)
    line(550,570,550,480)
    
    line(200,410,290,410) #square  1
    line(200,410,200,500)
    line(200,500,290,500)
    line(290,410,290,500)
    
    line(200,550,200,640) #square 2
    line(200,550,290,550)
    line(290,550,290,640)
    line(290,640,200,640)
        
    line(410,410,500,410) #square under second S / square 3
    line(410,410,410,500)
    line(500,500,500,410)
    line(410,500,500,500)
    
    line(410,550,410,640)
    line(410,550,500,550)
    line(500,550,500,640)
    line(500,640,410,640)

    
    line(340,410,360,410) #bar in the center at the bottom half of the screen
    line(340,410,340,640)
    line(340,640,360,640)
    line(360,640,360,410)
    
    
    frameRate(6)
    stroke(random(255),random(255),random(255))
    line(100,200,100,360) #C
    line(100,360,200,360)
    line(100,200,200,200)
    line(200,200,200,220)
    line(200,220,120,220)
    line(120,220,120,340)
    line(120,340,200,340)
    line(200,340,200,360)
    
    line(250,200,350,200) #s
    line(350,200,350,220)
    line(350,220,270,220)
    line(270,220,270,270)
    line(250,200,250,290)
    line(250,290,330,290)
    line(270,270,350,270)
    line(350,270,350,360)
    line(350,360,250,360)
    line(250,360,250,340)
    line(250,340,330,340)
    line(330,340,330,290)
    
    line(400,200,500,200) #s
    line(500,200,500,220)
    line(500,220,420,220)
    line(420,220,420,270)
    line(400,200,400,290)
    line(400,290,480,290)
    line(420,270,500,270)
    line(500,270,500,360)
    line(500,360,400,360)
    line(400,360,400,340)
    line(400,340,480,340)
    line(480,340,480,290)
    
    line(550,200,570,200)#i
    line(550,200,550,360)
    line(550,360,570,360)
    line(570,360,570,200)


def ghost(r,g,bl,a,b):
    noStroke()
    fill(r,g,bl)
    ellipse(a,b,35,35)
    fill(0)
    triangle(a,b+5,a-5,b+20,a+5,b+20)
    triangle(a+10,b+3,a+5,b+20,a+20,b+20)
    triangle(a-10,b+3,a-20,b+20,a-5,b+20)
    ellipse(a-7,b-2,5,5)
    ellipse(a+7,b-2,5,5)
    
def peach(x,y):
    ellipse(x,y,8,8)
    fill(255,204,153)
    
def Bigpeach(x,y):
    ellipse(x,y,15,15)
    fill(255,204,153)
    
def pacMan(x,y):
    fill(0,255,0)
    ellipse(x,y,40,40)
    fill(0,0,0)
    
def keyPressed():
    frameRate(15)
    global x
    global y
    
    left = True
    right = True
    down = True
    up = True
    
    # DOWN BOUNDARIES
    if y == 35 and ((x > 35 and x < 275) or (x > 275 and x < 345) or (x > 345 and x <= 665)):
        down = False
    if y == 105 and ((x >= 105  and x < 135) or (x > 135 and x <= 275) or (x >= 320 and x < 565) or (x > 565 and x <= 595)): 
        down = False
    if y == 175 and ((x == 35) or (x > 75 and x < 225) or (x > 225 and x < 375) or (x > 375 and x < 525) or (x > 525 and x < 595) or (x > 595)):
        down = False
    if y == 245 and ((x > 145 and x < 225) or (x > 295 and x < 375) or (x > 445 and x < 525)):
        down = False
    if y == 315 and ((x >= 145 and x < 225) or (x > 225 and x <= 305) or (x > 375 and x <= 455)):
        down = False 
    if y == 385 and ((x > 35  and x < 175) or (x > 175 and x < 315) or (x > 315 and x < 385) or (x > 385 and x < 525) or (x > 525 and x <665)): 
        down = False
    if y == 455 and ((x >= 105  and x < 175) or (x > 525 and x < 595)): 
        down = False
    if y == 525 and ((x > 35  and x < 105) or (x > 175 and x < 315) or (x > 385 and x < 525) or (x > 595 and x < 665)): 
        down = False
    if y == 595 and ((x >= 105  and x < 175) or (x > 525 and x < 595)): 
        down = False
    if y == 665:
        down = False
    
    # UP BOUNDARIES
    if y == 35:
        up = False
    if y == 105 and ((x >= 105 and x < 275 ) or (x > 345 and x >= 595)):
        up = False
   if y == 175 and ((x > 35 and x < 135) or (x > 135 and x < 565) or (x > 565 and x <665)):
       up = False
    
            
    
    
        
        
        
        
    if keyCode == UP and up == True:
        y = y-10
        triangle(x,y,x+20,y-20,x-20,y-20)
        print (" Y = ") + str(y)
    if keyCode == DOWN and down == True:
        y = y+10
        triangle(x,y,x-20,y+20,x+20,y+20)
        print (" Y = ") + str(y)
    if keyCode == LEFT and left == True:
        x = x-10
        triangle(x,y,x-20,y+20,x-20,y-20)
        print (" X = ") + str(x)
    if keyCode == RIGHT and right == True:
        x = x+10
        triangle(x,y,x+20,y+20,x+20,y-20)
        print (" X = ") + str(x)

