from easygui import *
from gopigo import*
from time import*
#file needs to be run under sudo (superadmin)
import usb  
import sys  
import time
from subprocess import call

#MISSILE CODE
device = usb.core.find(idVendor=0x2123, idProduct=0x1010)  
# On Linux we need to detach usb HID first  
try:  
  device.detach_kernel_driver(0)  
# except Exception, e:  
except Exception:  
  pass # already unregistered  
device.set_configuration()  
endpoint = device[0][(0,0)][0]  
down = 1 # down  
up = 2 # up  
left = 4 # rotate left  
right = 8 # rotate right  
fire = 16 # fire  
stop = 32 # stop  
#device.ctrl_transfer(0x21, 0x09, 0x0200, 0, [signal])
#END MISSILE CODE

#TITLE OF THE PROGRAM AND THE ONTENTS OF THE COMMAND BUTTONS
title = "GopiGo Robot control with USB Missile"
choices = ["down", "up", "left", "right", "fire", "stop", "CarForward", "CarBackward", "CarLeft", "CarRight", "CarStop", "Take Picture", "Exit Program"]

#PROGRAM TO STOP THE USB CANNON
def cannon_stops():
    time.sleep(0.1)
    device.ctrl_transfer(0x21, 0x09, 0, 0, [0x02, stop, 0x00,0x00,0x00,0x00,0x00,0x00])
  
# message to be displayed AND LOAD THE IMAGE
msg= "Click on the following buttons"
inp = ''
inp1 = ''
image="gopigo2.jpeg"
while inp != "None": #happens when the user presses ESC
    inp = buttonbox("GopiGo Robot control with USB Missile", image=image, choices=choices)
    
    if inp == "down":
        call(['espeak "Down"'], shell=True)
        device.ctrl_transfer(0x21, 0x09, 0, 0, [0x02, down, 0x00,0x00,0x00,0x00,0x00,0x00])
        cannon_stops()
    elif inp == "up":
        call(['espeak "Up"'], shell=True)
        device.ctrl_transfer(0x21, 0x09, 0, 0, [0x02, up, 0x00,0x00,0x00,0x00,0x00,0x00])
        cannon_stops()
    elif inp == "left":
        call(['espeak "Left"'], shell=True)
        device.ctrl_transfer(0x21, 0x09, 0, 0, [0x02, left, 0x00,0x00,0x00,0x00,0x00,0x00])
        stops()
    elif inp == "right":
        call(['espeak "Right"'], shell=True)
        device.ctrl_transfer(0x21, 0x09, 0, 0, [0x02, right, 0x00,0x00,0x00,0x00,0x00,0x00])
        cannon_stops()
    elif inp == "fire":
        call(['espeak "Fire"'], shell=True)
        device.ctrl_transfer(0x21, 0x09, 0, 0, [0x02, fire, 0x00,0x00,0x00,0x00,0x00,0x00])  
        time.sleep(4)
        cannon_stops()
    elif inp == "stop":
        call(['espeak "Stop"'], shell=True)
        device.ctrl_transfer(0x21, 0x09, 0, 0, [0x02, stop, 0x00,0x00,0x00,0x00,0x00,0x00])

    elif inp =="CarForward": # If user entered 'Forward' move forward for 2 sec then stops
        fwd()
        sleep(2)
        stop()
    elif inp =="CarBackwards": # If user entered 'Backwards' moves back for 2 seconds while blinking both lights in .25 intervals then stops
        bwd()
        for x in range(4): # repeats 4 times
            led_on(LED_L)
            led_on(LED_R)
            sleep(.25)
            led_off(LED_L)
            led_off(LED_R)
            sleep(.25)
        stop()
    elif inp =="CarLeft": # If user entered 'Right' moves right for 2 seconds blinking the Right light in .25 intervals then stops
        left()
        for x in range(3): # repeats 4 times 
            led_on(LED_L)
            sleep(.25)
            led_off(LED_L)
            sleep(.25)          
        stop()
    elif inp =="CarRight": # If user entered 'Left' moves right for 2 seconds blinking the Left light in .25 intervals then stops
        right()
        for x in range(3): # repeats 4 times
            led_on(LED_R)
            sleep(.25)
            led_off(LED_R)
            sleep(.25)
        stop()
    elif inp =="CarStop":
        stop()
    elif inp =="Take Picture":
        call(['raspistill -o 123.jpg'], shell=True)
    elif inp =="Exit Program":
        quit()           
