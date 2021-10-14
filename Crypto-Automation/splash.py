import sys
import os

file_name=sys.argv[1]
mode = sys.argv[2]
file_name_out = sys.argv[3]

if file_name=='--help': 
	print("Usage : python3 splash <file_name_in> <mode> <file_name_out>")

if mode == 1 :
	f=open(file_name,'r')
	c=f.read()
	print(c.replace('\n','.'))
	f2=open(file_name_out,'w')
	f2.write(c.replace('\n','.'),)
else:
	f=open(file_name,'r')
	c=f.read()
	print(c.replace('.','\n'))
	f2=open(file_name_out,'w')
	f2.write(c.replace('.','\n'))