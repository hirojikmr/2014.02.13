import RPi.GPIO as GPIO 

# Use the pin numbers from the ribbon cable board. 
GPIO.setmode(GPIO.BCM) 

# Set up the pin you are using ("18" is an example) as output. 
GPIO.setup(18, GPIO.OUT) 

# Turn on the pin and see the LED light up. 
GPIO.output(18, GPIO.HIGH) 

for x in range(10000):

#Turn off the pin to turn off the LED. 
GPIO.output(18, GPIO.LOW)
