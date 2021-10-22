Description of De-crypter
=========================

**Description of the Main Raptor's Cryptographic Algorithm**

_________________________________________________________________

**Algorithm**
-------------

**Description of the Main Raptor's Cryptographic Algorithm**

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