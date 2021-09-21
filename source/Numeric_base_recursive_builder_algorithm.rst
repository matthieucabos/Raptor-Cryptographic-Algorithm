Numeric Base Recursive Builder Algorithm
========================================

**This is the Main Base Builder Recursive Generator Algorithm**

_________________________________________________________________

**Algorithm**
-------------

This is the main Base Table Builder Algorithm.
The algorithm is ruled by these following steps :

	* **Init time** : I init Time variable using the time library from Python
	* **First Step Base Table** : This is the first step of the builder, I build the basic table from the tablebase function
	* **First level of recursivity** : I build the first level of recursivity in safe mode using recursive_build function
	* **Full Recursive algorithm** : We get the full computation of the table via the recursive_build_sup_lvl method.
	* **Time calculation** : Computation of necessary time for the construction of the full array


:Returns: **list of list** : A list of list containing all the string values representing the full generateed Base Table array

_________________________________________________________________

**Source Code**
---------------

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
