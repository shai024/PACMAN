add_library('minim')
minim = Minim(this)

def setup():
    player = minim.loadFile("Super Mario Bros. Soundtrack (1).mp3")
    player.play()
    size(700,700) 
    
    x = 35
    y = 35
    speed = 10
    directiony = 10
    global speed
    global directiony
    global x
    global y
    global balls
    global i

    
    i=1
    balls={}
    
    c=75
    while c<700:
        updatedict(c,35)
        c=c+35
    d=70
    while d<180:
        updatedict(670,d)
        d=d+35
    c=635
    while c>35:
        updatedict(c,175)
        c=c-35
    d=210
    while d<370:
        updatedict(75,d)
        d=d+35
        
    c=40
    while c<700:
        updatedict(c,385)
        c=c+35
    d=175
    while d<380:
        updatedict(600,d)
        d=d+35
    d=175
    while d<380:
        updatedict(530,d)
        d=d+35
    d=385
    while d<670:
        updatedict(40,d)
        d=d+35
    c=40
    while c<700:
        updatedict(c,665)
        c=c+35
    d=385
    while d<700:
        updatedict(670,d)
        d=d+35
    d=385
    while d<700:
        updatedict(180,d)
        d=d+35
    d=385
    while d<700:
        updatedict(530,d)
        d=d+35
        
    ghosts = [{"a":35, "b":35, "direction":"right", "r":255, "g":0, "bl":0},
              {"a":35, "b":665, "direction":"right", "r":0, "g":0, "bl":255},
              {"a":665, "b":665, "direction":"right", "r":0, "g":255, "bl":255},
            
    global ghosts
    

def draw():
    background(0,0,0)
    global speed
    global directiony
    
    gameBoard()
    pacMan(x,y)
    
    global ghosts   
    for character in ghosts:
    
        getMovesGhost(character["a"],character["b"])
        nextdirection = getNextDirection(character)
        if nextdirection == "left":
            character["a"] = character["a"] - speed
        if nextdirection == "right":
            character["a"] = character["a"] + speed
        if nextdirection == "up":
            character["b"] = character["b"] - directiony
        if nextdirection == "down":
            character["b"] = character["b"] + directiony 
            
        ghost(character["r"],character["g"],character["bl"],character["a"],character["b"])

    
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
    
    
    frameRate(3)
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
    
    gameended= True
        
    for ball in balls:
        value=balls[ball]
        if value[2] == True:
            dots(value[0], value[1]) 
        if abs(x-value[0])<= 5 and abs(y-value[1])<=5:
            balls[ball][2]=False
        if balls[ball][2]==True:
            gameended=False
            
    if gameended== True:
        print ('game over')

        
    
def dots(c,d):
    ellipse(c,d,5,5)

def updatedict(c,d):
    global balls
    global i
    balls[i]=[c,d,True]
    i=i+1

def ghost(r,g,bl,a,b):
    global speed
    global direction

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
    noStroke()
    fill(0,255,0)
    ellipse(x,y,40,40)
    fill(0,0,0)
    
def keyPressed():
    frameRate(10)
    global x
    global y
    
    moves = getMoves(x,y)
        
    if keyCode == UP and "up" in moves:
        y = y-5
        triangle(x,y,x+20,y-20,x-20,y-20)
        print (" Y = ") + str(y)
    if keyCode == DOWN and "down" in moves:
        y = y+5
        triangle(x,y,x-20,y+20,x+20,y+20)
        print (" Y = ") + str(y)
    if keyCode == LEFT and "left" in moves:
        x = x-5
        triangle(x,y,x-20,y+20,x-20,y-20)
        print (" X = ") + str(x)
    if keyCode == RIGHT and "right" in moves:
        x = x+5
        triangle(x,y,x+20,y+20,x+20,y-20)
        print (" X = ") + str(x)

def getMoves(x,y): #produces a list of possible moves based on PAC-MAN's position. 
    
    moves = []
    
    left = True
    right = True
    down = True
    up = True
    
    # DOWN BOUNDARIES
    if y == 35 and ((x > 35 and x < 275) or (x > 275 and x < 345) or (x > 345 and x < 665)):
        down = False
    if y == 105 and ((x >= 105  and x < 135) or (x > 135 and x <= 275) or (x >= 320 and x < 565) or (x > 565 and x < 595)): 
        down = False
    if y == 175 and ((x < 75) or (x > 75 and x < 225) or (x > 225 and x < 375) or (x > 375 and x < 525) or (x > 525 and x < 595) or (x > 595)):
        down = False
    if y == 245 and ((x > 145 and x < 225) or (x > 295 and x < 375) or (x > 445 and x < 525)):
        down = False
    if y == 315 and ((x >= 145 and x < 225) or (x > 225 and x <= 305) or (x > 375 and x <= 455)):
        down = False 
    if y == 385 and ((x > 35  and x < 175) or (x > 175 and x < 315) or (x > 315 and x < 385) or (x > 385 and x < 525) or (x > 525 and x <665)): 
        down = False
    if y == 455 and ((x > 105  and x < 175) or (x > 525 and x < 595)): 
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
    if y == 105 and ((x >= 105 and x < 275 ) or (x > 345 and x < 595)):
        up = False
    if y == 175 and ((x > 35 and x < 135) or (x > 135 and x < 565) or (x > 565 and x < 665)):
       up = False
    if y == 245 and ((x >= 145 and x < 225) or (x >= 295 and x < 375) or (x >= 445 and x <525)):
       up = False
    if y == 315 and ((x > 145 and x < 225) or (x > 225 and x <= 305) or (x > 375 and x <455)):
       up = False
    if y == 385 and ((x == 35) or (x > 75 and x < 225) or (x > 225 and x < 375) or (x > 375 and x <525) or (x > 525 and x < 595) or (x > 595 and x <= 665)):
       up = False
    if y == 455 and ((x >= 105 and x < 175) or (x > 525 and x <= 595)):
       up = False
    if y == 525 and ((x > 35 and x < 105) or (x > 105 and x < 175) or (x > 175 and x < 315) or (x > 315 and x < 385) or (x > 385 and x < 525) or (x > 525 and x < 595) or (x > 595 and x < 665)):
       up = False
    if y == 595 and ((x > 105 and x < 175) or (x > 525 and x < 595)):
       up = False
    if y == 665 and ((x > 35 and x < 175) or (x > 175 and x < 315) or (x > 315 and x < 385) or (x > 385 and x < 525) or (x > 525 and x < 665)):
       up = False
       
    #LEFT BOUNDARIES
    if x == 35:
       left = False
    if x == 75 and (y > 175 and y < 385):
       left = False
    if x == 105 and ((y == 105) or (y >= 455 and y < 525) or (y == 595)):
       left = False
    if x == 135 and (y > 105 and y < 175):
       left = False
    if x == 145 and (y >= 245 and y <= 315):
       left = False
    if x == 175 and ((y > 385 and y < 455) or (y > 455 and y < 595) or (y > 595 and y < 665)):
       left = False
    if x == 225 and ((y > 175 and y < 245) or (y > 245 and y < 315) or (y > 315 and y < 385)):
       left = False
    if x == 275 and (y > 35 and y < 105):
       left = False
    if x == 295 and (y == 245):
       left = False
    if x == 315 and ((y > 385 and y < 525) or (y > 525 and y < 665)):
       left = False
    if x == 345 and (y > 35 and y < 105):
       left = False
    if x == 375 and ((y > 175 and y < 245) or (y > 245 and y < 385)):
       left = False
    if x == 385 and ((y > 385 and y < 665)):
       left = False
    if x == 525 and ((y > 175 and y < 245) or (y > 245 and y < 385) or (y > 385 and y < 525) or (y > 525 and y < 665)):
       left = False
    if x == 565 and ((y > 105 and y < 175)):
       left = False
    if x == 595 and ((y > 175 and y < 385) or (y > 455 and y < 595)):
       left = False
    if x == 665 and ((y > 35 and y < 175) or (y > 385 and y < 525) or (y > 525 and y < 665)):
       left = False
    
    #RIGHT BOUNDARIES
    if x == 35 and ((y > 35 and y < 175) or (y > 385 and y < 525) or (y > 525 and y < 665)):
        right = False
    if x == 75 and (y > 175 and y < 385):
        right = False
    if x == 105 and (y > 455 and y < 595):
        right = False
    if x == 135 and (y > 105 and y < 175):
        right = False
    if x == 145 and (y > 245 and y < 315):
        right = False
    if x == 175 and ((y > 385 and y < 525) or (y > 525 and y < 665)):
        right = False
    if x == 225 and ((y > 175 and y < 315) or (y > 315 and y <385)):
        right = False
    if x == 275 and (y > 35 and y <= 105):
        right = False
    if x == 315 and (y > 385 and y < 665):
        right = False
    if x == 345 and (y > 35 and y < 105):
        right = False
    if x == 375 and ((y > 175 and y < 315) or (y > 315 and y < 385)) :
        right = False
    if x == 385 and ((y > 385 and y < 525) or (y > 525 and y < 665)):
        right = False
    if x == 525 and ((y > 175 and y < 385) or (y > 385 and y < 455) or (y > 455 and y <595) or (y > 595 and y < 665)) :
        right = False
    if x == 565 and (y > 105 and y < 175):
        right = False
    if x == 595 and ((y == 105) or (y > 175 and y < 385) or (y >= 455 and y < 525) or (y > 525 and y <= 595)):
        right = False
    if x == 665:
        right = False
    
    if left == True:
        moves.append("left")
    if right == True:
        moves.append("right")
    if up == True:
        moves.append("up")
    if down == True:
        moves.append("down")
        
    return moves




def getMovesGhost(a,b): #produces a list of possible moves based on the position of the ghost
    movesGhost = []
    global movesGhost
    
    left = True
    right = True
    down = True
    up = True
    
    # DOWN BOUNDARIES
    if b == 35 and ((a > 35 and a < 275) or (a > 275 and a < 345) or (a > 345 and a < 665)):
        down = False
    if b == 105 and ((a >= 105  and a < 135) or (a > 135 and a <= 275) or (a >= 320 and a < 565) or (a > 565 and a < 595)): 
        down = False
    if b == 175 and ((a == 35) or (a > 75 and a < 225) or (a > 225 and a < 375) or (a > 375 and a < 525) or (a > 525 and a < 595) or (a > 595)):
        down = False
    if b == 245 and ((a > 145 and a < 225) or (a > 295 and a < 375) or (a > 445 and a < 525)):
        down = False
    if b == 315 and ((a >= 145 and a < 225) or (a > 225 and a <= 305) or (a > 375 and a <= 455)):
        down = False 
    if b == 385 and ((a > 35  and a < 175) or (a > 175 and a < 315) or (a > 315 and a < 385) or (a > 385 and a < 525) or (a > 525 and a <665)): 
        down = False
    if b == 455 and ((a > 105  and a < 175) or (a > 525 and a < 595)): 
        down = False
    if b == 525 and ((a > 35  and a < 105) or (a > 175 and a < 315) or (a > 385 and a < 525) or (a > 595 and a < 665)): 
        down = False
    if b == 595 and ((a >= 105  and a < 175) or (a > 525 and a < 595)): 
        down = False
    if b == 665:
        down = False
    
    # UP BOUNDARIES
    if b == 35:
        up = False
    if b == 105 and ((a >= 105 and a < 275 ) or (a > 345 and a < 595)):
        up = False
    if b == 175 and ((a > 35 and a < 135) or (a > 135 and a < 565) or (a > 565 and a < 665)):
       up = False
    if b == 245 and ((a >= 145 and a < 225) or (a >= 295 and a < 375) or (a >= 445 and a <525)):
       up = False
    if b == 315 and ((a > 145 and a < 225) or (a > 225 and a <= 305) or (a > 375 and a <455)):
       up = False
    if b == 385 and ((a == 35) or (a > 75 and a < 225) or (a > 225 and a < 375) or (a > 375 and a <525) or (a > 525 and a < 595) or (a > 595 and a <= 665)):
       up = False
    if b == 455 and ((a >= 105 and a < 175) or (a > 525 and a <= 595)):
       up = False
    if b == 525 and ((a > 35 and a < 105) or (a > 105 and a < 175) or (a > 175 and a < 315) or (a > 315 and a < 385) or (a > 385 and x < 525) or (a > 525 and a < 595) or (x > 595 and x < 665)):
       up = False
    if b == 595 and ((a > 105 and a < 175) or (a > 525 and a < 595)):
       up = False
    if b == 665 and ((a > 35 and a < 175) or (a > 175 and a < 315) or (a > 315 and a < 385) or (a > 385 and a < 525) or (a > 525 and a < 665)):
       up = False
       
    #LEFT BOUNDARIES
    if a == 35:
       left = False
    if a == 75 and (b > 175 and b < 385):
       left = False
    if a == 105 and ((b == 105) or (b >= 455 and b < 525) or (b == 595)):
       left = False
    if a == 135 and (b > 105 and b < 175):
       left = False
    if a == 145 and (b >= 245 and b <= 315):
       left = False
    if a == 175 and ((b > 385 and b < 455) or (b > 455 and b < 595) or (b > 595 and b < 665)):
       left = False
    if a == 225 and ((b > 175 and b < 245) or (b > 245 and b < 315) or (b > 315 and b < 385)):
       left = False
    if a == 275 and (b > 35 and b < 105):
       left = False
    if a == 295 and (b == 245):
       left = False
    if a == 315 and ((b > 385 and b < 525) or (b > 525 and b < 665)):
       left = False
    if a == 345 and (b > 35 and b < 105):
       left = False
    if a == 375 and ((b > 175 and b < 245) or (b > 245 and b < 385)):
       left = False
    if a == 385 and ((b > 385 and b < 665)):
       left = False
    if a == 525 and ((b > 175 and b < 245) or (b > 245 and b < 385) or (b > 385 and b < 525) or (y > 525 and y < 665)):
       left = False
    if a == 565 and ((b > 105 and b < 175)):
       left = False
    if a == 595 and ((b > 175 and b < 385) or (b > 455 and b < 595)):
       left = False
    if a == 665 and ((b > 35 and b < 175) or (b > 385 and b < 525) or (b > 525 and b < 665)):
       left = False
    
    #RIGHT BOUNDARIES
    if a == 35 and ((b > 35 and b < 175) or (b > 385 and b < 525) or (b > 525 and b < 665)):
        right = False
    if a == 75 and (b > 175 and b < 385):
        right = False
    if a == 105 and (b > 455 and b < 595):
        right = False
    if a == 135 and (b > 105 and b < 175):
        right = False
    if a == 145 and (b > 245 and b < 315):
        right = False
    if a == 175 and ((b > 385 and b < 525) or (b > 525 and b < 665)):
        right = False
    if a == 225 and ((b > 175 and b < 315) or (b > 315 and b <385)):
        right = False
    if a == 275 and (b > 35 and b <= 105):
        right = False
    if a == 315 and (b > 385 and b < 665):
        right = False
    if a == 345 and (b > 35 and b < 105):
        right = False
    if a == 375 and ((b > 175 and b < 315) or (b > 315 and b < 385)) :
        right = False
    if a == 385 and ((b > 385 and b < 525) or (b > 525 and b < 665)):
        right = False
    if a == 525 and ((b > 175 and b < 385) or (b > 385 and b < 455) or (b > 455 and b <595) or (b > 595 and b < 665)) :
        right = False
    if a == 565 and (b > 105 and b < 175):
        right = False
    if a == 595 and ((b == 105) or (b > 175 and b < 385) or (b >= 455 and b < 525) or (b > 525 and b <= 595)):
        right = False
    if a == 665:
        right = False
    
    if left == True:
        movesGhost.append("left")
    if right == True:
        movesGhost.append("right")
    if up == True:
        movesGhost.append("up")
    if down == True:
        movesGhost.append("down")
        
    return movesGhost
    print movesGhost

def atOpening(a,b): 
    #Determines whether a ghost is at an opening. 
    #If the function returns True, then the ghost will recalculate it's next move.
    
    movesGhost = getMoves(a,b)
    if len(movesGhost) > 2:  
        return  True
    else:
        return False
    
def getNextDirection(character): 
    #randomly selects a new direction for the ghost to travel in from the list of possible moves. 
    movesGhost = getMoves(character["a"],character["b"])
    if atOpening(character["a"],character["b"]) == True: #selects new direction 
        nextdirection = movesGhost[int(random(0,len(movesGhost)))]
        character["direction"] = nextdirection
        return nextdirection 
    elif atOpening(character["a"],character["b"]) == False:
        nextdirection = character["direction"]
        if nextdirection in movesGhost: #continues in last used direction
            return nextdirection
        else:
            nextdirection = movesGhost[int(random(0,len(movesGhost)))] #selects a new direction if last used direction is no longer an option 
            character["direction"] = nextdirection
            return nextdirection
