import sys 
import math as m
import random as r
from mouchar import *
# codes from math:
# sqrt
# cos
# randint (moindre carré)

# high resolution cryptographic protocol
# author  : CABOS Matthieu
# release : 12/02/2018
# only for security tools as :
#   * autentification security
#   * cryptographic procedure
#   * software protection
# WARNING : i don't support any other use, use with extreme precaution

def ascii_to_int(chaine):
	"""
		Utils method : ascii to integer converter.

		=============== ========== =======================
		**Parameters**   **Type**   **Description**
		*chaine*         str        The string to convert
		=============== ========== =======================

		Returns
		=======
		list res : A list containing all integers values since ASCII. 

		Examples
		========
		>>> chaine="ceci est une chaine de caractère"
		>>> ascii_to_int(chaine)
		[99, 101, 99, 105, 32, 101, 115, 116, 32, 117, 110, 101, 32, 99, 104, 97, 105, 110, 101, 32, 100, 101, 32, 99, 97, 114, 97, 99, 116, 232, 114, 101]
	"""
	res = []
	for letter in chaine:
		res.append(ord(letter))
	return res

def int_to_ascii(crypt):
	"""
		Utils method : integer to ascii converter.

		================ ========== =================
		**Description**   **Type**   **Description**
		*crypt*           int list  The int list to convert
		================ ========== =================

		Returns
		=======
		str res : The converted ASCII string since int list.

		Examples
		========
		>>> print(l)
		[99, 101, 99, 105, 32, 101, 115, 116, 32, 117, 110, 101, 32, 99, 104, 97, 105, 110, 101, 32, 100, 101, 32, 99, 97, 114, 97, 99, 116, 232, 114, 101]
		>>> int_to_ascii(l)
		'ceci est une chaine de caractère'
	"""
	res = ''
	for i in range (0,len(crypt)):
		res+=chr(crypt[i])
	return res

def cryptChaine(to_crypt,table,base):
	"""
		The simple method to crypt an ascii string as integer list.

		=============== ============= ==================================================
		**Parameters**   **Type**      **Description**
		*to_crypt*       int list      The converted int list since an ascii string
		*table*          list of list  An array containing all fully builded Base Table
		*base*           int           Define the Base index 
		=============== ============= ==================================================

		Returns
		=======
		str list res : A string list containing all the base crypted values
		Must be used as a crypted list.
	"""
	res = []
	for i in range(0,len(to_crypt)):
		res.append(table[base][to_crypt[i]])
	return res

def local_table_dico(table2,base,rangeB):
	"""
		Utils method : A method to convert a Base table to Python dictionnary

		=============== ============== ======================================================
		**Parameters**   **Type**      **Description**
		*table2*         list of list  An array containing all the fully builded Base table
		*base*           int           Define the Base index
		*rangeB*         int           Define the max step of incrementation
		=============== ============== ======================================================

		Returns
		=======
		Dictionnary str_base : A dictionnary representing the specified Base table
	"""
	str_base={}
	res = {}
	if(rangeB>base**2):
		rangeB=base**2
	for i in range (0,rangeB):
		str_base[i]=table2[base][i]
	return str_base

def limit_range(Range,base):
	"""
		Utils method : A method to limit the Base range

		============== =========== ========================
		**Parameters**   **Type**   **Description**
		*Range*          int        The range as a limit
		*base*           int        The current Base index
		============== =========== ========================

		Returns
		=======
		int res : The limited by range res.
	"""
	res=0
	if(Range>base**2):
		res=base**2
	else:
		res=Range 
	return res

def base_key(int_chaine):
	"""
		This is the key builder.

		=============== =========== ===================================================
		**Parameters**   **Type**   **Description**
		*int_chaine*     int list   The base index list as a starting builder for key
		=============== =========== ===================================================

		Returns
		=======
		int list : the builded key from index base list.
	"""
	res=[]
	for i in range (0,len(int_chaine)):
		tmp=((int_chaine[i]*int_chaine[len(int_chaine)-i-1]+10)%36)
		if(tmp<10):
			tmp+=10
		res.append(tmp)
	return res 

def vec_poids(int_chaine):
	"""
		Compute the vectorial cumulated weight of the list.

		=============== ========== ===========================
		**Parameters**   **Type**   **Description**
		*int_chaine*     int list   The integer list to treat
		=============== ========== ===========================

		Returns
		=======
		int list res : The computed accumulated weigth integer list
	"""
	res = []
	res.append(int_chaine[0])
	for i in range(1,len(int_chaine)):
		res.append(res[i-1]+int_chaine[i])
	return res

def vec_1_poids(vec_poids):
	"""
		Compute the inverse of the vectorial cumulated weigth computation.

		=============== ========== ===============================
		**Parameters**   **Type**   **Description**
		*vec_poids*      int list   The weigth as an integer list
		=============== ========== ===============================

		Returns
		=======
		int list : The computed list containing the inverse operation of vec_poids method 
	"""
	res=[]
	for i in range (0,len(vec_poids)):
		res.append(1/vec_poids[i])
	return res

def equa_2_nd(a,b,c):
	"""
		Utils : An 2nd order equation solver

		============== ============= =================
		**Parameters**  **Type**     **Description**
		*a*             int / float  The a coefficient
		*b*             int / float  The b coefficient
		*c*             int / float  The c coefficient
		============== ============= =================

		Returns
		=======
		int / float res : The solved equation positive root
	"""
	res = 0
	racine1 = 0.0
	racine2 = 0.0
	delta = b**2-4*a*c 
	if(delta>0):
		racine1 = (-b+m.sqrt(delta))/2*a
		racine2 = (-b-m.sqrt(delta))/2*a
	if(racine1>0):
		res = int(racine1)
	else:
		res = int(racine2)
	return res

def multlist(a,b):
	"""
		Utils : A point by point list multiplier

		=============== ================ =====================
		**Parameters**   **Type**        **Description**
		*a*              int/float list  The list to multiply
		*b*              int/float list  The list to multiply
		=============== ================ =====================

		Returns
		=======
		int / float list : The computed point by point multiplication
	"""
	res = []
	if(len(a)!=len(b)):
		return []
	else:
		for i in range(0,len(a)):
			res.append(a[i]*b[i])
	return res

def transpose_base(liste,key,table):
	"""
		A method to transpose an integer list to the corresponding key's base index
		=> The result will be a succession of transposed values from differents integers to differents base
	
		=============== ========== ==========================================
		**Parameters**   **Type**   **Description**
		*liste*          list        the integer converted since ASCII list
		*key*            list        The Base index list as key
		*table*          list        The full Base Table recursively builded
		=============== ========== ==========================================

		Returns
		=======
		str list res : The crypted list as String list
	"""
	res = []
	if(len(liste)!=len(key)):
		return []
	else :
		for i in range (0,len(liste)):
			if(key[i]==10):
				res.append(liste[i])
			else:
				res.append(table[key[i]-2][liste[i]])
	return res

def inv_transpose_base(liste,key,table):
	"""
		The inverse method to decrypt a str list of base transposed values

		=============== ========== ===========================================
		**Parameters**   **Type**   **Description**
		*liste*           str list   The crypted list as String list
		*key*             int list   The Base index list as key
		*table*           int list   The full Base table recursively builded
		=============== ========== ===========================================

		Returns
		=======
		int list res : The decrypted list as integers
	"""
	res = []
	if(len(liste)!=len(key)):
		return []
	else:
		for i in range(0,len(liste)):
			if(key[i]==10):
				res.append(int(liste[i]))
			else:
				res.append(int(table[key[i]-2].index(liste[i])))
	return res

def crypt_procedure(chaine,table):
	"""
		The crypter manager to orchestrate the crypting procedure.
		It works from these steps:
			* We convert the given ascii string as integer list
			* We compute the Base index list as key from the converted integer list
			* We build the second part of the key since the mirror of the Base index list
			* We compute the cumulated weight of the integer list
			* We compute the point by point multiplication between cumulated weigth list and original integer list
			* We transpose the multiplied list into the given specified Base from the key
			* We associate the crypted strin to the key as return

		=============== ================ ======================================
		**Parameters**    **Type**        **Description**
		*chaine*           string          The string to crypt
		*table*            list of list    The Base Table recursively builded
		=============== ================ ======================================

		Returns
		=======
		list tuple (crypt_lst,key) : The couple crypted string and key as result. It permits to decrypt any message.
	"""
	int_chaine = ascii_to_int(chaine)
	base_keyy  = base_key(int_chaine)
	if(len(base_keyy)%2==0):
		key=base_keyy[0:int(len(base_keyy)/2)]
	else:
		key=base_keyy[0:int((len(base_keyy)/2)+1)]
	vec_poid   = vec_poids(int_chaine)
	crypt_lst  = multlist(int_chaine,vec_poid)
	crypt_lst  = transpose_base(crypt_lst,base_keyy,table)
	# print(crypt_lst)
	return(crypt_lst,key)

def cyclik_ascii(current):
	"""
		Compute a cyclik ascii separators into ponctuation signs

		============== =========== ===================================
		**Parameters**   **Type**   **Description**
		 *current*        str        The current poncuation separator 
		============== =========== ===================================

		 Returns
		 =======
		 str res : The following separator from the defined 'sep' Set.
	"""
	sep=['!','"','#','$','%','&','(',')','*','+',',','-','.','/']
	tmp=((sep.index(current)+1)%13)
	res =sep[tmp]
	return res

def cyclik_ascii_lvl2(current):
	"""
		Compute a cyclik ascii separators into ponctuation signs.
		Get a second cyclic ascii set modulo length

		============== =========== ===================================
		**Parameters**   **Type**   **Description**
		 *current*        str        The current poncuation separator 
		============== =========== ===================================

		 Returns
		 =======
		 str res : The following separator from the defined 'sep' Set.
	"""
	sep=[":",";","<","=",">","?","@"]
	tmp=((sep.index(current)+1)%6)
	res =sep[tmp]
	return res

def cyclik_ascii_lvl3(current):
	"""
		Compute a cyclik ascii separators into Upper letters from A to L.
		Get a third cyclic ascii set modulo length

		============== =========== ===================================
		**Parameters**   **Type**   **Description**
		 *current*        str        The current poncuation separator 
		============== =========== ===================================

		 Returns
		 =======
		 str res : The following separator from the defined 'sep' Set.
	"""
	sep=['A','B','C','D','E','F','G','H','I','J','K','L'] 		
	tmp=r.randint(0,11)
	res = sep[tmp]
	return res

def cyclik_ascii_mesquin(current,int_chaine):
	"""
		Compute a cyclik ascii separators into Upper letters from M to Z.
		Get a third cyclic ascii set modulo length

		============== =========== ===================================
		**Parameters**   **Type**   **Description**
		 *current*        str        The current poncuation separator 
		============== =========== ===================================

		 Returns
		 =======
		 str res : The following separator from the defined 'sep' Set.
	"""
	mesquin=['M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'] 
	tmp=r.randint(0,11)
	res=mesquin[tmp]
	return res

def reverse(liste):
	"""
		A function to reverse a string as argument.

		============== ========== ========================
		**Parameter**   **Type**   **Description**
		**s**           *String*   The string to reverse
		============== ========== ========================

		Returns
		=======
		str : The reversed string

		Examples
		========
		>>> s="the string to reverse"
		>>> reverse(s)
		'esrever ot gnirts eht'	

		
		.. code-block:: python	

			str= ""
			for i in s:
				str=i+str
			return str
		

	"""
	res=[]
	for i in range(0,len(liste)):
		res.append(liste[len(liste)-i-1])
	return res

def split_number(num):
	"""
		Integer splitter using the inverse Horner scheme and get it as a list of digits.

		=============== ========== =============================
		**Parameters**   **Type**   **Description**
		**num**           int        The integer to be splitted
		=============== ========== =============================

		Returns
		=======
		list : The splitted integer as list
	"""
	res=[]
	while(num>0):
		res.append(num % 10)
		num=int(num/10)
	return reverse(res)

def complement_at(x,base=2):
	"""
		Get the direct Base complemented value from the original x value.
		The Base must be inferior or equal to 10.

		=============== ============ ===============================
		**Parameters**    **Type**   **Description**
		**x**              int        The value to be complemented
		**base**           int        The current base
		=============== ============ ===============================

		Returns
		=======
		int : 
	"""
	return (base-1-x)

def get_value(x,table,base):
	"""
		A value getter to obtain an index from the original Base converted string value.
		This method is working as the list 'index' method and allow us to get the raw full integer corresponding to the list of list value.

		=============== ============ =======================
		**Parameters**  **Type**      **Description**
		**x**           str           The value to search
		**table**       list of list  The full Base Table 
		**base**        int           The index of the base
		=============== ============ =======================

		Returns
		=======
		int : The real decimal value of the specified term in his own Base.
	"""
	ind=0
	while(table[base][ind]!=x):
		ind+=1
	return ind

def complement_at_sup11(x,table,base=11):
	"""
		This function is used to compute the complement value from the original one in his own base.
		I use a temporary variable to store the numeric value of the compement and restitute it in his own base.

		=============== =============== ===================================================
		**Parameters**   **Type**       **Description**
		**x**             str           A string representation of my base converted value
		**table**         list of list  The full Base Table array
		**base**          int           The base index of the current value
		=============== =============== ===================================================

		Returns
		=======
		str : The complmented value in his own Base.
	"""
	nb_char=len(x)
	local_max=0
	for i in range(0,nb_char):
		local_max+=(base-1)*base**i
	num_value=local_max-get_value(x,table,base)
	return table[base][num_value]

def complement(x,table,base=2):
	"""
		The complement function is the full algorithm combining the complement_at_sup11 and complement_at functions.
		I specify the way to take between both of them using an if then else structure.

		=============== =============== =====================================================
		**Parameters**    **Type**       **Description**
		**x**              str            A string representation of my base converted value
		**table**          list of list   The full Base Table array
		**base**           int            The base index of the current value
		=============== =============== =====================================================

		Returns
		=======
		str : The complmented value in his own Base.
	"""
	final_res=0
	if(base<=10):
		splitted=split_number(int(x))
		for i in range(0,len(splitted)):
			splitted[i]=complement_at(splitted[i],base)
			final_res*=10
			final_res+=splitted[i]
		return final_res
	else:
		final_res=complement_at_sup11(x,table,base)
		return final_res

def crypt_final(tuple,int_chaine,table):
	"""
		The layout procedure to organise crypting results. The uodate consist to complement each of terms in his corresponding base.
		It allow a superior level of crypting. I use the separators set as well.

		=============== ========== ===================================================================
		**Parameters**   **Type**   **Description**
		*tuple*           tuple     list couple representing the crypted strin and the associated key
		=============== ========== ===================================================================

		Returns
		=======
		str res : The crypted list as a string with correct separators
	"""
	sept=['!','"','#','$','%','&','(',')','*','+',',','-','.','/']
	res = ''
	sep =sept[int(int_chaine[1]*m.cos(int_chaine[0]))%13] 
	crypt=tuple[0]
	key=tuple[1]
	tmp_len=len(key)
	if(len(key)%2==0):
		for i in range(1,tmp_len):
			key.append(key[tmp_len-i-1])
	else:
		for i in range(0,tmp_len):
			key.append(key[tmp_len-i-1])
	for i in range (0,len(crypt)):
		# injective crypt[i]
		res+=sep+str(complement(crypt[i],table,key[i])) 
		sep=cyclik_ascii(sep)
	return res

def crypt_final_long(liste,int_chaine,table):
	"""
		Chaining the final-level algorithm to get complex crypto-procedure

		=============== ========== ===================================================================
		**Parameters**   **Type**   **Description**
		*tuple*           tuple     list couple representing the crypted string and the associated key
		=============== ========== ===================================================================

		Returns
		=======
		str res : The full second level crypted string 
	"""
	sept=['!','"','#','$','%','&','(',')','*','+',',','-','.','/']
	res = ''
	sep =sept[int(int_chaine[1]*m.cos(int_chaine[0]))%13] 
	for i in range (0,len(liste)):
		res+=sep+str(liste[i])
		sep=cyclik_ascii(sep)
	# print(res)
	return res

def slurp(chaine):
	"""
		This method allow us to rebuild a str list of crypted terms using separators set.

		=============== ========== ==================================
		**Parameters**   **Type**   **Description**
		*chaine*         str         The raw string crypted message
		=============== ========== ==================================

		Returns
		=======
		str list res : The list of crypted terms rebuilded from the raw string
	"""
	tmp=''
	res = []
	sep=['!','"','#','$','%','&','(',')','*','+',',','-','.','/']
	for elem in chaine:
		if(not elem in sep):
			tmp+=str(elem)
			# print("tmp = "+tmp)
		else :
			res.append(tmp)
			# print("res = ")
			# print(res)
			tmp=''
		if(elem==''):
			break
	res=res[1:]
	res.append(tmp)
	return res

def slurp2(chaine):
	"""
		This method is similar of the slurp method. It defined a second level of crypting management.

		=============== ========== ==================================
		**Parameters**   **Type**   **Description**
		*chaine*         str         The raw string crypted message
		=============== ========== ==================================

		Returns
		=======
		str list res : The list of crypted terms rebuilded from the raw string.
	"""
	tmp=''
	res = []
	sep=[":",";","<","=",">","?","@"]
	for elem in chaine:
		if(not elem in sep):
			tmp+=str(elem)
		else:
			res.append(tmp)
			tmp=''
		if(elem==''):
			break
	res.append(tmp)
	return res

def slurp3(chaine):
	"""
		This method is similar of the slurp2 method. It defined a third level of crypting management.

		=============== ========== ==================================
		**Parameters**   **Type**   **Description**
		*chaine*         str         The raw string crypted message
		=============== ========== ==================================

		Returns
		=======
		str list res : The list of crypted terms rebuilded from the raw string.
	"""
	tmp=''
	mesquin=['M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	for elem in chaine:
		if(not elem in mesquin):
			tmp+=str(elem)		
	return tmp

def slurp4(chaine):
	"""
		This method is similar of the slurp2 method. It defined a third level of crypting management.

		=============== ========== ==================================
		**Parameters**   **Type**   **Description**
		*chaine*         str         The raw string crypted message
		=============== ========== ==================================

		Returns
		=======
		str list res : The list of crypted terms rebuilded from the raw string.
	"""
	tmp=''
	res = []
	sep=['A','B','C','D','E','F','G','H','I','J','K','L'] 	
	for elem in chaine:
		if(not elem in sep):
			tmp+=str(elem)
		else:
			res.append(tmp)
			tmp=''
		if(elem==''):
			break
	res.append(tmp)
	return res

def miam(key):
	"""
		Key builder from the half key as integer list. It rebuild the missing half with a mirror copy of the first one.

		=============== ========== ==========================
		**Parameters**   **Type**   **Description**
		**key**          int list   The half key as int list
		=============== ========== ==========================

		Returns
		=======
		int list res : The full key rebuilded from the half key
	"""
	tmp=''
	count=1
	res=[]
	for this in key:
		# print("this = "+str(this))
		# print("tmp = "+str(tmp))
		if(count%2==0):
			tmp+=str(this)
			count=1
			# print("tmp = "+str(tmp))
			res.append(tmp)
			tmp=''
		else:
			tmp=str(this)
			count+=1
	for i in range(0,len(res)):
		res[i]=int(res[i])
	return res

def resolve(liste):
	"""
		This method compute the chained 2nd order equations to solve the numeric suit.
		It permit us to get the ASCII values as a list.
		To solve the system you have to instance the solver with the square root of term 0.
		Once theorem zero done, you will apply the equation solver with square root of the 0-term as b,
		a as 1 and c as -following term.
		The algorithm sort the roots and take only positives ones.

		============== =========== ========================================
		**Parameters**   **Type**   **Description**
		*liste*          int list    The computed multiplied list to solve
		============== =========== ========================================

		Returns
		=======
		int list res : A list containing solved terms. 
	"""
	res = []
	x = 0
	tmp2 = 0
	res.append(int(m.sqrt(liste[0])))
	tmp=res[0]
	for i in range (1,len(liste)):
		# print("y = "+str(tmp))
		# print("x = "+str(x))
		tmp2 = equa_2_nd(1,-tmp,-liste[i])
		x=tmp2-tmp
		res.append(int(x))
		tmp=tmp2
	# print(res)
	return res

def decrypt_procedure(chaine,key,table):
	"""
		This method manage the decrypting procedure.
		It is ruled by the following steps :
			* Build the full key since the key argument
			* Split the string since separators via slurp method
			* Complement eah ch term in his own value
			* Apply the inv_tranpose_base method to get the uncrypted terms
			* Solve the cumulated multiplued weigth with the equation solver
			* Convert the int list as result to ASCII chain

		=============== =============== =================================
		**Parameters**   **Type**        **Description**
		*chaine*          str             The raw crypted text as string
		*key*             int list        The half key as int list
		*table*           list of list    The Base Table array
		=============== =============== =================================

		Returns
		=======
		str res : The uncrypted text.
	"""
	res = ''
	base=key[:]
	tmp = []
	key.reverse()
	tmp = key[:]
	to_find = []
	to_find=slurp(chaine)
	print(len(to_find))
	print(len(key))
	for i in range(0,len(to_find)):
		#injective inverse to_find[i]
		to_find[i]=complement(to_find[i],table,base[i])
	tmp_liste=inv_transpose_base(to_find,base,table)
	int_liste=resolve(tmp_liste)
	res = int_to_ascii(int_liste)
	return res

def split(chaine,seuil):
	"""
		Split the given string argument 'chaine' into slices from threshold size 'seuil'.
		Each of this slices are allowed into the cryptographic algorithm.

		============== ========== ============================================
		**Parameters**   **Type**   **Description**
		*chaine*          str        The full string to treat
		*seuil*           int        Define the threshold size of the slices
		============== ========== ============================================

		Returns
		=======
		str list res : The slices list as result
	"""
	res = []
	tmp = ''
	index = 0
	div=int(len(chaine)/seuil)
	for i in range(0,div):
		tmp=''
		# print("index = "+str(index)+" | seuil = "+str(seuil)+" | i = "+str(i))
		for j in range(index,(index+seuil)):
			tmp+=chaine[j]
			# print("j = "+str(j)+" | tmp = "+str(tmp))
			if(j==(index+seuil-1)):
				index=j+1
		res.append(tmp)
	if((index-1)<len(chaine)):
		tmp=chaine[index:]
		res.append(tmp)
	return res

def tilps(chaine):
	"""
		The reverse method of the split function. From a given str list, we rebuild the full length string

		=============== =========== =============================
		**Parameters**    **Type**   **Description**
		*chaine*          str list   The String slices as a list
		=============== =========== =============================

		Returns
		=======
		str res : The full striing rebuilded from the slices list
	"""
	res = ''
	for i in range (0,len(chaine)):
		res+=chaine[i]
	return res

def mesqui(txt,seuil):
	"""
		This method is used to create a wrong path of decrypting method.
		Using a similar Separators terms, I define a 'fake' terms list wich have absolutely no meanings for the rest of the algorithm.
		Using it as the last step of algorithm, it doesn't allow any brute force attack to decrypt.
		The threshold value 'seuil' will define the amount of distribution of fake separators.

		=============== ========== ==========================================================
		**Parameters**   **Type**   **Description**
		*txt*             str       The raw string to treat
		*seuil*           int       The threshold variable to assign the 'fake terms' length
		=============== ========== ==========================================================

		Returns
		=======
		str : The fully 'fake splitted' crypted string

	"""
	mesquin=['M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	res=''
	sep='M'
	for i in range(0,len(txt)):
		res+=txt[i]
		if(i%int((seuil))==0):
			res+=sep 
			sep=cyclik_ascii_mesquin(sep,int_chaine)
	return res


# firs step numeric base construction
def tablebase(base):
	res = []
	letter = 'a'
	letterbis = 'A'
	# //
	for i in range(0,base):
		if(i<10 or (i<=10 and base <=10)):
			res.append(str(i))
		if(i>=10 and base >10 and base<37):
			res.append(letter)
			letter=chr(ord(letter)+1)
	return res

# first level recursive build
def recursive_build(table_base):
	res = []
	# //*2
	for i in table_base:
		for j in table_base:
			res.append(i+j)
	return res

# first level recursive build in safe mode
def recursive_build_sup_lvl_safe_mode(current,indice):
	res = []
	#//
	for i in current:
		res.append(str(indice)+str(i))
	return res

# final level recursive build (the best one) 
def recursive_build_sup_lvl(table_base,current,lvl):
	res   = []
	break_ind = 0
	#//
	for i in table_base:	
		try :
			res.extend(recursive_build_sup_lvl_safe_mode(current,i))
		except:
			print("break in method : recursive_build_sup_lvl")
			break_ind=1
			break
	return (res,break_ind)

def table():
	rec_level_h = [6,6,6,6,6,5,5,5,5,5,5,5,5,5,5,5,5,4,4,4,4,4,4,4,4,4]
	rec_level_m = [5,5,5,5,5,4,4,4,4,4,4,4,4,4,4,4,4,3,3,3,3,3,3,3,3,3]
	rec_level_l = [4,4,4,4,4,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]
	table       = []
	bases       = []
	tmp         = ()
	ok          = 0
	mini        = 11
	mytime      = 0
	fini        = 0
	finalt      = 0

	for i in range (mini,37):
		ind = 1
		ok  = 0
		bases.append(tablebase(i))
		table.append(recursive_build(bases[i-mini]))
		# print(table[i-mini])
		# print(bases[i-mini])
		while(not ok):
			# print("i-mini = "+str(i-mini)+" | len table = "+str(len(table[i-mini]))+" | ok = "+str(ok))
			tmp=recursive_build_sup_lvl(bases[i-mini],table[i-mini],ind)
			table[i-mini]=tmp[0]
			ind+=1
			# print("recursive level "+str(ind))
			if(ind==rec_level_l[i-mini]):
				ok=1
	return table

def crypto_procedure():
	"""*
		This is the main algorithm of the program.
		It allows from a system argv string to crypt it and get a string,key couple as result.
		We will use this following variables to make it work :

			* **table2** : A list of list containing all the necessary Base table from Base 11 to Base 37
			* **Basemin** : 2 as default, it means the minimum base index to generate
			* **Basemax** :  37 as default, it means the maximum base index to generate
			* **chaine** : The string chain to crypt as system argv argument
			* **choice** : A choice variable to manage the main loop (continue or quit)
			* **Range** : Define the range of values generate into the corresponding Numeric Base a the begining	

		The return of the algorithm is ruled by the following variables:

			* **testkey** : The final half key as key
			* **raw_txt** : The final crypted strin as string.

		This is the main Raptor Cryptographic Algorithm v3. It is ruled by the following steps :

			* **Initialization** of differents variables and of the Base table via the table generator methods
			* **Splitting** part of the given raw string as input. This string will be splitted into differents slices, wiche be crypted one by one and associated to his key via the third level separators wich define the third level of the crypting tree.
			* **Crypting procedure** for each of the slices obtained by the split method above. These crypted results will be stored as a list of list, respectively a list of slices, defined by a list of crypted terms.
			* **Manage the results** via slurp2 and slurp3 methods. The results are properly stored at this time to be correctly interpreted later.
			* **Give a wrong path** for decrypting using some fake values to both of crypted txt and key as strings. It means any Brute force attack will be ignored.
			* **Returns** the couple (crypt txt, key) wich is efficient to be decrypted by the solver.


		This algorithm is stable in his domain and must be used on it.
		Please not to try bigger data slice and automate it via shell script if necessary.
		It should be used as a data crypter using a top level slicer and manager (from the shell script as exemple).

		See source below to more explanation.

		.. code-block:: python	

			represent=''
			table2 = []
			dic = {}
			main_dic={}
			choice = ' '
			chaine=''
			chaine=sys.argv[1]

			if(len(sys.argv)!=4):
				Basemin = 2
				Basemax = 37
				Range   = 36**2
			else : 	
				Basemin = int(sys.argv[1])
				Basemax = int(sys.argv[2])
				Range   = int(sys.argv[3])

			if(Basemin<2 or Basemax>37):
				print("Affichage impossible veuillez selectionner une plage de valeure contenue dans [2,36]")
				exit(0)

			maxi=Basemax-Basemin
			table2=table()
			long_chaine = []
			long_crypt  = []
			longi=0
			seuil = 20
			seuil_lvl2=70
			choice = ''
			userchoice=0
			sep=['!','"','#','$','%','&','(',')','*','+',',','-','.','/']
			sep_lvl2=[":",";","<","=",">","?","@"]
			sep_lvl3=['A','B','C','D','E','F','G','H','I','J','K','L'] 
			mesquin=['M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

			long_long_chaine = []
			tmp_long_chaine  = []
			long_chaine      = []
			long_crypt       = []
			testc            = []
			testk            = []
			int_chaine       = []
			lvl2_key_miam    = []
			tmp_crypt        = []


			while(choice!='q'):
				# init_all()
				current_sep_lvl3    =  "A"
				current_sep_lvl2    =  ":"
				long_chaine[:]      = []
				long_crypt[:]       = []
				long_long_crypt     = []
				testc[:]            = []
				testk[:]            = []
				int_chaine[:]       = []
				lvl2_key_miam[:]    = []
				long_long_chaine[:] = []
				tmp_long_chaine[:]  = []
				tmp_crypt           = ()
				testkey             = ''
				raw_txt             = ''
				clean_txt           = ''
				longi               = 0
				longii              = 0
				res                 = ()

				if(userchoice):
					chaine = ''
					chaine=input("Veuillez entrer la chaine à crypter : ")
				if(len(chaine)>=seuil and len(chaine)<seuil_lvl2):
					long_chaine = split(chaine,seuil)
					longi+=1
				else: 
					if(len(chaine)>=seuil_lvl2):
						tmp_long_chaine = split(chaine,seuil_lvl2)
						for i in range(0,len(tmp_long_chaine)):
							long_long_chaine.append(split(tmp_long_chaine[i],seuil))
						longii+=1
				if(not longi and not longii):
					res=crypt_procedure(chaine,table2)
				else :
					if(longi):
						for i in range(0,len(long_chaine)):
							long_crypt.append(crypt_procedure(long_chaine[i],table2))
					if(longii):
						for i in range (0,len(long_long_chaine)):
							for j in range(0,len(long_long_chaine[i])):
								tmp_crypt = crypt_procedure(long_long_chaine[i][j],table2)
								long_long_crypt.append(tmp_crypt)
						# print(long_crypt[-1][0])
				if(not longi and not longii):
					testc = res[0]
					testk = res[1]
				else :
					if (longi):
						for i in range (0,len(long_crypt)):
							for j in range(0,len(long_crypt[i][0])):
								testc.append(str(long_crypt[i][0][j]))				
							for k in range(0,len(long_crypt[i][1])):
								testk.append(str(long_crypt[i][1][k]))				
							current_sep_lvl2=cyclik_ascii_lvl2(current_sep_lvl2)
							testc[-1]+=current_sep_lvl2
							testk[-1]+=current_sep_lvl2
					if(longii):
						for l in range (0,len(long_long_crypt)):
							# print(long_long_crypt[l])
							for j in range(0,len(long_long_crypt[l][0])):
								testc.append(str(long_long_crypt[l][0][j]))	
							for k in range(0,len(long_long_crypt[l][1])):		
								testk.append(str(long_long_crypt[l][1][k]))
							current_sep_lvl2=cyclik_ascii_lvl2(current_sep_lvl2)
							testc[-1]+=current_sep_lvl2
							testk[-1]+=current_sep_lvl2		
							# print("l = "+str(l)+" | len long[l] = "+str(len(long_long_crypt[l][0])))			
							if(len(long_long_crypt[l][0])<seuil):	
								current_sep_lvl3=cyclik_ascii_lvl3(current_sep_lvl3)
								testc[-1]+=current_sep_lvl3
								testk[-1]+=current_sep_lvl3	
					# print(testc)
					# print(testk)
				int_chaine=(ascii_to_int(chaine))
				for i in range(0,len(testk)):
					testkey+=str(testk[i])
				if(not longi and not longii):
					raw_txt = crypt_final(res,int_chaine,table2)
				else:
					raw_txt += crypt_final_long(testc,int_chaine,table2)
				raw_txt=mesqui(raw_txt,seuil)
				testkey=mesqui(testkey,seuil)
				print("---------------------------------")
				print("Chaine cryptée : \n")
				print(raw_txt)
				print("---------------------------------")
				print("Clé unique : \n")
				print(testkey)
				print("---------------------------------")
				choice=input("c)ontinuer ou q)uitter")
				if(choice!='q'):
					userchoice+=1
	"""
	represent=''
	table2 = []
	dic = {}
	main_dic={}
	choice = ' '
	chaine=''
	chaine=sys.argv[1]

	if(len(sys.argv)!=4):
		Basemin = 2
		Basemax = 37
		Range   = 36**2
	else : 	
		Basemin = int(sys.argv[1])
		Basemax = int(sys.argv[2])
		Range   = int(sys.argv[3])

	if(Basemin<2 or Basemax>37):
		print("Affichage impossible veuillez selectionner une plage de valeure contenue dans [2,36]")
		exit(0)

	maxi=Basemax-Basemin
	table2=table()
	long_chaine = []
	long_crypt  = []
	longi=0
	seuil = 20
	seuil_lvl2=70
	choice = ''
	userchoice=0
	sep=['!','"','#','$','%','&','(',')','*','+',',','-','.','/']
	sep_lvl2=[":",";","<","=",">","?","@"]
	sep_lvl3=['A','B','C','D','E','F','G','H','I','J','K','L'] 
	mesquin=['M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

	long_long_chaine = []
	tmp_long_chaine  = []
	long_chaine      = []
	long_crypt       = []
	testc            = []
	testk            = []
	int_chaine       = []
	lvl2_key_miam    = []
	tmp_crypt        = []


	while(choice!='q'):
		# init_all()
		current_sep_lvl3    =  "A"
		current_sep_lvl2    =  ":"
		long_chaine[:]      = []
		long_crypt[:]       = []
		long_long_crypt     = []
		testc[:]            = []
		testk[:]            = []
		int_chaine[:]       = []
		lvl2_key_miam[:]    = []
		long_long_chaine[:] = []
		tmp_long_chaine[:]  = []
		tmp_crypt           = ()
		testkey             = ''
		raw_txt             = ''
		clean_txt           = ''
		longi               = 0
		longii              = 0
		res                 = ()

		# if(userchoice):
		# 	chaine = ''
		# 	chaine=input("Veuillez entrer la chaine à crypter : ")
		# if(len(chaine)>=seuil and len(chaine)<seuil_lvl2):
		# 	long_chaine = split(chaine,seuil)
		# 	longi+=1
		# else: 
		# 	if(len(chaine)>=seuil_lvl2):
		# 		tmp_long_chaine = split(chaine,seuil_lvl2)
		# 		for i in range(0,len(tmp_long_chaine)):
		# 			long_long_chaine.append(split(tmp_long_chaine[i],seuil))
		# 		longii+=1
		# if(not longi and not longii):
		# 	res=crypt_procedure(chaine,table2)
		# else :
		# 	if(longi):
		# 		for i in range(0,len(long_chaine)):
		# 			long_crypt.append(crypt_procedure(long_chaine[i],table2))
		# 	if(longii):
		# 		for i in range (0,len(long_long_chaine)):
		# 			for j in range(0,len(long_long_chaine[i])):
		# 				tmp_crypt = crypt_procedure(long_long_chaine[i][j],table2)
		# 				long_long_crypt.append(tmp_crypt)
		# 		# print(long_crypt[-1][0])
		# if(not longi and not longii):
		# 	testc = res[0]
		# 	testk = res[1]
		# else :
		# 	if (longi):
		# 		for i in range (0,len(long_crypt)):
		# 			for j in range(0,len(long_crypt[i][0])):
		# 				testc.append(str(long_crypt[i][0][j]))				
		# 			for k in range(0,len(long_crypt[i][1])):
		# 				testk.append(str(long_crypt[i][1][k]))				
		# 			current_sep_lvl2=cyclik_ascii_lvl2(current_sep_lvl2)
		# 			testc[-1]+=current_sep_lvl2
		# 			testk[-1]+=current_sep_lvl2
		# 	if(longii):
		# 		for l in range (0,len(long_long_crypt)):
		# 			# print(long_long_crypt[l])
		# 			for j in range(0,len(long_long_crypt[l][0])):
		# 				testc.append(str(long_long_crypt[l][0][j]))	
		# 			for k in range(0,len(long_long_crypt[l][1])):		
		# 				testk.append(str(long_long_crypt[l][1][k]))
		# 			current_sep_lvl2=cyclik_ascii_lvl2(current_sep_lvl2)
		# 			testc[-1]+=current_sep_lvl2
		# 			testk[-1]+=current_sep_lvl2		
		# 			# print("l = "+str(l)+" | len long[l] = "+str(len(long_long_crypt[l][0])))			
		# 			if(len(long_long_crypt[l][0])<seuil):	
		# 				current_sep_lvl3=cyclik_ascii_lvl3(current_sep_lvl3)
		# 				testc[-1]+=current_sep_lvl3
		# 				testk[-1]+=current_sep_lvl3	
		# 	# print(testc)
		# 	# print(testk)
		# int_chaine=(ascii_to_int(chaine))
		# for i in range(0,len(testk)):
		# 	testkey+=str(testk[i])
		# if(not longi and not longii):
		# 	raw_txt = crypt_final(res,int_chaine,table2)
		# else:
		# 	raw_txt += crypt_final_long(testc,int_chaine,table2)
		# raw_txt=mesqui(raw_txt,seuil)
		# testkey=mesqui(testkey,seuil)
		# print("---------------------------------")
		# print("Chaine cryptée : \n")
		# print(raw_txt)
		# print("---------------------------------")
		# print("Clé unique : \n")
		# print(testkey)
		# print("---------------------------------")

		raw_txt=input("Veuillez entrer la chaine cryptée : \n")
		testkey=input("Veuillez saisir la clé : \n")
		if(len(raw_txt)>=seuil*6 and len(raw_txt)<seuil_lvl2*6):
			long_chaine = split(raw_txt,seuil)
			longi+=1
		else: 
			if(len(raw_txt)>=seuil_lvl2*6):
				tmp_long_chaine = split(raw_txt,seuil_lvl2*6)
				for i in range(0,len(tmp_long_chaine)):
					long_long_chaine.append(split(tmp_long_chaine[i],seuil))
				longii+=1

		raw_txt = slurp3(raw_txt)
		testkey = slurp3(testkey)
		if(not longi and not longii):
			clean_txt = decrypt_procedure(raw_txt,testk,table2)
		else:
			if(longi):
				lvl2_liste = []
				lvl2_key   = []
				lvl2_liste = slurp2(raw_txt)		
				lvl2_key   = slurp2(testkey)
				lvl2_key_miam = []
				# print(lvl2_liste)
				# print(lvl2_key)
				for i in range (0,len(lvl2_key)):
					lvl2_key_miam.append(miam(lvl2_key[i]))
				# print(lvl2_key_miam)
				for i in range (0,len(lvl2_liste)-1):
					clean_txt+= decrypt_procedure(lvl2_liste[i],lvl2_key_miam[i],table2)
			if(longii):
				lvl3_liste = []
				lvl3_key   = []
				lvl3_liste = slurp4(raw_txt)
				lvl3_key   = slurp4(testkey)
				lvl2_liste = []
				lvl2_key   = []
				lvl2_key_miam = []
				final_key  = []
				for i in range (0,len(lvl3_key)):
					lvl2_key.append(slurp2(lvl3_key[i]))
				for i in range (0,len(lvl3_liste)-1):
					lvl2_liste.append(slurp2(lvl3_liste[i]))
				for i in range(0,len(lvl2_key)-1):
					lvl2_key_miam[:] = []
					for j in range (0,len(lvl2_key[i])):
						lvl2_key_miam.append(miam(lvl2_key[i][j]))
						# print("miam")
						# print(lvl2_key_miam)
					del lvl2_key_miam[-1]
					final_key.append(lvl2_key_miam)
					# print("final")
					# print(final_key)
					# print("liste : "+str(len(lvl2_liste))+" | key "+str(len(final_key)))
					for k in range (0,len(lvl2_liste[i])-1):
						# print("lvl2[i][k] : ")
						# print(lvl2_liste[i][k])
						# print(final_key[0][k])
						clean_txt+=decrypt_procedure(lvl2_liste[i][k],final_key[0][k],table2)
						# print(str(k) + "/" + str(len(lvl2_liste[i])-2))
					# print(str(i)+" / "+str(len(lvl2_key)-1))

		print("Chaine décryptée : \n")
		print(clean_txt)
		choice=input("c)ontinuer ou q)uitter")
		if(choice!='q'):
			userchoice+=1

def decrypto_procedure():
	"""
		This is the main solver algorithm program.
		It allow us to decrypt datas slices crypted with the version 1 of the Raptor Cryptographic Algorithm.
		To solve I need thse following variables :

			* **raw_txt** : The input crypted string storage
			* **Basemin** : The minimum Base index 
			* **Basemax** : The maximum Base index
			* **table2** : The list of list containing the Base Table
			* **testkey** : The key of the algorithm, the decrypting process absolutely need this key.
			
		The solving procedure is ruled by the following steps:

			* **Generating the Base Table** and store it into my table2 variable
			* **Getting inputs** known as crypted string and his associated key.
			* **Organize data slice** removing separators via the slurps methods
			* **Decrypting process** using the decrypt_procedure method (see documentation)
			* **Store and return** the results of decrypting process

		.. code-block:: python	

			represent=''
			table2 = []
			dic = {}
			main_dic={}
			choice = ' '
			chaine=''
			chaine=sys.argv[1]

			if(len(sys.argv)!=4):
				Basemin = 2
				Basemax = 37
				Range   = 36**2
			else : 	
				Basemin = int(sys.argv[1])
				Basemax = int(sys.argv[2])
				Range   = int(sys.argv[3])

			if(Basemin<2 or Basemax>37):
				print("Affichage impossible veuillez selectionner une plage de valeure contenue dans [2,36]")
				exit(0)

			maxi=Basemax-Basemin
			table2=table()
			long_chaine = []
			long_crypt  = []
			longi=0
			seuil = 20
			seuil_lvl2=70
			choice = ''
			userchoice=0
			sep=['!','"','#','$','%','&','(',')','*','+',',','-','.','/']
			sep_lvl2=[":",";","<","=",">","?","@"]
			sep_lvl3=['A','B','C','D','E','F','G','H','I','J','K','L'] 
			mesquin=['M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

			long_long_chaine = []
			tmp_long_chaine  = []
			long_chaine      = []
			long_crypt       = []
			testc            = []
			testk            = []
			int_chaine       = []
			lvl2_key_miam    = []
			tmp_crypt        = []


			while(choice!='q'):
				# init_all()
				current_sep_lvl3    =  "A"
				current_sep_lvl2    =  ":"
				long_chaine[:]      = []
				long_crypt[:]       = []
				long_long_crypt     = []
				testc[:]            = []
				testk[:]            = []
				int_chaine[:]       = []
				lvl2_key_miam[:]    = []
				long_long_chaine[:] = []
				tmp_long_chaine[:]  = []
				tmp_crypt           = ()
				testkey             = ''
				raw_txt             = ''
				clean_txt           = ''
				longi               = 0
				longii              = 0
				res                 = ()

				raw_txt=input("Veuillez entrer la chaine cryptée : \n")
				testkey=input("Veuillez saisir la clé : \n")
				if(len(raw_txt)>=seuil*6 and len(raw_txt)<seuil_lvl2*6):
					long_chaine = split(raw_txt,seuil)
					longi+=1
				else: 
					if(len(raw_txt)>=seuil_lvl2*6):
						tmp_long_chaine = split(raw_txt,seuil_lvl2*6)
						for i in range(0,len(tmp_long_chaine)):
							long_long_chaine.append(split(tmp_long_chaine[i],seuil))
						longii+=1

				raw_txt = slurp3(raw_txt)
				testkey = slurp3(testkey)
				if(not longi and not longii):
					clean_txt = decrypt_procedure(raw_txt,testk,table2)
				else:
					if(longi):
						lvl2_liste = []
						lvl2_key   = []
						lvl2_liste = slurp2(raw_txt)		
						lvl2_key   = slurp2(testkey)
						lvl2_key_miam = []
						# print(lvl2_liste)
						# print(lvl2_key)
						for i in range (0,len(lvl2_key)):
							lvl2_key_miam.append(miam(lvl2_key[i]))
						# print(lvl2_key_miam)
						for i in range (0,len(lvl2_liste)-1):
							clean_txt+= decrypt_procedure(lvl2_liste[i],lvl2_key_miam[i],table2)
					if(longii):
						lvl3_liste = []
						lvl3_key   = []
						lvl3_liste = slurp4(raw_txt)
						lvl3_key   = slurp4(testkey)
						lvl2_liste = []
						lvl2_key   = []
						lvl2_key_miam = []
						final_key  = []
						for i in range (0,len(lvl3_key)):
							lvl2_key.append(slurp2(lvl3_key[i]))
						for i in range (0,len(lvl3_liste)-1):
							lvl2_liste.append(slurp2(lvl3_liste[i]))
						for i in range(0,len(lvl2_key)-1):
							lvl2_key_miam[:] = []
							for j in range (0,len(lvl2_key[i])):
								lvl2_key_miam.append(miam(lvl2_key[i][j]))
								# print("miam")
								# print(lvl2_key_miam)
							del lvl2_key_miam[-1]
							final_key.append(lvl2_key_miam)
							# print("final")
							# print(final_key)
							# print("liste : "+str(len(lvl2_liste))+" | key "+str(len(final_key)))
							for k in range (0,len(lvl2_liste[i])-1):
								# print("lvl2[i][k] : ")
								# print(lvl2_liste[i][k])
								# print(final_key[0][k])
								clean_txt+=decrypt_procedure(lvl2_liste[i][k],final_key[0][k],table2)
								# print(str(k) + "/" + str(len(lvl2_liste[i])-2))
							# print(str(i)+" / "+str(len(lvl2_key)-1))

				print("Chaine décryptée : \n")
				print(clean_txt)
				choice=input("c)ontinuer ou q)uitter")
				if(choice!='q'):
					userchoice+=1		
	"""