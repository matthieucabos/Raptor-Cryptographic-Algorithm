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

	This is the main Raptor Cryptographic Alternative algorithm v2.
	The difference between both versions is the type of the numbers list. The second version is using
	a representation of float crypted preserving the full precision of the values.
	This one is stable on his definition's domain and could be considered as the first one as 'fast crypting algorithm'.
	There are differents ways to use : 

		* Cybersecurity of business and organization (Hospitals, banks, etc)
		* Crypting data stream on the web
		* Crypting authentification informations

	This algorithm is ruled by the followings steps :

		* Define two differents sets :

			* The sep Set representing terms separators
			* The vir Set reprseneting the comma in float values

		* Getting raw string as input
		* Converting ASCII values to their decimal correspondence
		* Dividing each i+1_term of the list by the i_term of the list
		* Building key from the given formula : key(i)=((l(i)*l(i+1) modulo l(i+2)) modulo 26)
		* Multiplying each term by 10000
		* Building the mirror key from the original one
		* Compute each fraction division float value. Each fraction is defined by res(i)/key(i+1). Each part of the value is represented into a single integer value
		* Multiplying each float res by 10 to get larger values (useful to Base Table converter)
		* Convert into key-indexed Base Table values
		* Defining commas and separators from the vir and sep Sets
		* Return the full crypted string

	_________________________________________________________________

	**Source Code**
	---------------
		
	# Algorithme de cryptage

	# txt=input("Entrez un texte")
	txt="salut bande de nazes"
	# txt="une autre chaine pour"
	# txt="salut bande de nazes, on va tester une chaine de grande longueur pour verifier si l'algorithme fonctionne toujours"
	l=[]
	res=[]
	for i in range(len(txt)):
		l.append(ord(txt[i]))

	print("l = ")
	print(l)
	print("#################################")

	first=int(l[0])
	for i in range(0,len(l)-1):
		res.append(float(l[i+1]/l[i]))
	key=[]
	for i in range(0,len(l)-2):               # Finir la chaine de texte par trois caractères "usuels", par exemple "..."
		key.append(int((l[i]*l[i+1])%l[i+2])) # Eventuellement ameliorer la clé en la complementant a 36 sur [10,36] 
		key[i]=(key[i])%26

	print("res =")
	print(res)
	print("#################################")

	for i in range(len(res)):
		res[i]=int(res[i]*10000)
	res.append(first)
	key.append(key[0])	#key padding
	key.append(key[1])
	print(len(res))
	print(len(key))
	print("key = ")
	print(key)
	print("################################")
	print("res =")
	print(res)
	print("################################")

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

	print("Float_res = ")
	print(Float_res)
	print("################################")
	print(len(Float_res))
	print(len(Mirror_key))
	#Multiplying each float res by 10 to get larger values (useful to Base Table converter)
	for i in range(len(Float_res)):
		Float_res[i]*=10

	#Convert into key-indexed Base Table values
	crypt=[]
	for i in range(len(Float_res)):
		crypt.append(table[Mirror_key[i]][Float_res[i]])
	print(crypt)
	print("################################")
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

	# Return the full crypted string 
	print("string = ")
	print(string)
	print("################################")

	Description of De-Crypter
	=========================

	**Main Raptor Cryptographic Alternative Algorithm**

	_________________________________________________________________

	**Algorithm**
	-------------

	To decrypt the obtained string sequence from the Crypter, you have to follow these steps :

		* Rebuild the terms list from the given string using sep and vir Sets
		* Convert crypted value to their integer index
		* Devide each of value by 10 to get the smaller origianl values
		* Rebuild float values from the integer couples values
		* Round multiplication of float value and Mirror key value to rebuild terms
		* Divide each computed values from multiplication of i_term fo the float list with the last computed term by 10000 to get origianls terms
		* Round and convert to ASCII values to get the original string

	_________________________________________________________________

	**Source Code**
	---------------

	rez=[]
	tmp=''
	ind=0
	first=Mirror_key[-1]
	Mirror_key=Mirror_key[:-1]

	# Rebuild the terms list from the given string using sep and vir Sets
	for item in string:
		if not item in sep and not item in vir:
			tmp+=item
			# print(tmp)
		else:
			# Convert crypted value to their integer index
			rez.append(table[Mirror_key[ind]].index(tmp))
			tmp=''
			ind+=1
	firstt=rez[-1]
	rez=rez[:-1]

	print("rez =")
	print(rez)
	print("################################")

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
			
	print("Float_rez = ")
	print(Float_rez)
	print("################################")

	# Algorithme de décryptage

	# Round multiplication of float value and Mirror key value to rebuild terms
	rez=[]
	for i in range(len(Float_rez)):
		rez.append(round(Float_rez[i]*(Mirror_key[i]+1)))

	print("rez =")
	print(rez)
	print("################################")

	rezz=[]
	rezz.append((first*rez[0])/10000)

	print("rez =")
	print(rez)
	print("################################")

	# Divide each computed values from multiplication of i_term fo the float list with the last computed term by 10000 to get origianls terms
	for i in range(1,len(rez)):
		rezz.append((rez[i]*rezz[i-1])/10000)

	print(rezz)

	final=[]
	# Round and convert to ASCII values to get the original string
	for i in range(len(rezz)):
		final.append(chr(round(rezz[i])))
	txt=[]
	txt.append(chr(first))
	for i in range(len(final)):
		txt+=final[i]
		
	print(txt)

"""

sep=['!','"','#','$','%','&','(',')','*','+',',','-','.','/']
vir=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

# Construction de la table des bases

table=table()

def mirror(liste):
	"""
		The mirror function build a mirror list from the given one.

		=============== =========== ========================
		**Parameters**    **Type**    **Description**
		**liste**          list        The list to be treat
		=============== =========== ========================

		:Returns: list : The mirror list from the given parameter.
	"""
	res=liste[:]
	for i in range(1,len(liste)):
		res.append(liste[-i])
	res.append(liste[0])
	return res

# Algorithme de cryptage

# txt=input("Entrez un texte")
txt="salut bande de nazes"
# txt="une autre chaine pour"
# txt="salut bande de nazes, on va tester une chaine de grande longueur pour verifier si l'algorithme fonctionne toujours"
l=[]
res=[]
for i in range(len(txt)):
	l.append(ord(txt[i]))

# print("l = ")
# print(l)
# print("#################################")

first=int(l[0])
for i in range(0,len(l)-1):
	res.append(float(l[i+1]/l[i]))
key=[]
for i in range(0,len(l)-2):               # Finir la chaine de texte par trois caractères "usuels", par exemple "..."
	key.append(int((l[i]*l[i+1])%l[i+2])) # Eventuellement ameliorer la clé en la complementant a 36 sur [10,36] 
	key[i]=(key[i])%26

# print("res =")
# print(res)
# print("#################################")

for i in range(len(res)):
	res[i]=int(res[i]*10000)
res.append(first)
key.append(key[0])	#key padding
key.append(key[1])
# print(len(res))
# print(len(key))
# print("key = ")
# print(key)
# print("################################")
# print("res =")
# print(res)
# print("################################")

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

# print("Float_res = ")
# print(Float_res)
# print("################################")
# print(len(Float_res))
# print(len(Mirror_key))
#Multiplying each float res by 10 to get larger values (useful to Base Table converter)
for i in range(len(Float_res)):
	Float_res[i]*=10

#Convert into key-indexed Base Table values
crypt=[]
for i in range(len(Float_res)):
	crypt.append(table[Mirror_key[i]][Float_res[i]])
# print(crypt)
# print("################################")
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
#######################################################################################################

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
		# print(tmp)
	else:
		# Convert crypted value to their integer index
		rez.append(table[Mirror_key[ind]].index(tmp))
		tmp=''
		ind+=1
firstt=rez[-1]
rez=rez[:-1]

print("rez =")
print(rez)
print("################################")

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
		
print("Float_rez = ")
print(Float_rez)
print("################################")

# Algorithme de décryptage

# Round multiplication of float value and Mirror key value to rebuild terms
rez=[]
for i in range(len(Float_rez)):
	rez.append(round(Float_rez[i]*(Mirror_key[i]+1)))

print("rez =")
print(rez)
print("################################")

rezz=[]
rezz.append((first*rez[0])/10000)

print("rez =")
print(rez)
print("################################")

# Divide each computed values from multiplication of i_term fo the float list with the last computed term by 10000 to get origianls terms
for i in range(1,len(rez)):
	rezz.append((rez[i]*rezz[i-1])/10000)

print(rezz)

final=[]
# Round and convert to ASCII values to get the original string
for i in range(len(rezz)):
	final.append(chr(round(rezz[i])))
txt=[]
txt.append(chr(first))
for i in range(len(final)):
	txt+=final[i]
	
print(txt)
