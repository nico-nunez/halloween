import RPi.GPIO as GPIO
import time
import pygame
from flask import Flask, render_template, request, redirect
app = Flask(__name__)
regan = 40
chuckles = 36
frijoles = 32
device = None

pygame.mixer.init()
pygame.mixer.music.load('/home/pi/Desktop/halloween/static/scream.mp3')

def activate_device(device_name):
    GPIO.setup(device_name, GPIO.OUT)
    GPIO.output(device_name, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(device_name, GPIO.LOW)
    GPIO.cleanup()

@app.route("/")
def index():
    return render_template('index.html')
@app.route("/<deviceName>/")
def action(deviceName):
    GPIO.setmode(GPIO.BOARD)
    if deviceName == 'regan':
        pygame.mixer.music.play()
        time.sleep(1.5)
        GPIO.setup(regan, GPIO.OUT)
        GPIO.output(regan, GPIO.HIGH)
        time.sleep(2)
        GPIO.output(regan, GPIO.LOW)
        time.sleep(.25)
        GPIO.output(regan, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(regan, GPIO.LOW)
        time.sleep(.3)
        GPIO.output(regan, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(regan, GPIO.LOW)
        time.sleep(.5)
        GPIO.output(regan, GPIO.HIGH)
        time.sleep(1.5)
        GPIO.output(regan, GPIO.LOW)
        time.sleep(1)
        pygame.mixer.music.stop()
    if deviceName == 'chuckles':
        activate_device(chuckles)
    if deviceName == 'frijoles':
        activate_device(frijoles)
    GPIO.cleanup()
    return redirect('/', code=303)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
