import os
dir = "/home/techgeek/Projects/www-sugarlabs/python_scripts/sugarlabs_Activites/"
files = os.listdir(dir)
f = open("/home/techgeek/Projects/www-sugarlabs/python_scripts/filenames")
name = "download"
i = 1

for line in f:
	while(1):
		if name in files:
			name = dir+ name
			print name
			if line[-1]=='\n':
				line = line[:-1]+".svg"
			print line
			os.rename(name, line)
			break
		else:
			name = "download (" + str(i) +")"
			i=i+1 	
		