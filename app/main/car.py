import RPi.GPIO as GPIO
import time


class Car():
    def __init__(self, channel1, channel2, channel3, channel4):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        GPIO.setup(channel1, GPIO.OUT)
        GPIO.setup(channel2, GPIO.OUT)
        GPIO.setup(channel3, GPIO.OUT)
        GPIO.setup(channel4, GPIO.OUT)
        self.channel_list = [channel1, channel2, channel3, channel4]

    def forward(self):
        GPIO.output(self.channel_list, (1, 0, 1, 0))

    def backward(self):
        GPIO.output(self.channel_list, (0, 1, 0, 1))

    def go_right(self):
        GPIO.output(self.channel_list, (1, 0, 0, 1))

    def go_left(self):
        GPIO.output(self.channel_list, (0, 1, 1, 0))

    def stop(self):
        GPIO.output(self.channel_list, (0, 0, 0, 0))
