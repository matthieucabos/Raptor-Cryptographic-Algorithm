Description of De-Crypter
=========================

**Main Raptor Cryptographic Alternative Algorithm**

_________________________________________________________________

**Algorithm**
-------------

To decrypt the obtained string sequence from the Crypter, you have to follow these steps :

	* **Rebuild the terms list** from the given string using sep and vir Sets
	* **Convert crypted value** to their integer index
	* **Devide each of value by 10** to get the smaller origianl values
	* **Rebuild float values** from the integer couples values
	* **Round multiplication** of float value and Mirror key value to rebuild terms
	* **Divide each computed values** from multiplication of i_term fo the float list with the last computed term by 10000 to get origianls terms
	* **Round and convert to ASCII** values to get the original string

_________________________________________________________________

**Source Code**
---------------

.. code-block:: python	

	from base_opt import *
	import random as r

	sep=['!','"','#','$','%','&','(',')','*','+',',','-','.','/']
	vir=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

	table=table()


	string=input('Chaine Cryptée : ')
	str_key=input('Clé : ')

	Mirror_key=[]
	tmp=''
	ind=0
	for item in str_key:
		if not item in sep :
			tmp+=item
		else:
			Mirror_key.append(int(tmp))
			tmp=''
			ind+=1

	rez=[]
	tmp=''
	ind=0
	first=Mirror_key[-1]
	Mirror_key=Mirror_key[:-1]

	# Rebuild the terms list from the given string using sep and vir Sets
	for item in string:
		if not item in sep and not item in vir:
			tmp+=item
		else:
			# Convert crypted value to their integer index
			rez.append(table[Mirror_key[ind]].index(tmp))
			tmp=''
			ind+=1
	firstt=rez[-1]
	rez=rez[:-1]

	# Devide each of value by 10 to get the smaller origianl values
	for i in range(len(rez)):
		rez[i]/=10
	Float_rez=[]

	# Rebuild float values from the integer couples values
	for i in range(0,len(rez)):
		if(i%2==0):
			tmp=rez[i]
		else:
			Float_rez.append(tmp+rez[i]/1000)
			tmp=0.0

	# Algorithme de décryptage

	# Round multiplication of float value and Mirror key value to rebuild terms
	rez=[]
	for i in range(len(Float_rez)):
		rez.append(round(Float_rez[i]*(Mirror_key[i]+1)))

	rezz=[]
	rezz.append((first*rez[0])/10000)

	# Divide each computed values from multiplication of i_term fo the float list with the last computed term by 10000 to get origianls terms
	for i in range(1,len(rez)):
		rezz.append((rez[i]*rezz[i-1])/10000)

	final=[]
	# Round and convert to ASCII values to get the original string
	for i in range(len(rezz)):
		final.append(chr(round(rezz[i])))
	txt=""
	txt=(chr(first))
	for i in range(len(final)):
		txt+=final[i]
		
	print(txt)