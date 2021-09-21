import sys
import time
# from mouchar import *
#Author : CABOS Matthieu
#Date : 06/2018

def tablebase(base):
	"""
		This method allow to build the first step Numeric Base Transposition Table.
		I use the Horner's scheme procedure to build the correct table independantly of the base index.
		I can build Base from 1->a to 1->z, mean Base11 to Base36.
			
		=============== ========== ===========================
		**Parameters**   **Type**   **Description**
		*base*            int        The base index to build
		=============== ========== ===========================

		Returns
		=======
		list res : The builded first step base table.

		Examples
		========
		>>> t=tablebase(16)
		>>> print(t)
		['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']


		.. code-block:: python	

			res = []
			letter = 'a'
			# //
			for i in range(0,base):
				if(i<10 or (i<=10 and base <=10)):
					res.append(str(i))
				if(i>=10 and base >10):
					res.append(letter)
					letter=chr(ord(letter)+1)
			return res
	"""
	res = []
	letter = 'a'
	# //
	for i in range(0,base):
		if(i<10 or (i<=10 and base <=10)):
			res.append(str(i))
		if(i>=10 and base >10):
			res.append(letter)
			letter=chr(ord(letter)+1)
	return res

def recursive_build(table_base):
	"""
		This function recursively build a full Base Table from an existing one.
		You can pass the first step table as already builded recursive table.

		=============== =========== ============================
		**Parameters**    **Type**   **Description**
		*table_base*       list        Base Table array as list
		=============== =========== ============================

		Returns
		=======
		str list res : The recursively builded Base Table

		Examples
		========
		>>> t=tablebase(16)
		>>> print(t)
		['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
		>>> rt=recursive_build(t)
		>>> print(rt)
		['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '0a', '0b', '0c', '0d', '0e', '0f', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '1a', '1b', '1c', '1d', '1e', '1f', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '2a', '2b', '2c', '2d', '2e', '2f', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '3a', '3b', '3c', '3d', '3e', '3f', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '4a', '4b', '4c', '4d', '4e', '4f', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '5a', '5b', '5c', '5d', '5e', '5f', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '6a', '6b', '6c', '6d', '6e', '6f', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '7a', '7b', '7c', '7d', '7e', '7f', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '8a', '8b', '8c', '8d', '8e', '8f', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '9a', '9b', '9c', '9d', '9e', '9f', 'a0', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9', 'aa', 'ab', 'ac', 'ad', 'ae', 'af', 'b0', 'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'b9', 'ba', 'bb', 'bc', 'bd', 'be', 'bf', 'c0', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9', 'ca', 'cb', 'cc', 'cd', 'ce', 'cf', 'd0', 'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9', 'da', 'db', 'dc', 'dd', 'de', 'df', 'e0', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'e9', 'ea', 'eb', 'ec', 'ed', 'ee', 'ef', 'f0', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'fa', 'fb', 'fc', 'fd', 'fe', 'ff']

		.. code-block:: python	

			res = []
			# //*2
			for i in table_base:
				for j in table_base:
					res.append(i+j)

			return res
	"""
	res = []
	# //*2
	for i in table_base:
		for j in table_base:
			res.append(i+j)

	return res

def recursive_build_sup_lvl_safe_mode(current,indice):
	"""
		The variable indeice correspond to the pow index of the current recursive build.
		The current argument contain the current Base Tale array as list.
		Using once again the Horner's scheme, we can build each sup level without be limited by internal constraints.

		Examples
		========
		>>> t=tablebase(16)
		>>> print(t)
		['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
		>>> rt=recursive_build_sup_lvl_safe_mode(t,1)
		>>> print(rt)
		['10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '1a', '1b', '1c', '1d', '1e', '1f']

		.. code-block:: python	

			res = []
			#//
			for i in current:
				# try:
				res.append(str(indice)+str(i))
				# except:
					# print("break in method : recursive_build_sup_lvl_safe_mode")
					# break
			return res
	"""
	res = []
	#//
	for i in current:
		# try:
		res.append(str(indice)+str(i))
		# except:
			# print("break in method : recursive_build_sup_lvl_safe_mode")
			# break
	return res

def recursive_build_sup_lvl(table_base,current,lvl):
	"""
		The recursive_build_sup_lvl method is used to manage recursivity of the algorithm. 
		I mean i have wrote the iterative version of the recursive function. So you can easely use it and control it.

		=============== ============ ========================================
		**Parameters**    **Type**    **Description**
		*table_base*       str list   my first step Base table array as list
		*current*          str list   my current Base table array as list
		*lvl*              int        Define the level of recursivity
		=============== ============ ========================================
 
		Examples
		========
		>>> t=tablebase(16)
		>>> print(t)
		['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
		>>> rtt=recursive_build_sup_lvl(t,t,0)
		>>> print(rtt)
		(['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '0a', '0b', '0c', '0d', '0e', '0f', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '1a', '1b', '1c', '1d', '1e', '1f', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '2a', '2b', '2c', '2d', '2e', '2f', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '3a', '3b', '3c', '3d', '3e', '3f', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '4a', '4b', '4c', '4d', '4e', '4f', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '5a', '5b', '5c', '5d', '5e', '5f', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '6a', '6b', '6c', '6d', '6e', '6f', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '7a', '7b', '7c', '7d', '7e', '7f', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '8a', '8b', '8c', '8d', '8e', '8f', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '9a', '9b', '9c', '9d', '9e', '9f', 'a0', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9', 'aa', 'ab', 'ac', 'ad', 'ae', 'af', 'b0', 'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'b9', 'ba', 'bb', 'bc', 'bd', 'be', 'bf', 'c0', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9', 'ca', 'cb', 'cc', 'cd', 'ce', 'cf', 'd0', 'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9', 'da', 'db', 'dc', 'dd', 'de', 'df', 'e0', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'e9', 'ea', 'eb', 'ec', 'ed', 'ee', 'ef', 'f0', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'fa', 'fb', 'fc', 'fd', 'fe', 'ff'], 0)
	
		.. code-block:: python	

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
	"""
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

# base  = int(sys.argv[1])
# test1 = []
# test2 = []
# tmp = ()
# print("test tablebase : ")
# test1=tablebase(base)
# print(test1)
# print("test : done\n")
# print("test recursive_buid : ")
# test2=recursive_build(test1)
# print(test2)
# print("test : done\n")
# print("test recursive_build_sup_lvl_safe_mode : ")
# test2=recursive_build_sup_lvl_safe_mode(test1,'e')
# print(test2)
# print("test : done\n")
# print("test recursive_build_sup_lvl 1 : ")
# test1=tablebase(base)
# tmp=recursive_build_sup_lvl(test1,test1,1)
# test2=tmp[0]
# print(len(test2))
# print("test recursive_build_sup_lvl full range : ")
# ind = 2
# while(1):
# 	tmp=recursive_build_sup_lvl(test1,test2,ind)
# 	test2=tmp[0]
# 	ind+=1
# 	print("recursive level "+str(ind))
# 	if(tmp[1]==1):
# 		break
# print("test : done \n")
# print(len(test2))
# print(test2[0])
# print(test2[-1])

def table():
	"""
		This is the main Base Table Builder Algorithm.
		The algorithm is ruled by these following steps :
			* **Init time** : I init Time variable using the time library from Python
			* **First Step Base Table** : This is the first step of the builder, I build the basic table from the tablebase function
			* **First level of recursivity** : I build the first level of recursivity in safe mode using recursive_build function
			* **Full Recursive algorithm** : We get the full computation of the table via the recursive_build_sup_lvl method.
			* **Time calculation** : Computation of necessary time for the construction of the full array

		Returns
		=======
		list of list : A list of list containing all the string values representing the full generateed Base Table array

		Examples
		========
		>>> t=table()
		test full tables recursive_build_sup_lvl full range : 
		test full computer numeric remap : 
		recursive level 2
		recursive level 3
		recursive level 4
		i-mini = 0 | Constructor base 11 done in 0.058423757553100586s. length = 161051 | last value = aaaaa
		recursive level 2
		recursive level 3
		recursive level 4
		i-mini = 1 | Constructor base 12 done in 0.07001042366027832s. length = 248832 | last value = bbbbb
		recursive level 2
		recursive level 3
		recursive level 4
		i-mini = 2 | Constructor base 13 done in 0.10061907768249512s. length = 371293 | last value = ccccc
		recursive level 2
		recursive level 3
		recursive level 4
		i-mini = 3 | Constructor base 14 done in 0.14471197128295898s. length = 537824 | last value = ddddd
		recursive level 2
		recursive level 3
		recursive level 4
		i-mini = 4 | Constructor base 15 done in 0.20563387870788574s. length = 759375 | last value = eeeee
		recursive level 2
		recursive level 3
		i-mini = 5 | Constructor base 16 done in 0.017303943634033203s. length = 65536 | last value = ffff
		recursive level 2
		recursive level 3
		i-mini = 6 | Constructor base 17 done in 0.02532958984375s. length = 83521 | last value = gggg
		recursive level 2
		recursive level 3
		i-mini = 7 | Constructor base 18 done in 0.029736042022705078s. length = 104976 | last value = hhhh
		recursive level 2
		recursive level 3
		i-mini = 8 | Constructor base 19 done in 0.036131858825683594s. length = 130321 | last value = iiii
		recursive level 2
		recursive level 3
		i-mini = 9 | Constructor base 20 done in 0.04368901252746582s. length = 160000 | last value = jjjj
		recursive level 2
		recursive level 3
		i-mini = 10 | Constructor base 21 done in 0.05226731300354004s. length = 194481 | last value = kkkk
		recursive level 2
		recursive level 3
		i-mini = 11 | Constructor base 22 done in 0.0626680850982666s. length = 234256 | last value = llll
		recursive level 2
		recursive level 3
		i-mini = 12 | Constructor base 23 done in 0.07324409484863281s. length = 279841 | last value = mmmm
		recursive level 2
		recursive level 3
		i-mini = 13 | Constructor base 24 done in 0.08711719512939453s. length = 331776 | last value = nnnn
		recursive level 2
		recursive level 3
		i-mini = 14 | Constructor base 25 done in 0.10201478004455566s. length = 390625 | last value = oooo
		recursive level 2
		recursive level 3
		i-mini = 15 | Constructor base 26 done in 0.11851167678833008s. length = 456976 | last value = pppp
		recursive level 2
		recursive level 3
		i-mini = 16 | Constructor base 27 done in 0.1371898651123047s. length = 531441 | last value = qqqq
		recursive level 2
		recursive level 3
		i-mini = 17 | Constructor base 28 done in 0.15837740898132324s. length = 614656 | last value = rrrr
		recursive level 2
		recursive level 3
		i-mini = 18 | Constructor base 29 done in 0.18125104904174805s. length = 707281 | last value = ssss
		recursive level 2
		recursive level 3
		i-mini = 19 | Constructor base 30 done in 0.20747065544128418s. length = 810000 | last value = tttt
		recursive level 2
		recursive level 3
		i-mini = 20 | Constructor base 31 done in 0.23558616638183594s. length = 923521 | last value = uuuu
		recursive level 2
		recursive level 3
		i-mini = 21 | Constructor base 32 done in 0.2667877674102783s. length = 1048576 | last value = vvvv
		recursive level 2
		recursive level 3
		i-mini = 22 | Constructor base 33 done in 0.28461384773254395s. length = 1185921 | last value = wwww
		recursive level 2
		recursive level 3
		i-mini = 23 | Constructor base 34 done in 0.31728363037109375s. length = 1336336 | last value = xxxx
		recursive level 2
		recursive level 3
		i-mini = 24 | Constructor base 35 done in 0.3570218086242676s. length = 1500625 | last value = yyyy
		Calulation time : 3.3737525939941406

		.. code-block:: python	

			print("test full tables recursive_build_sup_lvl full range : ")
			print("test full computer numeric remap : ")
			rec_level_h = [6,6,6,6,6,5,5,5,5,5,5,5,5,5,5,5,5,4,4,4,4,4,4,4,4,4]
			rec_level_m = [5,5,5,5,5,4,4,4,4,4,4,4,4,4,4,4,4,3,3,3,3,3,3,3,3,3]
			rec_level_l = [4,4,4,4,4,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]
			table = []
			bases = []
			tmp   = ()
			ok    = 0
			mini   =11
			# stop   = int(sys.argv[2])
			mytime = 0
			fini = 0
			finalt = 0
			initt  =time.time()
			for i in range (mini,36):
				mytime=time.time()
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
					# ok=tmp[1]
					ind+=1
					print("recursive level "+str(ind))
					if(ind==rec_level_l[i-mini]):
						ok=1
					# time.sleep(7)
					# if(ind==stop):
					# 	ok=1
				fini=time.time()-mytime
				print("i-mini = "+str(i-mini)+" | Constructor base "+str(i)+" done in "+str(fini)+"s. length = "+str(len(table[i-mini]))+" | last value = "+str(table[i-mini][-1]))
			finalt=time.time()-initt
			print("Calulation time : "+str(finalt))

			return table
	"""
	print("test full tables recursive_build_sup_lvl full range : ")
	print("test full computer numeric remap : ")
	rec_level_h = [6,6,6,6,6,5,5,5,5,5,5,5,5,5,5,5,5,4,4,4,4,4,4,4,4,4]
	rec_level_m = [5,5,5,5,5,4,4,4,4,4,4,4,4,4,4,4,4,3,3,3,3,3,3,3,3,3]
	rec_level_l = [4,4,4,4,4,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]
	table = []
	bases = []
	tmp   = ()
	ok    = 0
	mini   =11
	# stop   = int(sys.argv[2])
	mytime = 0
	fini = 0
	finalt = 0
	initt  =time.time()
	for i in range (mini,36):
		mytime=time.time()
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
			# ok=tmp[1]
			ind+=1
			print("recursive level "+str(ind))
			if(ind==rec_level_l[i-mini]):
				ok=1
			# time.sleep(7)
			# if(ind==stop):
			# 	ok=1
		fini=time.time()-mytime
		print("i-mini = "+str(i-mini)+" | Constructor base "+str(i)+" done in "+str(fini)+"s. length = "+str(len(table[i-mini]))+" | last value = "+str(table[i-mini][-1]))
	finalt=time.time()-initt
	print("Calulation time : "+str(finalt))

	return table