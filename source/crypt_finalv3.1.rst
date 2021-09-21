crypt_final
===========

.. code-block:: python	

	def crypt_final(tuple,int_chaine,table)

_________________________________________________________________

**Algorithm**
-------------

The layout procedure to organise crypting results. The uodate consist to complement each of terms in his corresponding base.
It allow a superior level of crypting. I use the separators set as well.

=============== ========== ===================================================================
**Parameters**   **Type**   **Description**
**tuple**        *tuple*    List couple representing the crypted strin and the associated key
=============== ========== ===================================================================

:Returns: **str** : The crypted list as a string with correct separators

_________________________________________________________________

**Source Code**
---------------

.. code-block:: python

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