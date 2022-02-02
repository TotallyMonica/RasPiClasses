import RPi.GPIO as GPIO                 # This will result in a runtime error if not being ran on a pi and doesn't have the GPIO package installed. Usually installed on pis by default
import time

ledPin = 11                             # GPIO 17

delay = 1                               # 1 second
loopCnt = 100                           # Loop 100 times

def main():
    for i in range(loopCnt):
        GPIO.output(ledPin, GPIO.HIGH)  # output 3.3V from GPIO pin
        time.sleep(delay)               # wait 1s
        GPIO.output(ledPin, GPIO.LOW)   # ouput 0V from GPIO pin
        time.sleep(delay)               # wait 1s

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledPin, GPIO.OUT)        # initialize GPIO pin as OUTPUT pin
    GPIO.output(ledPin, GPIO.LOW)

if __name__ == "__main__":
    setup()
    main()
    GPIO.cleanup()                      # Free up used resources, can probably omit safely