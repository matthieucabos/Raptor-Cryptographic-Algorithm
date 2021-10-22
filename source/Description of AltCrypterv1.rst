Description of Crypter
======================

**Main Raptor Cryptographic Alternative Algorithm**

_________________________________________________________________

**Algorithm**
-------------

This is the main Raptor Cryptographic Alternative algorithm.
During my researches, I have thought about an other version of the algorithm optimised for the long data stream as string.
The first algorithm use exponentional integer values list instead of this one wich allow to treat bigger slices using a divider.
Each term will be divide during the algorithm.
This algorithm is rules by following steps :

	* **Getting inputs**
	* **Converting ASCII** to Integers values to get a numeric list
	* **Dividing chain** : eachterm is divided by the next one  
	* **Multiplying** each i_term to the i+1_term modulo the i+2_term to get the key modulo 26. It means key(i)=((data(i)*data(i+1)) modulo data(i+2)) modulo 26
	* **Multiplying** each term of the crypt list with 10000 to get integers values from float.
	* **Key padding** to confirm key appending the two first elements of the key at the end and the top one numric list at the end
	* **Transposing** to the associated key index Base the full data list
	* **Adding separators** from the sep Set to split each term from another

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
	key.append(first)

	crypt=[]
	for i in range(len(res)):
		crypt.append(table[key[i]][res[i]])

	# rajouter des operations de listes reversibles 

	string=""
	for i in range(len(crypt)):
		string+=crypt[i]
		string+=sep[r.randint(0,13)]

	str_key=''
	for i in range(len(key)):
		str_key+=str(key[i])
		str_key+=sep[r.randint(0,13)]

	print(str_key)
	# print("################################")
	print('!'+string)
	# print("################################")
	quit()
