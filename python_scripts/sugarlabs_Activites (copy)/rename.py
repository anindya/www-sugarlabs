import os
dir = "/home/techgeek/Projects/www-sugarlabs/python_scripts/sugarlabs_Activites/"
files = os.listdir(dir)
f = open("/home/techgeek/Projects/www-sugarlabs/python_scripts/filenames")
name = "download"
i = "1"
for file_list in files:
	for line in f:
		if name in files:
			name = dir+"name"
			os.rename(name, line)
		name = "download (" + i +")" 	
		break