"""
spaceshooter.py
Author: Daniel Wilson
Credit: Ethan Adner, Mr. D
Assignment:
Write and submit a program that implements the spacewar game:
https://github.com/HHS-IntroProgramming/Spacewar
"""
from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame
from ggame import SoundAsset, Sound, TextAsset, Color
import math
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
            self.vx += 0.03*math.cos(self.rotation+1/2*math.pi)
            self.vy += 0.03*math.sin(self.rotation-1/2*math.pi)
            if self.thrustframe == 4:
                self.thrustframe = 1
            else:
                self.setImage(0)
        col=self.collidingWithSprites(Sun)
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
        SpaceShip((100,100))
        Sun((500,300))

        

    def step(self):
        for ship in self.getSpritesbyClass(SpaceShip):
            ship.step()
        for explosion in self.getSpritesbyClass(ExplosionSmall):
            explosion.step()

    def registerKeys(self, keys):
        commands = ["left", "right", "forward", "fire"]
        self.keymap = dict(zip(keys, commands))
        [self.app.listenKeyEvent("keydown", k, self.controldown) for k in keys]
        [self.app.listenKeyEvent("keyup", k, self.controlup) for k in keys]


class Sun(Sprite):
    
    asset5 = ImageAsset("images/sun.png")
    height = 90
    width = 40
    
    def __init__(self, position):
        super().__init__(Sun.asset5, position)
        
        
    

myapp = SpaceGame(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()