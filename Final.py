"""
Final.py
Author: Daniel Wilson
Credit: Ethan Adner, Mr. D
Assignment:
Write and submit a program that implements the spacewar game:
https://github.com/HHS-IntroProgramming/Spacewar
"""
from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame
from ggame import SoundAsset, Sound, TextAsset, Color
import math
import random
SCREEN_WIDTH = 1250
SCREEN_HEIGHT = 700


class SpaceShip(Sprite):
    """
    Animated space ship
    """
    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", 
        Frame(227,0,292-227,125), 4, 'vertical')

    def __init__(self, position):
        super().__init__(SpaceShip.asset, position)
        self.vx = 0
        self.vy = 0
        self.vr = 0.0
        self.thrust = 0
        self.thrustframe = 1
        #self. circularCollisionModule()
        #self.imagex = 0
        SpaceGame.listenKeyEvent("keydown", "w", self.thrustOn)
        SpaceGame.listenKeyEvent("keyup", "w", self.thrustOff)
        SpaceGame.listenKeyEvent("keydown", "s", self.UPON)
        #SpaceGame.listenKeyEvent("keyup", "s", self.stop)
        SpaceGame.listenKeyEvent("keydown", "a", self.Right)
        SpaceGame.listenKeyEvent("keyup", "a", self.stop)
        SpaceGame.listenKeyEvent("keydown", "d", self.Left)
        SpaceGame.listenKeyEvent("keyup", "d", self.stop)
        self.fxcenter = self.fycenter = 0.5


    def step(self):
        self.x += self.vx
        self.y += self.vy
        self.rotation += self.vr
        #self.explode(self.x, self.y)
        if self.thrust == 1:
            self.setImage(self.thrustframe)
            self.thrustframe += 1
            self.vx += 0.1*math.cos(self.rotation+1/2*math.pi)
            self.vy += 0.1*math.sin(self.rotation-1/2*math.pi)
            if self.thrustframe == 4:
                self.thrustframe = 1
            else:
                self.setImage(0)
        col=self.collidingWithSprites(Asteroid)
        if col:
            print("boom")
            self.explode(self)
            

    def thrustOn(self, event):
        self.thrust = 1

    def thrustOff(self, event):
        self.thrust = 0

    def UPON(self, event):
        self.vy=1 
    def DOWNON(self, event):
        self.vy=-1
    def Right(self, event):
        self.vr = .1
    def Left(self, event):
        self.vr = -.1
    def stop(self, event):
        self.vr=0
        self.vx=0
        self.vy=0

    def explode(self, event):
        self.visible = False
        self.vx=0
        self.vy=0
        ExplosionSmall(self.position)
        
        
class ExplosionSmall(Sprite):
    
    asset = ImageAsset("images/explosion1.png", Frame(0,0,128,128), 10)
    boomasset = SoundAsset("sounds/explosion1.mp3")
    
    def __init__(self, position):
        super().__init__(ExplosionSmall.asset, position)
        self.image = 0
        self.center = (0.5, 0.5)
        self.boom = Sound(ExplosionSmall.boomasset)
        self.boom.play()
        
        
    def step(self):
        self.setImage(self.image//2)  # slow it down
        self.image = self.image + 1
        if self.image == 20:
            self.destroy()

lvl = int(input("What is your level? "))

#randomizing the spawn point of the asteroid 
nums=lvl
ov=lvl*2

if nums>=6 and nums<=10:
    numbs=nums+1
    numbes=0
    nums=5
elif nums>=11:
    numbes=nums+1
    numbs=12
    nums=5
else:
    numbs=0
    numbes=0
saved=[]
while nums >=1:
    h=1
    while h==1:
        b=random.randint(1,1230)
        c=random.randint(1,700)
        d=random.randint(1,1230)
        e=random.randint(1,700)
        if b<=1220 and d<=1220 and e<=5 and c<=5:
            h=0
            j=(b,c)
            k=(d,e)
            saved.append((j))
            saved.append((k))
            

        elif b<=5 and d<=5 and e<=700 and c<=700:
            j=(b,c)
            k=(d,e)
            saved.append((j))
            saved.append((k))
        
        elif b>=1221 and d>=1221 and e<=350 and c<=700 and c>=350:
            j=(b,c)
            k=(d,e)
            saved.append((j))
            saved.append((k))
            

        else:
            h=1
    nums=nums-1

while numbs >=8:
    h=1
    while h==1:
        b=random.randint(1,1000)
        c=random.randint(1,700)
        d=random.randint(1,1000)
        e=random.randint(1,700)
        if b<=1250 and d<=1250 and e<=5 and c<=5:
            h=0
            j=(b,c)
            k=(d,e)
            saved.append((j))
            saved.append((k))
            

        elif b<=5 and d<=5 and e<=700 and c<=700:
            h=0
            j=(b,c)
            k=(d,e)
            saved.append((j))
            saved.append((k))

        elif b>=1221 and d>=1221 and e<=350 and c<=700 and c>=350:
            j=(b,c)
            k=(d,e)
            saved.append((j))
            saved.append((k))

        else:
            h=1
    numbs=numbs-1

while numbes >=12:
    h=1
    while h==1:
        b=random.randint(1,1000)
        c=random.randint(1,700)
        d=random.randint(1,1000)
        e=random.randint(1,700)
        if b<=1250 and d<=1250 and e<=5 and c<=5:
            h=0
            j=(b,c)
            k=(d,e)
            saved.append((j))
            saved.append((k))
            

        elif b<=5 and d<=5 and e<=700 and c<=700:
            h=0
            j=(b,c)
            k=(d,e)
            saved.append((j))
            saved.append((k))
            

        else:
            h=1
    numbes=numbes-1

print(saved)

numas=lvl
m=0
n=1
while numas != 0:
    l=saved[m]
    o=saved[n]
    m=m+2
    n=n+2
    numas=numas-1
    print(l)
    print(o)

p=random.randint(1,10)
class Asteroid(Sprite):
    
    asset5 = ImageAsset("images/Asteroid.png")
    def __init__(self, position):
        super().__init__(Asteroid.asset5, position)
        if position >= (1245,6) and position <= (1250,700):
            if position >= (1245,6) and position <= (1250,100):
                u = random.randint(1,5)
                self.vx = (-.5)*u
                self.vy = (random.randint(40,80)/100)*u
                self.t=0
                #make a randomizer for speed of slope => radians(random.int(90,180))
                self.vr = 0.01
                self.thrust = 10
                self.thrustframe = 10

            if position >= (1245,101) and position <= (1250,200):
                u = random.randint(1,5)
                self.vx = (-.5)*u
                self.vy = (random.randint(40,80)/100)*u
                self.t=0
                #make a randomizer for speed of slope => radians(random.int(90,180))
                self.vr = 0.01
                self.thrust = 10
                self.thrustframe = 10
                
            if position >= (1245,201) and position <= (1250,400):
                u = random.randint(1,5)
                self.vx = (-.5)*u
                s=random.randint(1,10)
                if s == 5:
                    self.vx = (-random.randint(0,5)/100)*u
                else:
                    self.vy = (random.randint(20,40)/100)*u
                self.t=0
                #make a randomizer for speed of slope => radians(random.int(90,180))
                self.vr = 0.01
                self.thrust = 10
                self.thrustframe = 10
                
            if position >= (1245,401) and position <= (1250,500):
                u = random.randint(1,5)
                self.vx = (-.5)*u
                self.vy = (-random.randint(20,40)/100)*u
                self.t=0
                #make a randomizer for speed of slope => radians(random.int(90,180))
                self.vr = 0.01
                self.thrust = 10
                self.thrustframe = 10
                
                
            if position >= (1245,501) and position <= (1250,700):
                u = random.randint(1,5)
                self.vx = (-.5)*u
                self.vy = (-random.randint(0,10)/100)*u
                self.t=0
                #make a randomizer for speed of slope => radians(random.int(90,180))
                self.vr = 0.01
                self.thrust = 10
                self.thrustframe = 10
                
        
        if position >= (0,6) and position <=(5,700):
            if position >= (0,6) and position <= (5,100):
                u = random.randint(1,5)
                self.vx = (.5)*u
                self.vy = (random.randint(40,80)/100)*u
                self.t=0
                #make a randomizer for speed of slope => radians(random.int(90,180))
                self.vr = 0.01
                self.thrust = 10
                self.thrustframe = 10

            if position >= (0,101) and position <= (5,200):
                u = random.randint(1,5)
                self.vx = (.5)*u
                self.vy = (random.randint(40,80)/100)*u
                self.t=0
                #make a randomizer for speed of slope => radians(random.int(90,180))
                self.vr = 0.01
                self.thrust = 10
                self.thrustframe = 10
                
            if position >= (0,201) and position <= (5,400):
                u = random.randint(1,5)
                self.vx = (.5)*u
                s=random.randint(1,10)
                if s == 5:
                    self.vx = (-random.randint(0,5)/100)*u
                else:
                    self.vy = (random.randint(20,40)/100)*u
                self.t=0
                #make a randomizer for speed of slope => radians(random.int(90,180))
                self.vr = 0.01
                self.thrust = 10
                self.thrustframe = 10
                
            if position >= (0,401) and position <= (5,500):
                u = random.randint(1,5)
                self.vx = (.5)*u
                self.vy = (-random.randint(20,40)/100)*u
                self.t=0
                #make a randomizer for speed of slope => radians(random.int(90,180))
                self.vr = 0.01
                self.thrust = 10
                self.thrustframe = 10
                
                
            if position >= (0,501) and position <= (5,700):
                u = random.randint(1,5)
                self.vx = (.5)*u
                self.vy = (-random.randint(0,10)/100)*u
                self.t=0
                #make a randomizer for speed of slope => radians(random.int(90,180))
                self.vr = 0.01
                self.thrust = 10
                self.thrustframe = 10
                
                
        
        elif position >= (0,0) and position <= (1250,5):
            if position >= (0,0) and position <= (100,5):
                u = random.randint(1,5)
                self.vx = (random.randint(30,70)/100)*u
                self.vy = (.5)*u
                self.t=0
                #make a randomizer for speed of slope => radians(random.int(90,180))
                self.vr = 0.01
                self.thrust = 10
                self.thrustframe = 10
                
                
            if position >= (101,0) and position <= (200,5):
                u = random.randint(1,5)
                self.vx = (random.randint(30,55)/100)*u
                self.vy = (.5)*u
                self.t=0
                #make a randomizer for speed of slope => radians(random.int(90,180))
                self.vr = 0.01
                self.thrust = 10
                self.thrustframe = 10
                
    
            if position >= (201,0) and position <=(300,5):
                u = random.randint(1,5)
                self.vx = (random.randint(10,40)/100)*u
                self.vy = (.5)*u
                self.t=0
                #make a randomizer for speed of slope => radians(random.int(90,180))
                self.vr = 0.01
                self.thrust = 10
                self.thrustframe = 10
                
                
            if position >= (301,0) and position <=(400,5):
                u = random.randint(1,5)
                self.vx = (random.randint(10,30)/100)*u
                self.vy = (.5)*u
                self.t=0
                self.vr = 0.01
                self.thrust = 10
                self.thrustframe = 10
                
            
            if position >= (401,0) and position <=(500,5):
                u = random.randint(1,5)
                q=random.randint(0,10)
                if q == 5:
                    self.vx = -random.randint(0,5)/100
                else:
                    self.vx = random.randint(0,20)/100
                self.vy = (.5)*u
                self.t=0
                self.vr = 0.01
                self.thrust = 10
                self.thrustframe = 10
                
    
            if position >= (501,0) and position <=(600,5):
                u = random.randint(1,5)
                self.vx = 0
                self.vy = (.5)*u
                self.t=0
                self.vr = 0.01
                self.thrust = 10
                self.thrustframe = 10
                
    
            if position >= (601,0) and position <=(700,5):
                u = random.randint(1,5)
                q=random.randint(0,10)
                if q == 5:
                    self.vx = (random.randint(0,5)/100)*u
                else:
                    self.vx = (-random.randint(0,20)/100)*u
                self.vy = (.5)*u
                self.t=0
                #make a randomizer for speed of slope => radians(random.int(90,180))
                self.vr = 0.01
                self.thrust = 10
                self.thrustframe = 10
                
    
            if position >= (701,0) and position <=(800,5):
                u = random.randint(1,5)
                self.vx = (-random.randint(10,30)/100)*u
                self.vy = (.5)*u
                self.t=0
                #make a randomizer for speed of slope => radians(random.int(90,180))
                self.vr = 0.01
                self.thrust = 10
                self.thrustframe = 10
                
    
            if position >= (801,0) and position <=(900,5):
                u = random.randint(1,5)
                self.vx = (-random.randint(15,30)/100)*u
                self.vy = (.5)*u
                self.t=0
                #make a randomizer for speed of slope => radians(random.int(90,180))
                self.vr = 0.01
                self.thrust = 10
                self.thrustframe = 10
                
                
            if position >= (901,0) and position <= (1000,5):
                u = random.randint(1,5)
                self.vx = (-random.randint(30,60)/100)*u
                self.vy = (.5)*u
                self.t=0
                #make a randomizer for speed of slope => radians(random.int(90,180))
                self.vr = 0.01
                self.thrust = 10
                self.thrustframe = 10
                
            
            if position >= (1001,0) and position <= (1100,5):
                u = random.randint(1,5)
                self.vx = (-random.randint(40,60)/100)*u
                self.vy = (.5)*u
                self.t=0
                #make a randomizer for speed of slope => radians(random.int(90,180))
                self.vr = 0.01
                self.thrust = 10
                self.thrustframe = 10
                
    
            if position >= (1101,0):
                u = random.randint(1,5)
                self.vx = (-random.randint(40,60)/100)*u
                self.vy = (.5)*u
                self.t=0
                #make a randomizer for speed of slope => radians(random.int(90,180))
                self.vr = 0.01
                self.thrust = 10
                self.thrustframe = 10
                
        
        ov=lvl*2
        if position >= (0,0) and position <= (1255, 705):
            ov=ov
        else:
            ov=ov-1
            print(ov)
            
    def step(self):
        if p==5:
            self.t += .1
            self.x += 1.5*math.cos(self.t) + 0.5*self.vx
            self.y += 1.5*math.sin(self.t) + 0.5*self.vy
            self.rotation += self.vr
        if p==6:
            self.t += .1
            self.x += 2*self.vx
            self.y += 2*math.sin(self.t) + self.vy
            self.rotation += self.vr
        else:
            self.x += self.vx
            self.y += self.vy
            self.rotation += self.vr
        
        if self.thrust == 1:
            #self.setImage(self.thrustframe)
            self.thrustframe += 1
            if self.thrustframe == 4:
                self.thrustframe = 1
        else:
            self.setImage(0)

    def thrustOn(self, event):
        self.thrust = 1

    def thrustOff(self, event):
        self.thrust = 0

    
class SpaceGame(App):
    """
    Tutorial4 space game example.
    """
    def __init__(self, width, height):
        super().__init__(width, height)
        black = Color(0, 1)
        noline = LineStyle(0, black)
        bg_asset = ImageAsset("images/starfield.jpg")
        bg1 = Sprite(bg_asset, (0,0))
        bg2 = Sprite(bg_asset, (512,0))
        bg3 = Sprite(bg_asset, (0, 512))
        bg4 = Sprite(bg_asset, (512, 512)) 
        bg5 = Sprite(bg_asset, (1024, 512))
        bg6 = Sprite(bg_asset, (1024, 0))
        SpaceShip((600,400))
        
        
        numas=lvl
        m=0
        n=1
        while numas != 0:
            l=saved[m]
            o=saved[n]
            Asteroid(o)
            Asteroid(l)
            m=m+2
            n=n+2
            numas=numas-1

    def step(self):
        for ship in self.getSpritesbyClass(SpaceShip):
            ship.step()
        for explosion in self.getSpritesbyClass(ExplosionSmall):
            explosion.step()
        for asteroid in self.getSpritesbyClass(Asteroid):
            asteroid.step()

    def registerKeys(self, keys):
        commands = ["left", "right", "forward", "fire"]
        self.keymap = dict(zip(keys, commands))
        [self.app.listenKeyEvent("keydown", k, self.controldown) for k in keys]
        [self.app.listenKeyEvent("keyup", k, self.controlup) for k in keys]



myapp = SpaceGame(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()
