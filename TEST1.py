import RPi.GPIO as GPIO
from time import sleep

from pydub import AudioSegment
from pydub.playback import play

song = AudioSegment.from_wav("mauvaise.wav")
play(song)


GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

Motor1 = 22    # Input Pin
Motor2 = 18    # Input Pin
Motor3 = 16    # Enable Pin

Motor4 = 11    # Input Pin
Motor5 = 13    # Input Pin
Motor6 = 15    # Enable Pin

GPIO.setup(Motor1,GPIO.OUT)
GPIO.setup(Motor2,GPIO.OUT)
GPIO.setup(Motor3,GPIO.OUT)

GPIO.setup(Motor4,GPIO.OUT)
GPIO.setup(Motor5,GPIO.OUT)
GPIO.setup(Motor6,GPIO.OUT)

GPIO.output(Motor1,GPIO.HIGH)
GPIO.output(Motor2,GPIO.LOW)
GPIO.output(Motor3,GPIO.HIGH)

GPIO.output(Motor4,GPIO.LOW)
GPIO.output(Motor5,GPIO.HIGH)
GPIO.output(Motor6,GPIO.HIGH)

sleep(1)

GPIO.output(Motor1,GPIO.LOW)
GPIO.output(Motor2,GPIO.HIGH)
GPIO.output(Motor3,GPIO.HIGH)

GPIO.output(Motor4,GPIO.LOW)
GPIO.output(Motor5,GPIO.HIGH)
GPIO.output(Motor6,GPIO.HIGH)

sleep(1.5)

GPIO.cleanup()
