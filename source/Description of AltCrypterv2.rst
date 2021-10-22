Description of Crypter
======================

**Main Raptor Cryptographic Alternative Algorithm**

_________________________________________________________________

**Algorithm**
-------------

This is the main Raptor Cryptographic Alternative algorithm v2.
The difference between both versions is the type of the numbers list. The second version is using
a representation of float crypted preserving the full precision of the values.
This one is stable on his definition's domain and could be considered as the first one as 'fast crypting algorithm'.
There are differents ways to use : 

	* **Cybersecurity of business and organization** (Hospitals, banks, etc)
	* **Crypting data stream** on the web
	* **Crypting authentification** informations

This algorithm is ruled by the followings steps :

	* **Define two differents sets** :

		* **The sep Set** representing terms separators
		* **The vir Set** reprseneting the comma in float values

	* **Getting raw string** as input
	* **Converting ASCII values** to their decimal correspondence
	* **Dividing each i+1_term of the list by the i_term** of the list
	* **Building key** from the given formula : key(i)=((l(i)*l(i+1) modulo l(i+2)) modulo 26)
	* **Multiplying each term by 10000**
	* **Building the mirror key** from the original one
	* **Compute each fraction** division float value. Each fraction is defined by res(i)/key(i+1). Each part of the value is represented into a single integer value
	* **Multiplying each float res by 10** to get larger values (useful to Base Table converter)
	* **Convert** into key-indexed Base Table values
	* **Defining commas and separators** from the vir and sep Sets
	* **Return the full crypted string**

_________________________________________________________________

**Source Code**
---------------
		
.. code-block:: python	

	from base_opt import *
	import random as r
	sep=['!','"','#','$','%','&','(',')','*','+',',','-','.','/']
	vir=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

	table=table()

	# Algorithme de cryptage

	txt=input("Entrez un texte")
	l=[]
	res=[]
	for i in range(len(txt)):
		l.append(ord(txt[i]))

	first=int(l[0])
	for i in range(0,len(l)-1):
		res.append(float(l[i+1]/l[i]))
	key=[]
	for i in range(0,len(l)-2):               # Finir la chaine de texte par trois caractères "usuels", par exemple "..."
		key.append(int((l[i]*l[i+1])%l[i+2])) # Eventuellement ameliorer la clé en la complementant a 36 sur [10,36] 
		key[i]=(key[i])%26

	for i in range(len(res)):
		res[i]=int(res[i]*10000)
	res.append(first)
	key.append(key[0])	#key padding
	key.append(key[1])

	tmp=0
	Float_res=[]
	Mirror_key=[]
	Mirror_key=mirror(key)
	Mirror_key.append(first)
	# Compute each fraction division float value. Each fraction is defined by res(i)/key(i+1)
	# Each part of the value is represented into a single integer value
	for i in range(len(res)):
		tmp = res[i]/(key[i]+1)
		Float_res.append(int(tmp))
		Float_res.append(int((tmp-int(tmp))*1000))
		tmp=0.0

	#Multiplying each float res by 10 to get larger values (useful to Base Table converter)
	for i in range(len(Float_res)):
		Float_res[i]*=10

	#Convert into key-indexed Base Table values
	crypt=[]
	for i in range(len(Float_res)):
		crypt.append(table[Mirror_key[i]][Float_res[i]])

	# rajouter des operations de listes reversibles 

	string=""
	ind=0
	# Defining commas and separators from the vir and sep Sets
	for i in range(len(crypt)):
		string+=crypt[i]
		if(ind%2==0):
			string+=vir[r.randint(0,25)]
		else:
			string+=sep[r.randint(0,13)]
		ind+=1

	ind=0
	str_key=''
	for i in range(len(Mirror_key)):
		str_key+=str(Mirror_key[i])
		str_key+=sep[r.randint(0,13)]

	print("key : ")
	print(str_key)	
	# Return the full crypted string 
	print("################################")

	print("string = ")
	print(string)
	print("################################")
	quit()