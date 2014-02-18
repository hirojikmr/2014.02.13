#!/usr/bin/env python
import os

IN_FILE='text.txt'
OUT_FILE="temp.txt"

f = open(OUT_FILE, 'w')
cnt = 0
prev_time=""
for line in open(IN_FILE, 'r'):
	time = line[11:16]
	if prev_time != time:
		f.write(line)
		prev_time = time

f.close() 
os.system("python cp_file.py %s" % OUT_FILE)
os.system("rm %s" % OUT_FILE);
