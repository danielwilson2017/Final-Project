
"""
tutorial4.py
by E. Dennison
"""
from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame
import random

SCREEN_WIDTH = 1250
SCREEN_HEIGHT = 700

lvl = int(input("What is your level? "))
#randomizing the spawn point of the asteroid 
h=1

while h==1:
    b=random.randint(1,100)
    c=random.randint(1,100)
    if b<=50 and c<=5:
        h=0
        print(b,c)
    elif b<=5 and c<=50:
        h=0
        print(b,c)
    else:
        h=1
        print(b,c)

class Asteroid(Sprite):
    
    asset5 = ImageAsset("images/Asteroid.png")
    def __init__(self, position):
        super().__init__(Asteroid.asset5, position)
        self.vx = .5
        self.vy = 0.5
        self.vr = 0.01
        self.thrust = 1
        self.thrustframe = 1
        #self.fxcenter = self.fycenter = 0.5
        
        
        
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
        
        
        numas=lvl
        if numas == 1 :
            Asteroid((b,c))
        elif numas >= 1:
            Asteroid((500,400))
            Asteroid((500,200))

    def step(self):
        for ship in self.getSpritesbyClass(Asteroid):
            ship.step()


myapp = SpaceGame(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()