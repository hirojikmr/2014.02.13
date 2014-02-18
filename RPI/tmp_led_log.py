import RPi.GPIO as GPIO
import datetime
import locale   
import os

OUT_FILE ='text.txt'

os.system("python read_data.py")

f = open( OUT_FILE, 'a')

# Use the pin numbers from the ribbon cable board.
GPIO.setmode(GPIO.BCM)

# Set up the pin you are using ("18" is an example) as output.
GPIO.setup(18, GPIO.OUT)


flg = 1

for i in range(100000):
	d_first = d_second = datetime.datetime.today()
	temp_sum=0
	data_cnt=0
	while (d_second - d_first).seconds < 60:
		# Open the file that we viewed earlier so that python can see what is in it. Replace the serial number as before. 
		tfile = open("/sys/bus/w1/devices/28-000003dab11b/w1_slave") 

		# Read all of the text in the file. 
		text = tfile.read() 
		data_cnt += 1

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
		temp_sum += temperature

		if temperature > 20.0 or flg == -1 :
			import RPi.GPIO as GPIO

			# Turn on the pin and see the LED light up.
			GPIO.output(18, GPIO.HIGH)
		else:
			#Turn off the pin to turn off the LED.
			GPIO.output(18, GPIO.LOW)
		flg = flg * -1;
		d_second = datetime.datetime.today()

	temperature = temp_sum/data_cnt
	#f.write("%s,%f\n" % (d.strftime("%Y-%m-%d %H:%M:%S"),temperature))
	print ("%s,%f\n" % (d_second.strftime("%Y-%m-%d %H:%M:%S"),temperature))
	os.system("wget 'http://python-app-momox.appspot.com/passdata?data1=%s&data2=%f'&> /dev/null" % (d_second.strftime("%Y-%m-%d %H:%M:%S"),temperature ))

f.close()
