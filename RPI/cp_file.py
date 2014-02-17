import os
import datetime
import locale

src = "text.txt"
dst = "%s_%s" % (src,datetime.datetime.today().strftime("%Y.%m.%d.%H%M%S"))

os.system("cp %s %s" % (src,dst) )
