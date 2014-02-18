#!/usr/bin/env python
import os
import time

IN_FILE='temp.txt_2014.02.18.183954'

cnt = 1
for line in open(IN_FILE, 'r'):
	d = line.split(',')
	#print ("wget 'http://python-app-momox.appspot.com/passdata?data1=%s&data2=%s'" % (d[0],d[1] ))
	os.system("wget 'http://python-app-momox.appspot.com/passdata?data1=%s&data2=%s'> /dev/null" % (d[0],d[1] ))	
	time.sleep(1.0)
	cnt += 1
	if cnt > 50:
		break


