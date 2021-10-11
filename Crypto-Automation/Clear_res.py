import os
import sys

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