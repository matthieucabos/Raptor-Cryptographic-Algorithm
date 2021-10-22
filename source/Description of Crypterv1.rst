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

The return of the algorithm is ruled by the fllowing variables:
	* **testkey** : The final half key as key
	* **raw_txt** : The final crypted strin as string.


The alorithm is ruled by the following steps :
	* Generating the first step Base table for each necessary numeric base via the function table and splitTable
	* Recursive build of the full Base table since the first step table using functions : 
		* rec_table_construct_lvl1 : It draw the 'zero theorem' of Table construction since the first step. Must be considered as te first loop of recursive builder algorithm
		* rec_manage : It draw the full Base Table using recursive loop

	* Instanciation of the local varables to manipulate the algorithm
	* I crypt the string using the crypt_procedure function. The return is a couple (crypt text / key) wich allow to decrypt it.
	* The crypt_final method allow us to organise the crypt list into interpretables results. We store results in variables:
		* **raw_txt** : Contains the raw crypted text as string
		* **testkey** : Contains the half key as str(int)

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

	represent=''
	table2 = []
	dic = {}
	main_dic={}
	choice = ' '
	chaine=''
	choice=''
	try : chaine=sys.argv[1]
	except : print("")

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
	testc=[]
	testk=[]
	while(choice!='q'):
		chaine=''
		res = ()
		testc[:]=[]
		testk[:]=[]
		raw_txt=''
		testkey=''
		while(len(chaine)>=29 or len(chaine)==0):
			chaine=input("Veuillez entrer une chaine <29 : \n")
		res=crypt_procedure(chaine,table2)
		testc = res[0]
		testk = res[1]
		for i in range(0,len(testk)):
			testkey+=str(testk[i])
		raw_txt = crypt_final(res)
		print("----------------------------------------------------------------------------------")
		print("Chaine cryptée : \n")
		print(raw_txt)
		print("----------------------------------------------------------------------------------")
		print("Clé unique : \n")
		print(testkey)
		print("----------------------------------------------------------------------------------")
		clean_txt = decrypt_procedure(raw_txt,testk,table2)
		print("Chaine décryptée : \n")
		print(clean_txt)
		choice=input("c)ontinuer ou q)uitter?")
