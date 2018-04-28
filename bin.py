#!/usr/bin/python3
'''
This script serves to send binary messages through just 2 cables
'''

from time import sleep
from hashlib import sha1
import RPi.GPIO as GPIO

pin = 12 #GPIO 12
flag = 16 #GPIO 16

GPIO.cleanup()
GPIO.setwarnings(False) # Ignore Warnings
GPIO.setmode(GPIO.BCM)  # set board mode to Broadcom
GPIO.setup(pin, GPIO.OUT)
GPIO.setup(flag, GPIO.OUT)

def formatBin(number, size=4):
        toAdd = "0" * (size - len(number))
        number = toAdd + number
        return number

def getBin(val):
        return formatBin(bin(int(val))[2:])

def sendBin(bitVal, pin = 12):
        #Sends a hex value through one pin using binary number
        GPIO.output(pin, bitVal)
        GPIO.output(flag, GPIO.HIGH)
        sleep(0.005)
        GPIO.output(flag, GPIO.LOW)
        sleep(0.016)

def main():
    GPIO.output(pin, GPIO.LOW)
    GPIO.output(flag, GPIO.LOW)
    hex = {'0': '0','1': '1','2': '2','3': '3',
           '4': '4','5': '5','6': '6','7': '7',
           '8': '8','9': '9','a': '10','b': '11',
           'c': '12','d': '13','e': '14','f': '15',}
    while(True):
        for hexVal in input("Hex value: "):
            decimal = hex[hexVal]
            binVal = getBin(decimal)
            for bit in binVal:
                GPIO.output(pin, int(bit))
                GPIO.output(flag, 1)
                sleep(0.005)
                GPIO.output(flag, 0)
                GPIO.output(pin, 0)
                sleep(0.016)
main()
