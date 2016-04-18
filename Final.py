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