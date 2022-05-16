import time
import random
import digitalio
from digitalio import DigitalInOut, Direction, Pull
import board


hall_sensor = digitalio.DigitalInOut(board.D13)
hall_sensor.direction = digitalio.Direction.INPUT
hall_sensor.pull = Pull.UP

led1 = DigitalInOut(board.D12)
led2 = DigitalInOut(board.D11)
led3 = DigitalInOut(board.D10)
led4 = DigitalInOut(board.D9)
led5 = DigitalInOut(board.D6)
led6 =DigitalInOut(board.D5)
led7 = DigitalInOut(board.A3)
led8 = DigitalInOut(board.A4)
led9 =DigitalInOut(board.A5)

led1.direction = Direction.OUTPUT
led2.direction = Direction.OUTPUT
led3.direction = Direction.OUTPUT
led4.direction = Direction.OUTPUT
led5.direction = Direction.OUTPUT
led6.direction = Direction.OUTPUT
led7.direction = Direction.OUTPUT
led8.direction = Direction.OUTPUT
led9.direction = Direction.OUTPUT


lights =[
    led1,
    led2,
    led3,
    led4,
    led5,
    led6,
    led7,
    led8,
    led9,

    ]

def blink(x):

        for i in range(8):
            lights[i].value = True
            time.sleep(1)
            lights[i].value = False
            time.sleep(0.01)



while True:
    if hall_sensor.value is False:
        blink(3)

