import pigpio
import time
import requests
import os

pi = pigpio.pi()
r = 17
g = 22
b = 24

ared = 0
agreen = 0
ablue = 0

rgb = [0, 0, 0]

def colorSet(color, brightness):
    pi.set_PWM_dutycycle(color, brightness)

def color(ared, agreen, ablue):
    if ared < 0:
        ared = 0
    if ared > 255:
        ared = 255
    if agreen < 0:
        agreen = 0
    if agreen > 255:
        agreen = 255
    if ablue < 0:
        ablue = 0
    if ablue > 255:
        ablue = 255
        
    pi.set_PWM_dutycycle(r, ared)
    pi.set_PWM_dutycycle(g, agreen)
    pi.set_PWM_dutycycle(b, ablue)
    return (ared, agreen, ablue)

def off():
    stop = True
    pi.set_PWM_dutycycle(r, 0)
    pi.set_PWM_dutycycle(g, 0)
    pi.set_PWM_dutycycle(b, 0)
    rgb = [0, 0, 0]
    return rgb

def red():
    pi.set_PWM_dutycycle(r, 255)
    pi.set_PWM_dutycycle(g, 0)
    pi.set_PWM_dutycycle(b, 0)
    rgb = [255, 0, 0]
    return rgb

def green():
    pi.set_PWM_dutycycle(r, 0)
    pi.set_PWM_dutycycle(g, 255)
    pi.set_PWM_dutycycle(b, 0)
    rgb = [0, 255, 0]
    return rgb
def blue():
    pi.set_PWM_dutycycle(r, 0)
    pi.set_PWM_dutycycle(g, 0)
    pi.set_PWM_dutycycle(b, 255)
    rgb = [0, 0, 255]
    return rgb

def purple():
    pi.set_PWM_dutycycle(r, 255)
    pi.set_PWM_dutycycle(g, 0)
    pi.set_PWM_dutycycle(b, 255)
    rgb = [255, 0, 255]
    return rgb

def cyan():
    pi.set_PWM_dutycycle(r, 0)
    pi.set_PWM_dutycycle(g, 255)
    pi.set_PWM_dutycycle(b, 255)
    rgb = [0, 255, 255]
    return rgb

def yellow():
    pi.set_PWM_dutycycle(r, 255)
    pi.set_PWM_dutycycle(g, 255)
    pi.set_PWM_dutycycle(b, 0)
    rgb = [255, 255, 0]
    return rgb

def white():
    pi.set_PWM_dutycycle(r, 255)
    pi.set_PWM_dutycycle(g, 255)
    pi.set_PWM_dutycycle(b, 255)
    rgb = [255, 255, 255]
    return rgb

##def jump3():
##    while True: 
##        red()
##        time.sleep(.1)
##        green()
##        time.sleep(.1)
##        blue()
##        time.sleep(.1)
##        x = colorSet;
##        if x != 'jump3()':
##            break
##        #make a fuction to maunually change time interval

##def fadeBlue():
##    bright = 255
##    pi.set_PWM_dutycycle(b, bright)
##    while bright > 0:
##        bright -= 1
##        pi.set_PWM_dutycycle(b, bright)
##        time.sleep(.5)
##    while bright <= 255:
##        bright += 1
##        pi.set_PWM_dutycycle(b, bright)
##        time.sleep(.5)
        
def updateColor(deltaR, deltaG, deltaB): #get this figured out
    ared += deltaR
    agreen += deltaG
    ablue += deltaB
    
    if ared < 0:
        ared = 0
    if ared > 255:
        ared = 255
    if agreen < 0:
        agreen = 0
    if agreen > 255:
        agreen = 255
    if ablue < 0:
        ablue = 0
    if ablue > 255:
        ablue = 255
        
    pi.set_PWM_dutycycle(r, ared)
    pi.set_PWM_dutycycle(g, agreen)
    pi.set_PWM_dutycycle(b, ablue)



def cls():
    os.system(['clear','cls'][os.name == 'nt'])

#for running through command line
#input('Set ')
#while True:
#        input('Set ')      

class changeColor:
    def __init__(self, r, g, b):
##        self.r = rbrightness
##        self.g = gbrightness
##        self.b = bbrightness
        self.r = rgb[0]
        self.g = rgb[1]
        self.b = rgb[2]
    def addRed(self):
        self.r += 15
        return self.r
    def subRed(self):
        self.r -= 15
        return self.r
    def addGreen(self):
        self.g += 15
        return self.g
    def subGreen(self):
        self.g -= 15
        return self.g
    def addBlue(self):
        self.b += 15
        return self.b
    def subBlue(self):
        self.b -= 15
        return self.b
    def change(self):
        if self.r < 0:
            self.r = 0
        if self.r > 255:
            self.r = 255
        if self.g < 0:
            self.g = 0
        if self.g > 255:
            self.g = 255
        if self.b < 0:
            self.b = 0
        if self.b > 255:
            self.b = 255
        pi.set_PWM_dutycycle(r, self.r)
        pi.set_PWM_dutycycle(g, self.g)
        pi.set_PWM_dutycycle(b, self.b)

while True:
    cls()
    print('LED Working')
    
    c = changeColor(rgb[0], rgb[1], rgb[2])
    colorSet = open("/var/www/html/color.txt", "r")
    exec colorSet


    
##<script type="text/javascript">
##    function addRed(){
##        $.get("addRed.php");
##        return false;
##    }
##</script>
##<a href="#" onclick="addRed();">
##    <img src="red.png" border="0">
##</a><br>
##
##<script type="text/javascript">
##    function addGreen(){
##        $.get("addGreen.php");
##        return false;
##    }
##</script>
##<a href="#" onclick="addGreen();">
##    <img src="green.png" border="0">
##</a><br>
##
##<script type="text/javascript">
##    function addBlue(){
##        $.get("addBlue.php");
##        return false;
##    }
##</script>
##<a href="#" onclick="addBlue();">
##    <img src="blue.png" border="0">
##</a><br>
    
    
