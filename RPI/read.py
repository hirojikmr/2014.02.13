#!/usr/bin/env python
cnt = 0
prev_time=""
for line in open('text.txt', 'r'):
	time = line[11:16]
	if prev_time != time:
		print line.rstrip()
		prev_time = time

