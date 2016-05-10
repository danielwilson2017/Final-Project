
"""
tutorial4.py
by E. Dennison
"""
from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame
import random
import math

SCREEN_WIDTH = 1250
SCREEN_HEIGHT = 700



lvl = int(input("What is your level? "))
#randomizing the spawn point of the asteroid 
nums=lvl
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

class Asteroid(Sprite):
    
    asset5 = ImageAsset("images/Asteroid.png")
    def __init__(self, position):
        super().__init__(Asteroid.asset5, position)
        if position ==(250,5):
            
            self.vx = .5
            self.vy = (math.sin(math.radians(180)))
            #make a randomizer for speed of slope => radians(random.int(90,180))
            self.vr = 0.01
            self.thrust = 10
            self.thrustframe = 10
            print(self.vy)
        '''
        if position <=(250,5):
            self.vx = .5
            self.vy = 0.5
            self.vr = 0.01
            self.thrust = 10
            self.thrustframe = 10
        elif position >=(250,5) and position<=(500,5):
            self.vx = .25
            self.vy = 0.5
            self.vr = 0.01
            self.thrust = 10
            self.thrustframe = 10
        elif position >=(501,5) and position <=(700,5):
            self.vx = 0
            self.vy = 0.5
            self.vr = 0.01
            self.thrust = 10
            self.thrustframe = 10
        elif position >=(701,5) and position <=(800,5):
            self.vx = -.25
            self.vy = 0.5
            self.vr = 0.01
            self.thrust = 10
            self.thrustframe = 10
        elif position >=(801,5) and position <=(900,5):
            self.vx = -.1
            self.vy = 0.5
            self.vr = 0.01
            self.thrust = 10
            self.thrustframe = 10
        elif position >=(901,5):
            self.vx = -.25
            self.vy = 0.5
            self.vr = 0.01
            self.thrust = 10
            self.thrustframe = 10
        '''
        

        
        
        
    def step(self):
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
        Asteroid((250,5))
        '''
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
        '''

    def step(self):
        for ship in self.getSpritesbyClass(Asteroid):
            ship.step()


myapp = SpaceGame(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()