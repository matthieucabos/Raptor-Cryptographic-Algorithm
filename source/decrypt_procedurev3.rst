decrypt_procedure
=================

.. code-block:: python	

	def decrypt_procedure(chaine,key,table)

_________________________________________________________________

**Algorithm**
-------------

This method manage the decrypting procedure.
It is ruled by the following steps :

	* **Build the full key** since the key argument
	* **Split the string** since separators via slurp method
	* **Apply the inv_tranpose_base method** to get the uncrypted terms
	* **Solve the cumulated multiplied weigth** with the equation solver
	* **Convert the int list** as result to ASCII chain

=============== =============== =================================
**Parameters**   **Type**        **Description**
**chaine**      *str*             The raw crypted text as string
**key**         *int list*        The half key as int list
**table**       *list of list*    The Base Table array
=============== =============== =================================

:Returns: **str** : The uncrypted text.

_________________________________________________________________

**Source Code**
---------------
 
.. code-block:: python

	res = ''
	base=key[:]
	tmp = []
	key.reverse()
	tmp = key[:]
	to_find = []
	to_find=slurp(chaine)
	if(len(to_find)%2==0):
		base+=tmp[0:len(key)]
	else:
		base+=tmp[1:len(key)]
	# Complexify
	tmp_liste=inv_transpose_base(to_find,base,table)
	# print(tmp_liste)
	int_liste=resolve(tmp_liste)
	res = int_to_ascii(int_liste)
	return res
