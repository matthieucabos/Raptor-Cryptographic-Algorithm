from base_opt import *
import random as r
from mouchar import *
#Author : CABOS Matthieu
#Date : 02/2020


"""
	

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

		* Getting inputs
		* ASCII to INT
		* Dividing chain (eachterm is divided by the next one)  
		* Multiplying each i_term to the i+1_term modulo the i+2_term to get the key modulo 26. It means key(i)=((data(i)*data(i+1)) modulo data(i+2)) modulo 26
		* Multiplying each term of the crypt list with 10000 to get integers values from float.
		* I use key padding to confirm key appending the two first elements of the key at the end
		* Transposing to the associated key index Base the full data list
		* Adding separators from the sep Set to split each term from another

	_________________________________________________________________

	**Source Code**
	---------------

	.. code-block:: python	

		sep=['!','"','#','$','%','&','(',')','*','+',',','-','.','/']
		vir=[]

		# Construction de la table des bases

		table=table()

		# Algorithme de cryptage

		# txt=input("Entrez un texte")
		txt="salut bande de nazes"
		# txt="salut bande de nazes, on va tester une chaine de grande longueur pour verifier si l'algorithme fonctionne toujours"
		l=[]
		res=[]
		for i in range(len(txt)):
			l.append(ord(txt[i]))

		print(l)
		print("#################################")

		first=int(l[0])
		for i in range(0,len(l)-1):
			res.append(float(l[i+1]/l[i]))
		key=[]
		for i in range(0,len(l)-2):               # Finir la chaine de texte par trois caractères "usuels", par exemple "..."
			key.append(int((l[i]*l[i+1])%l[i+2])) # Eventuellement ameliorer la clé en la complementant a 36 sur [10,36] 
			key[i]=(key[i])%26

		print(res)
		print("#################################")

		for i in range(len(res)):
			res[i]=int(res[i]*10000)
		res.append(first)
		key.append(key[0])	#key padding
		key.append(key[1])

		print(len(res))
		print(len(key))
		print(key)
		print("################################")
		print(res)
		print("################################")

		crypt=[]
		for i in range(len(res)):
			crypt.append(table[key[i]][res[i]])

		# rajouter des operations de listes reversibles 

		string=""
		for i in range(len(crypt)):
			string+=crypt[i]
			string+=sep[r.randint(0,13)]

		print(string)
		print("################################")


	Description of De-Crypter
	=========================

	**Main Raptor Cryptographic Alternative Algorithm**

	_________________________________________________________________

	**Algorithm**
	-------------

	To decrypt the obtained string sequence from the Crypter, you have to follow these steps :

		* I rebuild original term list from the string using the sep Set
		* Transpose each term in his corresponding Base from the key to get integers values.
		* Dividing each of term by 10000 to restitute float values
		* The first step of decrypting is the multiplication of the first term of the list with the first value of the begining Ascii converted list (appending it to the key to make it confidential)
		* Restitute each i_term multiplying with i-1_term
		* Rounding and restitute via conversion the origial ASCII chain.

	_________________________________________________________________

	**Source Code**
	---------------

	.. code-block:: python	

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

		print(rez)
		print("################################")

		# Algorithme de décryptage

		for i in range(0,len(rez)):
			rez[i]=rez[i]/10000

		print(rez)
		print("################################")

		rezz=[]
		rezz.append(first*rez[0])

		print(rez)
		print("################################")

		for i in range(1,len(rez)):
			rezz.append(rez[i]*rezz[i-1])

		print(rezz)

		final=[]

		for i in range(len(rezz)):
			final.append(chr(round(rezz[i])))
		txt=[]
		txt.append(chr(first))
		for i in range(len(final)):
			txt+=final[i]
			
		print(txt)

"""

sep=['!','"','#','$','%','&','(',')','*','+',',','-','.','/']
vir=[]

# Construction de la table des bases

table=table()

# Algorithme de cryptage

# txt=input("Entrez un texte")
txt="salut bande de nazes"
# txt="salut bande de nazes, on va tester une chaine de grande longueur pour verifier si l'algorithme fonctionne toujours"
l=[]
res=[]
for i in range(len(txt)):
	l.append(ord(txt[i]))

print(l)
print("#################################")

first=int(l[0])
for i in range(0,len(l)-1):
	res.append(float(l[i+1]/l[i]))
key=[]
for i in range(0,len(l)-2):               # Finir la chaine de texte par trois caractères "usuels", par exemple "..."
	key.append(int((l[i]*l[i+1])%l[i+2])) # Eventuellement ameliorer la clé en la complementant a 36 sur [10,36] 
	key[i]=(key[i])%26

print(res)
print("#################################")

for i in range(len(res)):
	res[i]=int(res[i]*10000)
res.append(first)
key.append(key[0])	#key padding
key.append(key[1])
key.append(first)

print(len(res))
print(len(key))
print(key)
print("################################")
print(res)
print("################################")

crypt=[]
for i in range(len(res)):
	crypt.append(table[key[i]][res[i]])

# rajouter des operations de listes reversibles 

string=""
for i in range(len(crypt)):
	string+=crypt[i]
	string+=sep[r.randint(0,13)]

print(string)
print("################################")

#######################################################################################################

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

print(rez)
print("################################")

# Algorithme de décryptage

for i in range(0,len(rez)):
	rez[i]=rez[i]/10000

print(rez)
print("################################")

rezz=[]
rezz.append(first*rez[0])

print(rez)
print("################################")

for i in range(1,len(rez)):
	rezz.append(rez[i]*rezz[i-1])

print(rezz)

final=[]

for i in range(len(rezz)):
	final.append(chr(round(rezz[i])))
txt=[]
txt.append(chr(first))
for i in range(len(final)):
	txt+=final[i]
	
print(txt)
