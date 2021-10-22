Description of De-crypter
=========================

**Description of the Main Raptor's Cryptographic Algorithm**

_________________________________________________________________

**Algorithm**
-------------

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

	#system check routine
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

	#init routine
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

	#second level local declaration
	long_chaine = []
	long_crypt  = []
	longi=0
	seuil = 20
	choice = ''
	userchoice=0
	#definition of sets
	sep=['!','"','#','$','%','&','(',')','*','+',',','-','.','/']
	sep_lvl2=[":",";","<","=",">","?","@"]
	long_chaine   = []
	long_crypt    = []
	testc         = []
	testk         = []
	int_chaine    = []
	lvl2_key_miam = []

	#main algorithm
	while(choice!='q'):
		# init_all()
		current_sep_lvl2 =  ":"
		long_chaine[:]   = []
		long_crypt[:]    = []
		testc[:]         = []
		testk[:]         = []
		int_chaine[:]    = []
		lvl2_key_miam[:] = []
		testkey=''
		raw_txt=''
		clean_txt = ''
		longi = 0

		res = ()
		raw_txt=input('Chaine cryptée : ')
		testkey=input('Clé unique : ')
		if(len(raw_txt)>=120):
			longi=1
		if(not longi):
			testkey=miam(testkey)
			clean_txt = decrypt_procedure(raw_txt,testkey,table2)
		else:
			lvl2_liste = []
			lvl2_key   = []
			lvl2_liste = slurp2(raw_txt)		
			lvl2_key   = slurp2(testkey)
			lvl2_key_miam = []
			for i in range (0,len(lvl2_key)):
				lvl2_key_miam.append(miam(lvl2_key[i]))
			for i in range (0,len(lvl2_liste)-1):
				clean_txt+= decrypt_procedure(lvl2_liste[i],lvl2_key_miam[i],table2)
		print("Chaine décryptée : \n")
		print(clean_txt)
		choice=input("c)ontinuer ou q)uitter")
		if(choice!='q'):
			userchoice+=1