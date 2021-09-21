rec_table_construct_lvl1
========================

.. code-block:: python	

	def rec_table_construct_lvl1(table,base,powindex,last)

_________________________________________________________________

**Algorithm**
-------------

Recursive Construction method from the Base table.
The recursive algorithm permit to edit much larger array from existing original base table.
Ths algorithm must be used as the init loop of the final recursive method (see rec_manage method)

=============== ============ =====================================
**Parameters**     **Type**   **Description**
**table**       *list*        The Base table array
**base**        *int*         The current numeric base as integer
**powindex**    *int*         The pow index as integer
**last**        *int*         unused
=============== ============ =====================================

:Returns: **list** : The Recursively builded Base table as list

_________________________________________________________________

**Source Code**
---------------

.. code-block:: python

	lettrebase=table[10:base]
	if(powindex == 1):
		del table[10*base]
	res=table[:]
	for i in range (len(table)-1,base**2-1):
		if(i%base==(base-1) and i!=len(table)-1):
			powindex+=1
		res.append(lettrebase[powindex-1]+str(table[(i-len(table)+1)%base]))
		# print("i = "+str(i)+" | i%base = "+str(i%base)+" | ib"+str(base)+" = "+str(res[i]))
	return res
