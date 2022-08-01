import grovepi
import time
import math
#Connect the ultrasonic sensor to D2 and the temp sensor to D4
tempsensor = 4 
# set I2C to use the hardware bus
grovepi.set_bus("RPI_1")

# Connect the Grove Ultrasonic Ranger to digital port D2
# SIG,NC,VCC,GND
ultrasonic_ranger = 2

blue = 0    # The Blue colored sensor.
white = 1   # The White colored sensor.
        
while True:
    try:
        # Read distance value from Ultrasonic
        print(grovepi.ultrasonicRead(ultrasonic_ranger))
        [temp,humidity] = grovepi.dht(tempsensor,blue)
        
        if math.isnan(temp) == False and math.isnan(humidity) == False:
            print("temp = %.02f C humidity =%.02f%%"%(temp, humidity))
    except Exception as e:
        print ("Error:{}".format(e))
    
    time.sleep(0.1) # don't overload the i2c bus
