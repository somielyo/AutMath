import RPi.GPIO as GPIO
from time import sleep
from pydub import AudioSegment
from pydub.playback import play

song = AudioSegment.from_wav("bravo.wav")
play(song)




GPIO.setmode(GPIO.BOARD)   ##je prefere la numerotation BOARD plutot que BCM

Moteur1A = 22      ## premiere sortie du premier moteur, broche 16
Moteur1B = 18      ## deuxieme sortie de premier moteur, broche 18
Moteur1E = 16      ## enable du premier moteur, broche 22

Moteur2A = 11      ## premiere sortie du deuxieme moteur, broche 19
Moteur2B = 13      ## deuxieme sortie de deuxieme moteur, broche 21
Moteur2E = 15      ## enable du deuxieme moteur, broche 22

GPIO.setup(Moteur1A,GPIO.OUT)  ## ces 6 broches du Raspberry Pi sont des sorties
GPIO.setup(Moteur1B,GPIO.OUT)
GPIO.setup(Moteur1E,GPIO.OUT)

GPIO.setup(Moteur2A,GPIO.OUT) 
GPIO.setup(Moteur2B,GPIO.OUT)
GPIO.setup(Moteur2E,GPIO.OUT)

pwm1 = GPIO.PWM(Moteur1E,100)   ## pwm de la broche 22 a une frequence de 50 Hz
pwm1.start(80)   ## on commemnce avec un rapport cyclique de 100%

pwm2 = GPIO.PWM(Moteur2E,50)   ## pwm de la broche 23 a une frequence de 50 Hz
pwm2.start(40)   ## on commemnce avec un rapport cyclique de 100%

print ("Moteur 1 sens direct, rapide.  Moteur 2 sens direct, lent.")
  ## on laisse tourner les moteur 5 secondes avec des parametres

print ("Moteur 1 sens direct, lent.  Moteur 2 sens inverse, lent.")

#pwm1.ChangeDutyCycle(20)  ## modification du rapport cyclique a 20%

GPIO.output(Moteur2A,GPIO.LOW)
GPIO.output(Moteur2B,GPIO.HIGH)
GPIO.output(Moteur2E,GPIO.HIGH)

GPIO.output(Moteur1A,GPIO.HIGH)
GPIO.output(Moteur1B,GPIO.LOW)
GPIO.output(Moteur1E,GPIO.HIGH)

sleep(5)

print ("Moteur 1 sens inverse, lent.  Moteur 2 sens inverse, rapide.")


print ("Arret des moteurs")
GPIO.output(Moteur1E,GPIO.LOW)
GPIO.output(Moteur2E,GPIO.LOW)
pwm1.stop()    ## interruption du pwm
pwm2.stop()
GPIO.cleanup()