

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
nums=lvl

h=1
while h==1:
    b=random.randint(1,1000)
    c=random.randint(1,700)
    if b<=1250 and c<=5:
        h=0
        print(b,c)
    elif b<=5 and c<=700:
        h=0
        print(b,c)
    else:
        h=1
        #print(b,c)
