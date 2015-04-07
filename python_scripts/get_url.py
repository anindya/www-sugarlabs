import urllib
import os
import sys

url = "/home/techgeek/Projects/www-sugarlabs/python_scripts/Sugar Activities.html"
page=urllib.urlopen(url)
a_url = []
a_name = []
result = page.read()
i = 0 
#files_in_dir = os.listdir("/home/techgeek/Projects/temp/sugarlabs_Activites/")
f= open('/home/techgeek/Projects/www-sugarlabs/_includes/about_activities3.html', 'w')
for i in range (0,69):
	startIndex = result.index("href")
	#print result[startIndex+6:startIndex+10]
	endIndex = result.index('>')
	a_url.append(result[startIndex+6:endIndex-1])
	#print a_url
	startIndex_name = result.index('<span class="title">')
	endIndex_name = result.index('</span>')
	a_name.append(result[startIndex_name+20:endIndex_name])
	url = result[startIndex+6:endIndex-1]
	name = result[startIndex_name+20:endIndex_name]
	print name+"\n"
	syntax  = "<div class=\"item\">\n\t<a href=\""+url+"\">"+"\n\t\t <ul>\n\t\t\t<li><img src=\"assets/activities_images/"+name+".svg\" ></li>\n\t\t\t<li><span class=\"title\">"+name+"</span></li>\n\t\t</ul>\n\t</a>\n</div>\n"
	#print syntax
	result = result[endIndex_name+11:]
	i=i+1
	f.write(syntax)
print i