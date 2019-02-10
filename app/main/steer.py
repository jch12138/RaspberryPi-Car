import RPi.GPIO as GPIO
import time

PWM_FREQ = 50


class Steer():
    def __init__(self, pin1, pin2):
        # GPIO.cleanup()
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        GPIO.setup(pin1, GPIO.OUT)
        GPIO.setup(pin2, GPIO.OUT)
        self.pwm1 = GPIO.PWM(pin1, PWM_FREQ)
        self.pwm2 = GPIO.PWM(pin2, PWM_FREQ)
        self.pwm1.start(0)
        self.pwm2.start(0)
        self.angle1 = 6.5 # 2.5~12
        self.angle2 = 2 # 2~6

    def increase_angle1(self):
        self.angle1 -= 1
        if self.angle1 < 2.5:
            self.angle1 = 2.5
        self.pwm1.ChangeDutyCycle(self.angle1)
        time.sleep(0.05)
        self.pwm1.ChangeDutyCycle(0)
    
    def increase_angle2(self):
        self.angle2 -= 1
        if self.angle2 < 2:
            self.angle2 = 2
        self.pwm2.ChangeDutyCycle(self.angle2)
        time.sleep(0.05)
        self.pwm2.ChangeDutyCycle(0)

    def reduce_angle1(self):
        self.angle1 += 1
        if self.angle1 > 12:
            self.angle1 = 12
        self.pwm1.ChangeDutyCycle(self.angle1)
        time.sleep(0.05)
        self.pwm1.ChangeDutyCycle(0)

    
    def reduce_angle2(self):
        self.angle2 += 1
        if self.angle2 > 6:
            self.angle2 = 6
        self.pwm2.ChangeDutyCycle(self.angle2)
        time.sleep(0.05)
        self.pwm2.ChangeDutyCycle(0)
