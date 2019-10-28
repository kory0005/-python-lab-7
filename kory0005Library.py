import math
import random
import time,click
from gfxhat import touch, lcd, backlight, fonts
from PIL import Image, ImageFont, ImageDraw
import sys, os


#function calculates circle area
def circleArea(arg1):
    area = math.pi * arg1**2
    return area


#function calculates mpg
def mpgMeasure(arg1, arg2):
    mpg = arg1/arg2
    return mpg


#function translates temperature from farenheits to celsius
def temperature(t):
    c = (t - 32) * 5/9
    return c


#function calculates calculate distance between points
def calculateDistanceBetweenPoints(a, b, a1, b1):
    d = float(math.sqrt((b-a)**2 + (b1-a1)**2))
    return d


# function displays a vertical line at a given x coordinate on the gfx hat.
def verticalLine(arg1, arg2):
    while(arg2 <= 63):
        lcd.set_pixel(arg1, arg2, 1)
        arg2 = arg2 + 1
    lcd.show()
    return (arg2)


# function displays a horizontal line at a given y coordinate.
def horizontalLine(arg1, arg2):
    while(arg1 <= 127):
        lcd.set_pixel(arg1, arg2, 1)
        arg1 = arg1 + 1
    lcd.show()
    return(arg1)


# function displays random pixel on the screen for a given period of time specifies in seconds.
def randomPixel(counter):
    while (counter <= 4):
        lcd.set_pixel(random.randrange(1, 128, 1), random.randrange(1, 64, 1), 1)
        time.sleep(2)
        lcd.show()
        # lcd.clear()
    return(counter)


# function changes the backlight color
def changeBacklight():
    while True:
        backlight.set_all(191, 0, 255)
        time.sleep(5)
        backlight.show()
    return ()


#fubction to setup backlight color
def setupBacklight():
    while True:
        backlight.set_all(191, 0, 255)
        backlight.show()
    return ()


# function resets the backlight color
def clearBacklight():
    backlight.set_all(0, 0, 0)
    backlight.show()


# function creates a staircase
def oneStep(x, y, w = 20, h = 127, SW = 127, SH = 63):
    for i in range (h):
        if y >= 0:
            lcd.set_pixel(x, y-i, 1)
        else:
            h = 1
    for j in range(0, w):
        if x + j <= SW:
            lcd.set_pixel(x+j, y-h, 1)
        else:
            w = h
    return (x + w, y - h)

def stairCase(x = 20, y = 63, w = 10, h = 10):
    while (x + y < 127 and y - h >= 0):
        x, y = oneStep(x, y, w, h)


#function displays text
def displayText(text,lcd,x,y):
    width, height = lcd.dimensions()
    image = Image.new('P', (width, height))
    draw = ImageDraw.Draw(image)
    # font = ImageFont.truetype(fonts.AmaticSCBold, 38)  
    font = ImageFont.load_default()
    w, h = font.getsize(text)
    draw.text((x,y), text, 1, font)
    for x1 in range(x,x+w):
        for y1 in range(y,y+h):
            pixel = image.getpixel((x1, y1))
            lcd.set_pixel(x1, y1, pixel)
    lcd.show()


#function to use gfxhat buttons
def handler(channel, event):
    global y, x
    print("Got {} on channel {}".format(event, channel))
    if (channel == 2 and event == 'press'): #  QUIT
        print("QUIT")
        lcd.clear()
        lcd.show()
        os._exit(1)
    elif (channel == 4 and event == 'press'): # RESET
        x = 60
        y = 30
        lcd.clear()
        lcd.set_pixel(x, y, 1)
        displayText('Etch a Sketch', lcd, 20, 10)
    elif (channel == 1 and event == 'press'): # DOWN
        y = y + 1
        if y > 63:
            y = 0
        lcd.set_pixel(x, y, 1)
    elif (channel == 0 and event == 'press'): # UP
        y = y - 1   
        if y < 0:
            y = 63
        lcd.set_pixel(x, y, 1)
    elif (channel == 3 and event == 'press'): # LEFT
        x = x - 1
        if x < 0:
            x = 127  
        lcd.set_pixel(x, y, 1) 
    elif (channel == 5 and event == 'press'): # RIGHT
        x = x + 1
        if x > 127:
            x = 0   
        lcd.set_pixel(x, y, 1) 
    lcd.show()


#function to clear screen
def eraseObject():
  lcd.clear()
  lcd.show()


#function displays an object
def displayObject(obj,x,y):
    i=0
    for line in obj:
        j=0
        for pixel in line:
            if (x+j>=123 or x+j<0):
                break
            if (y+i>=64 or y+i<0):
                break
            lcd.set_pixel(x+j,y+i,pixel)
            j=j+1
        i=i+1
    lcd.show()


#move object
def moveObject(obj):    
    # global x,y,vx,vy
    #Bouncing ball
    x=y=0
    vx=vy=3
    x=x+vx
    y=y+vy
    if (x<0 or x>127):
        vx=-vx
        x=x+vx
    if (y<0 or y>62):
        vy=-vy
        y=y+vy
    lcd.show()