#!/usr/bin/env python

import pigpio
import time
import requests
import os

pi = pigpio.pi()
#assocated pins on raspberry pi
r = 17
g = 22
b = 24

class rgb:
    def __init__(self, redDiode, greenDiode, blueDiode):
        pi.set_PWM_dutycycle(r, redDiode)
        pi.set_PWM_dutycycle(g, greenDiode)
        pi.set_PWM_dutycycle(b, blueDiode)
        redDiode = 0
        greenDiode = 0
        blueDiode = 0

    def off(self):
        self.redDiode = 0
        self.greenDiode = 0
        self.blueDiode = 0
        self.change()
        return self.redDiode, self.greenDiode, self.blueDiode

    def red(self):
        self.redDiode = 255
        self.greenDiode = 0
        self.blueDiode = 0
        self.change()
        return self.redDiode, self.greenDiode, self.blueDiode
    
    def green(self):
        self.redDiode = 0
        self.greenDiode = 255
        self.blueDiode = 0
        self.change()
        return self.redDiode, self.greenDiode, self.blueDiode
    
    def blue(self):
        self.redDiode = 0
        self.greenDiode = 0
        self.blueDiode = 255
        self.change()
        return self.redDiode, self.greenDiode, self.blueDiode
    
    def magenta(self):
        self.redDiode = 255
        self.greenDiode = 0
        self.blueDiode = 255
        self.change()
        return self.redDiode, self.greenDiode, self.blueDiode
    
    def cyan(self):
        self.redDiode = 0
        self.greenDiode = 255
        self.blueDiode = 255
        self.change()
        return self.redDiode, self.greenDiode, self.blueDiode
    
    def yellow(self):
        self.redDiode = 255
        self.greenDiode = 255
        self.blueDiode = 0
        self.change()
        return self.redDiode, self.greenDiode, self.blueDiode
    
    def white(self):
        self.redDiode = 255
        self.greenDiode = 255
        self.blueDiode = 255
        self.change()
        return self.redDiode, self.greenDiode, self.blueDiode
    
    def addRed(self):
        self.redDiode += 15
        self.change()
        return self.redDiode
    
    def subRed(self):
        self.redDiode -= 15
        self.change()
        return self.redDiode
    
    def addGreen(self):
        self.greenDiode += 15
        self.change()
        return self.greenDiode

    def subGreen(self):
        self.greenDiode -= 15
        self.change()
        return self.greenDiode

    def addBlue(self):
        self.blueDiode += 15
        self.change()
        return self.blueDiode

    def subBlue(self):
        self.blueDiode -= 15
        self.change()
        return self.blueDiode

    #updates current state of color
    def change(self):
        if self.redDiode < 0:
            self.redDiode = 0
        if self.redDiode > 255:
            self.redDiode = 255
        if self.greenDiode < 0:
            self.greenDiode = 0
        if self.greenDiode > 255:
            self.greenDiode = 255
        if self.blueDiode < 0:
            self.blueDiode = 0
        if self.blueDiode > 255:
            self.blueDiode = 255
        pi.set_PWM_dutycycle(r, self.redDiode)
        pi.set_PWM_dutycycle(g, self.greenDiode)
        pi.set_PWM_dutycycle(b, self.blueDiode)
        return self.redDiode, self.greenDiode, self.blueDiode

#clears screen
def cls():
    os.system(['clear','cls'][os.name == 'nt'])

#writes a method to text file that executable is this scope
#for when progam crashes or ends
reset = open("/var/www/html/color.txt", "w")
reset.write("c.off()")
reset.close()
    
c = rgb(0,0,0)
while True:
    cls()
    print('LED Working')

    colorSet = open("/var/www/html/color.txt", "r")
    exec(colorSet)
    print(c.redDiode, c.greenDiode, c.blueDiode)

    #for the purpose of incrementing only once per button press
    with open('/var/www/html/color.txt') as colorFile:
        if 'c.change()' not in colorFile.read():
            resume = open("/var/www/html/color.txt", "w")
            resume.write("c.change()")
            resume.close()

    #writes brightness of diodes to a text file for HTML to read
    #and then display on the interface
    with open('/var/www/html/status.html') as statusFile:
        if 'color status: ' + str(c.redDiode) + ', ' + str(c.greenDiode) + ', ' + str(c.blueDiode) not in statusFile.read():
            updateStatus = open("/var/www/html/status.html", "w")
            updateStatus.write('<html><body><style type="text/css"> h1{background-color: black; font-family: Arial, Verdana, sans-serif; font-size: 300%; color: white;}</style><h1> color status: ' + str(c.redDiode) + ', ' + str(c.greenDiode) + ', ' + str(c.blueDiode) + '<h1></body></html>')
            updateStatus.close()


