# Documentation
# Name : Yohjit Chopra
# Roll No. 2110994798

import RPi.GPIO as GPIO     #importing libraries
import time

GPIO.setmode(GPIO.BOARD)    # set mode for the pins i.e either boards or BCM 

LED = 12                    # initializing all the pins
TRIG = 10
ECHO = 8
GPIO.setup(LED, GPIO.OUT)   #setup of all the pins that have bneen initialized
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

glow = GPIO.PWM(LED, 100)   #setup of the PWM pin which is connected to the LED
glow.start(0)
max_distance = 30           # a constant for max distance (obejct will not be considered after this distance)


def Distance():                  # Making fucntion Distance which will measure the distance from the ultrasonice sensor using the formula.....
    GPIO.output(TRIG, True)       # Distance = (Time_taken x SpeedOfSound) / 2.
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO) == False:
        start = time.time()         # time library used to measure time taken

    while GPIO.input(ECHO) == True:
        end = time.time()

    time_distance = end - start

    distance = time_distance / 0.000058
    return distance


while True:
    sensor_distance = Distance()        # using fuction storing value of the object distance
    print(sensor_distance)              # printing the distance for testing purposes
    if sensor_distance <= max_distance:     # condition
        glow.ChangeDutyCycle(100 - (sensor_distance/max_distance * 100))        # the subration of ratio of distances multiplied by 100 from 100 will give a specific glow 
        time.sleep(0.1)                                                     # that represents the how far is the object.
    else:
        glow.ChangeDutyCycle(0)


glow.stop()              # stops the PWM pin
GPIO.cleanup()
