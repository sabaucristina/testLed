import RPi.GPIO as GPIO
import time
from firebase import firebase
firebase = firebase.FirebaseApplication('https://console.firebase.google.com/project/first-46d3a/database/data/', None)
result = firebase.get('/led', '')
print (result)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
print "LED on"
if result:
    GPIO.output(18,GPIO.HIGH)
time.sleep(1)
print "LED off"
GPIO.output(18,GPIO.LOW)
