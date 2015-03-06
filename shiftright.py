#!/usr/bin/python

# This script taks a word list and makes a new word list that has its letters shifted to the right on a US keyboard. i.e. 'a' becomes 's', 'r' becomes 't'
# 'l' becomes ';', etc. Written by ryman1

mapping=file("D:\pwcracking\mapping.txt","r")
secondpass = False
letterin = ''
letterout = ''
legend = {}

#Create a python dictionary of the mappings
for x in mapping.read(-1):
	if x != '\n':
			
		if secondpass == False:
			letterin = x
			secondpass = True
		else:
			letterout = x
			secondpass = False
			legend[letterin]=letterout
		
sourcefile = file("D:/pwcracking/dic/word.lst","r",1)
destfile = file("D:/pwcracking/dic/word-shifted.lst","w")

for x in sourcefile.read(-1):
	
	if x == "\n":
		destfile.write("\n")
	elif legend.__contains__(x):
		destfile.write(legend[x])
	else:
		destfile.write(x)
		
sourcefile.close()
destfile.close()
