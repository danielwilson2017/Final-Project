

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
if nums>=5:
    numbs=nums+1
    nums=5

saved=[]

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
            saved.append((h))
            

        elif b<=5 and d<=5 and e<=700 and c<=700:
            h=0
            f=(b,d)
            g=(c,e)
            h=list(zip(f,g))
            saved.append((h))
            

        else:
            h=1
    nums=nums-1

print(saved)
saved2=[]

while numbs >=5:
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
            saved2.append((h))
            

        elif b<=5 and d<=5 and e<=700 and c<=700:
            h=0
            f=(b,d)
            g=(c,e)
            h=list(zip(f,g))
            saved2.append((h))
            

        else:
            h=1
    nums=nums-1

print(saved2)
