crypt_procedure
===============

.. code-block:: python

	def crypt_procedure(chaine,table)

_________________________________________________________________

**Algorithm**
-------------

The crypter manager to orchestrate the crypting procedure.
It works from these steps:

	* *We convert the given ascii string as integer list*
	* *We compute the Base index list as key from the converted integer list*
	* *We build the second part of the key since the mirror of the Base index list*
	* *We compute the cumulated weight of the integer list*
	* *We compute the point by point multiplication between cumulated weigth list and original integer list*
	* *We transpose the multiplied list into the given specified Base from the key*
	* *We associate the crypted strin to the key as return*

=============== ================ ======================================
**Parameters**    **Type**        **Description**
**chaine**       *string*          The string to crypt
**table**        *list of list*    The Base Table recursively builded
=============== ================ ======================================

:Returns: **list tuple** : The couple crypted string and key as result. It permits to decrypt any message.

_________________________________________________________________

**Source Code**
---------------

.. code-block:: python

	int_chaine = ascii_to_int(chaine)
	base_keyy  = base_key(int_chaine)
	if(len(base_keyy)%2==0):
		key=base_keyy[0:int(len(base_keyy)/2)]
	else:
		key=base_keyy[0:int((len(base_keyy)/2)+1)]
	vec_poid   = vec_poids(int_chaine)
	crypt_lst  = multlist(int_chaine,vec_poid)
	crypt_lst  = transpose_base(crypt_lst,base_keyy,table)
	return(crypt_lst,key)
