import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

LED = 12
TRIG = 10
ECHO = 8
GPIO.setup(LED, GPIO.OUT)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

glow = GPIO.PWM(LED, 100)
glow.start(0)
max_distance = 30


def Distance():
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO) == False:
        start = time.time()

    while GPIO.input(ECHO) == True:
        end = time.time()

    time_distance = end - start

    distance = time_distance / 0.000058
    return distance


while True:
    sensor_distance = Distance()
    print(sensor_distance)
    if sensor_distance <= max_distance:
        glow.ChangeDutyCycle(100 - (sensor_distance/max_distance * 100))
        time.sleep(0.1)
    else:
        glow.ChangeDutyCycle(0)


led.stop()
GPIO.cleanup()
