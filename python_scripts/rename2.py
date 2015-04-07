import os
import re
dir = "/home/techgeek/Projects/www-sugarlabs/python_scripts/sugarlabs_Activites/"
files = os.listdir(dir)
for file_l in files:
	if file_l[-1]!="\W":
		os.rename(file_l, file_l[:-1])