import os
import sys

__author__="Matthieu CABOS"
__date__="11/10/2021"

f=open('res.txt','r')
Contents=f.readlines()
res=""
for item in Contents:
	res+=item
res=res.replace('\n',' ')
clear_text=""
for c in res :
	clear_text+=c
print(clear_text)
f.close()
