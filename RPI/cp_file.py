import os
import datetime
import locale
import sys

if len(sys.argv) == 1:
	src = "text.txt"
else:
	src = sys.argv[1]

dst = "%s_%s" % (src,datetime.datetime.today().strftime("%Y.%m.%d.%H%M%S"))

os.system("cp %s %s" % (src,dst) )
