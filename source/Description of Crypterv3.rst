Description of Crypter
======================


Welcom to Raptor cryptographic help

This following instructions give you the full light on the given cryptographic algorithm "Raptor".
In a firts time I will explain the main algorithm rules. Each of the function used can be found on the
full source code and have a dedicated help section.

**Description of the Main Raptor's Cryptographic Algorithm**

_________________________________________________________________

**Algorithm**
-------------

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

_________________________________________________________________

**Source Code**
---------------

.. code-block:: python	

	import sys 
	import math as m
	import random as r
	
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

	for i in range(Basemin,Basemax):
		table2.append(table(i,0,Range,1))

	for i in range (0,len(table2)):
		table2[i]=splitTable(table2[i])

	for j in range (0,len(table2)):
		table2[j]=rec_table_construct_lvl1(table2[j],j+2,1,0)
		for k in range(0,j+2):
			table2[j][k]=(str(0)+table2[j][k])
	table2=rec_manage(table2)


	# print("Max int = "+str(sys.maxsize))
	# for i in range(9,len(table2)):
	# 	print("Length Base "+str(i+2)+" = "+str(len(table2[i])))
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
	long_chaine   = []
	long_crypt    = []
	testc         = []
	testk         = []
	int_chaine    = []
	lvl2_key_miam = []
	tmp_crypt     = []


	while(choice!='q'):
		# init_all()
		current_sep_lvl3 =  "A"
		current_sep_lvl2 =  ":"
		long_chaine  = []
		long_crypt    = []
		long_long_crypt  = []
		testc         = []
		testk         = []
		int_chaine    = []
		lvl2_key_miam = []
		long_long_chaine = []
		tmp_long_chaine  = []
		tmp_crypt        = ()
		testkey=''
		raw_txt=''
		clean_txt = ''
		longi = 0
		longii= 0

		res = ()
		if(userchoice):
			chaine = ""
			chaine=input("Veuillez entrer la chaine à crypter  (>20): ")
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
					# current_sep_lvl3=cyclik_ascii_lvl3(current_sep_lvl3)
					# testc[-1]+=current_sep_lvl3
					# testk[-1]+=current_sep_lvl3	
		int_chaine=(ascii_to_int(chaine))
		# sepk=sep[int(int_chaine[1]*m.cos(int_chaine[0]))%13] 
		for i in range(0,len(testk)):
			testkey+=str(testk[i])
			# testkey+=sepk
			# sepk=cyclik_ascii(sepk)
		
		if(not longi and not longii):
			raw_txt = crypt_final(res,int_chaine)
		else:
			raw_txt += crypt_final_long(testc,int_chaine)
		raw_txt=mesqui(raw_txt,seuil)
		testkey=mesqui(testkey,seuil)
		print("---------------------------------")
		print("Chaine cryptée : \n")
		print(raw_txt)
		print("---------------------------------")
		print("Clé unique : \n")
		print(testkey)
		print("---------------------------------")
