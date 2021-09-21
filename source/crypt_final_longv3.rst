crypt_final_long
================

.. code-block:: python	

	def crypt_final_long(liste,int_chaine)

_________________________________________________________________

**Algorithm**
-------------

Chaining the final-level algorithm to get complex crypto-procedure

=============== ========== =====================================================================
**Parameters**   **Type**   **Description**
**tuple**        *tuple*     List couple representing the crypted string and the associated key
=============== ========== =====================================================================

:Returns: **str** : The full second level crypted string 

_________________________________________________________________

**Source Code**
---------------
 
.. code-block:: python

	sept=['!','"','#','$','%','&','(',')','*','+',',','-','.','/']
	res = ''
	sep =sept[int(int_chaine[1]*m.cos(int_chaine[0]))%13] 
	for i in range (0,len(liste)):
		res+=sep+str(liste[i])
		sep=cyclik_ascii(sep)
	# print(res)
	return res
