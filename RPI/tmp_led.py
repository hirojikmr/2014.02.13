import RPi.GPIO as GPIO

# Use the pin numbers from the ribbon cable board.
GPIO.setmode(GPIO.BCM)

# Set up the pin you are using ("18" is an example) as output.
GPIO.setup(18, GPIO.OUT)


flg = 1

for i in range(50000):
	# Open the file that we viewed earlier so that python can see what is in it. Replace the serial number as before. 
	tfile = open("/sys/bus/w1/devices/28-000003dab11b/w1_slave") 
	# Read all of the text in the file. 
	text = tfile.read() 

	# Close the file now that the text has been read. 
	tfile.close() 

	# Split the text with new lines (\n) and select the second line. 
	secondline = text.split("\n")[1] 

	# Split the line into words, referring to the spaces, and select the 10th word (counting from 0). 
	temperaturedata = secondline.split(" ")[9] 

	# The first two characters are "t=", so get rid of those and convert the temperature from a string to a number. 
	temperature = float(temperaturedata[2:]) 

	# Put the decimal point in the right place and display it. 
	temperature = temperature / 1000 
	print temperature

	
	if temperature > 20.0 or flg == -1 :
		import RPi.GPIO as GPIO

		# Turn on the pin and see the LED light up.
		GPIO.output(18, GPIO.HIGH)
	else:
		#Turn off the pin to turn off the LED.
		GPIO.output(18, GPIO.LOW)

	flg = flg * -1;
