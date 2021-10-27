import os
import pexpect as pe
import re
import sys

# Automate fro Crypting Management. Respect the md5sum as reference

def Manage_crypted(crypted):
	# Manage the raw stdout from the Raptor Algorithm and sort it
	regCr=r"^[!\"#$%&()*+,./:;<=>?@][0-9a-z].*"
	regKe=r"^[0-9].*"
	Crypted=[]
	Key=[]
	matches = re.finditer(regCr, crypted, re.MULTILINE)
	for matchNum, match in enumerate(matches, start=1):
		Crypted.append(match.group()[:-1])
	matches = re.finditer(regKe, crypted, re.MULTILINE)
	for matchNum, match in enumerate(matches, start=1):
		Key.append(match.group()[:-1])
	Cr_dict={}
	print(Crypted)
	print(Key)
	for i in range(len(Crypted)):
		Cr_dict[Crypted[i]]=Key[i]
	f=open('Crypted.txt','a')
	for k,v in Cr_dict.items():
		f.write(k)
		f.write('_')
		f.write(v)
		f.write('_')
	f.close()

# Getting Parameters

mode=int(sys.argv[1])
algo=int(sys.argv[2])
if (algo !=3):
	slice_size=int(sys.argv[3])
else:
	slice_size=int(sys.argv[3])
	if slice_size < 20:
		print('Please insert a slice size > 20')
		quit()
if mode :
	raw_data=sys.argv[4]
	raw_data=raw_data.replace(' ','_')


if mode:
	# Crypting Mode
	splitted=[]
	crypted=''
	count=0

	# Slice the raw data
	while raw_data != '' :
		splitted.append(raw_data[:slice_size])
		raw_data=raw_data[slice_size:]
		count+=1

	# Raptor v1 
	if algo == 1:
		child=pe.spawn('./basetestrecursivev2',encoding='utf-8')
		ind=0
		for item in splitted:
			ind+=1
			child.expect("Veuillez entrer une chaine <29 :",timeout=5)
			child.send(item)
			child.send('\r')
			child.expect("c\)ontinuer ou q\)uitter?")
			crypted+=child.before
			if (ind < count):
				child.send("c")
				child.send('\r')
			else:
				child.send("q\r")
				child.close()
		Manage_crypted(crypted)

	# Raptor v2
	elif algo == 2:
		child=pe.spawn('./basetestrecursivev3_longchaine',encoding='utf-8')
		ind=0
		for item in splitted:
			ind+=1
			child.expect("Veuillez entrer la chaine à crypter : ")
			child.send(item)
			child.send('\r')
			child.expect("c\)ontinuer ou q\)uitter")
			crypted+=child.before
			if(ind < count):
				child.send('c')
				child.send('\r')
			else:
				child.send('q\r')
				child.close()
		Manage_crypted(crypted)

	elif algo == 3:
		pass
	elif algo == 4:
		pass
	elif algo == 5:
		pass
else:
	# Uncrypting Mode
	raw_data=[]
	f=open('Crypted.txt','r')
	raw_data=f.read().split('_')[:-1]
	count=len(raw_data)
	Clean_txt=''

	# Raptor v1
	if algo == 1:
		child=pe.spawn('./basetestrecursivev2_solveur',encoding='utf-8')
		ind=0
		for item in raw_data:
			if ind % 2 == 0 :
				child.expect("Veuillez entrer la chaine cryptée : ")
				child.send(item)
				child.send('\r')
			else:
				child.expect("Veuillez saisir la clé : ")
				child.send(item)
				child.send('\r')
				child.expect("c\)ontinuer ou q\)uitter?")
				if (ind < count):
					child.send("c")
					child.send('\r')
					Clean_txt+=child.before.split('\n')[4][:-1]
				else:
					child.send("q\r")
					child.close()
			ind+=1
		print(Clean_txt.replace('_',' '))
		f=open('Uncrypted.txt','a')
		f.write(Clean_txt.replace('_',' '))

	# Raptor v2
	elif algo == 2:
		child=pe.spawn('./basetestrecursivev3_longchaine_solveur',encoding='utf-8')
		ind=0
		for item in raw_data:
			if ind % 2 == 0 :
				child.expect("Chaine cryptée : ")
				child.send(item)
				child.send('\r')
			else:
				child.expect("Clé unique : ")
				child.send(item)
				child.send('\r')
				child.expect("c\)ontinuer ou q\)uitter")
				if (ind < count):
					child.send("c")
					child.send('\r')
					Clean_txt+=child.before.split('\n')[3][:-1]
					# print(child.before.split('\n'))
				else:
					child.send("q\r")
					child.close()
			ind+=1
		print(Clean_txt.replace('_',' '))
		f=open('Uncrypted.txt','a')
		f.write(Clean_txt.replace('_',' '))

	elif algo == 3:
		pass
	elif algo == 4:
		pass
	elif algo == 5:
		pass