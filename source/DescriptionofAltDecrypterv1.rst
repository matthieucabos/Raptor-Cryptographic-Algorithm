Description of De-Crypter
=========================

**Main Raptor Cryptographic Alternative Algorithm**

_________________________________________________________________

**Algorithm**
-------------

To decrypt the obtained string sequence from the Crypter, you have to follow these steps :

	* **Rebuild** original term list from the string using the sep Set
	* **Transpose** each term in his corresponding Base from the key to get integers values.
	* **Dividing** each of term by 10000 to restitute float values
	* **The zero step of decrypting** is the multiplication of the first term of the list with the first value of the begining Ascii converted list (appending it to the key to make it confidential)
	* **Restitute** each i_term multiplying with i-1_term
	* **Rounding and restitute** via conversion the origial ASCII chain.

_________________________________________________________________

**Source Code**
---------------

.. code-block:: python	

	from base_opt import *
	import random as r
	sep=['!','"','#','$','%','&','(',')','*','+',',','-','.','/']
	vir=[]

	# Construction de la table des bases

	table=table()


	string=input('chaine cryptée : ')
	str_key=input('clé : ')

	key=[]
	tmp=''
	ind=0
	for item in str_key:
		if not item in sep:
			tmp+=item
		else:
			key.append(int(tmp))
			tmp=''
			ind+=1


	rez=[]
	tmp=''
	ind=0
	first = key[-1]
	key= key[:-1]
	for item in string:
		if not item in sep:
			tmp+=item
			# print(tmp)
		else:
			rez.append(table[key[ind]].index(tmp))
			tmp=''
			ind+=1
	firstt=rez[-1]
	rez=rez[:-1]

	# Algorithme de décryptage

	for i in range(0,len(rez)):
		rez[i]=rez[i]/10000

	rezz=[]
	rezz.append(first*rez[0])

	for i in range(1,len(rez)):
		rezz.append(rez[i]*rezz[i-1])

	final=[]

	for i in range(len(rezz)):
		final.append(chr(round(rezz[i])))
	txt=''
	txt=(chr(first))
	for i in range(len(final)):
		txt+=str(final[i])
		
	print(txt)