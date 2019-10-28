from kory0005Library import displayObject,eraseObject
from gfxhat import lcd

    
ball = [
[0,0,0,1,1,0,0,0],
[0,0,1,1,1,1,0,0],
[0,1,1,1,1,1,1,0],
[0,1,1,1,1,1,1,0],
[0,1,1,1,1,1,1,0],
[0,1,1,1,1,1,1,0],
[0,0,1,1,1,1,0,0],
[0,0,0,1,1,0,0,0]
]


x=y=0
w=h=8
vx=vy=3


#Move ball
def moveObject(obj):    
    global x,y,vx,vy
    #Bouncing ball
    x=x+vx
    y=y+vy
    if (x<0 or x>127):
        vx=-vx
        x=x+vx
    if (y<0 or y>62):
        vy=-vy
        y=y+vy
    lcd.show()


while True:
    eraseObject()
    displayObject(ball,x,y)
    moveObject(ball)
    lcd.show()
