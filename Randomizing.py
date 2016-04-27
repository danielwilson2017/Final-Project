

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

while nums >=1:
    h=1
    while h==1:
        b=random.randint(1,1000)
        c=random.randint(1,700)
        d=random.randint(1,1000)
        e=random.randint(1,700)
        if b<=1250 and d<=1250 and e<=5 and c<=5:
            h=0
            f=(b,d)
            g=(c,e)
            h=list(zip(f,g))
            print(h)
            m=random.randint(1,5)
            if m<=3:
                j=h[0:1]
                k=h[1:2]
            else:
                k=h[0:1]
                j=h[1:2]
            print(j)
            print(k)
        else:
            h=1
    nums=nums-1
            
'''
        elif b<=5 and c<=700:
            h=0
            print(b,c)

        else:
            h=1
    nums=nums-1
'''