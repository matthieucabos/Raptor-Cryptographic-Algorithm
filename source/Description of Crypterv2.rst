Description of Crypter
======================

Welcome to Raptor cryptographic help

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


The alorithm is ruled by the following steps :

	* **Generating the first step Base table** for each necessary numeric base via the function table and splitTable
	* **Recursive build of the full Base table** since the first step table using functions : 

		* **rec_table_construct_lvl1** : It draw the 'zero theorem' of Table construction since the first step. Must be considered as te first loop of recursive builder algorithm
		* **rec_manage** : It draw the full Base Table using recursive loop

	* **Initialization** : Instanciation of the local varables to manipulate the algorithm
	* **Split** : I crypt the data string as input using slices of the string vector. Using a loop, I will crypt each slices independantly from each others. It permits us to have a full crypted string more complex than the first version of algorithm
	* **Crypting Slices** : Once each slices properly cutted, we have to crypt each of them using the crypt_procedure automated on a loop coursing each of them.
	* **Manage Slices** : The crypted slices are managed via a second level separators set wich define a second level of crypting tree. In fact each term of a slice is using a first level of separators, it give a one-level tree. The second level permit to complexify the full algorithm result.
	* **Rebuild results** : Finally, the crypt_procedure function is used to associate each crypted slice to his key and draw a correct interpretated result as list of couple (crypted string/integer key)
	* **Return results** : The couple full result rebuilded from slices couple is organized from the second level separators to draw a 2-level tree 

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


	# print("Max int = "+str(sys.maxsize))
	# for i in range(9,len(table2)):
	# 	print("Length Base "+str(i+2)+" = "+str(len(table2[i])))

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
		if(userchoice):
			chaine = ''
			chaine=input("Veuillez entrer la chaine à crypter : ")
		if(len(chaine)>=20):
			long_chaine = split(chaine,seuil)
			longi+=1	
		if(not longi):
			res=crypt_procedure(chaine,table2)
		else :
			for i in range(0,len(long_chaine)):
				long_crypt.append(crypt_procedure(long_chaine[i],table2))
				# print(long_crypt[-1][0])
		if(not longi):
			testc = res[0]
			testk = res[1]
		else :
			for i in range (0,len(long_crypt)):
				for j in range(0,len(long_crypt[i][0])):
					testc.append(str(long_crypt[i][0][j]))				
				for k in range(0,len(long_crypt[i][1])):
					testk.append(str(long_crypt[i][1][k]))				
				current_sep_lvl2=cyclik_ascii_lvl2(current_sep_lvl2)
				testc[-1]+=current_sep_lvl2
				testk[-1]+=current_sep_lvl2
		
		int_chaine=(ascii_to_int(chaine))
		# sepk=sep[int(int_chaine[1]*m.cos(int_chaine[0]))%13] 
		for i in range(0,len(testk)):
			testkey+=str(testk[i])
			# testkey+=sepk
			# sepk=cyclik_ascii(sepk)
		
		if(not longi):
			raw_txt = crypt_final(res,int_chaine)
		else:
			raw_txt += crypt_final_long(testc,int_chaine)

		print("---------------------------------")
		print("Chaine cryptée : \n")
		print(raw_txt)
		print("---------------------------------")
		print("Clé unique : \n")
		print(testkey)
		print("---------------------------------")

