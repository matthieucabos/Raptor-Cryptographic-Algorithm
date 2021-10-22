slurp
=====

.. code-block:: python	

	def slurp(chaine)

_________________________________________________________________

**Algorithm**
-------------

This method allow us to rebuild a str list of crypted terms using separators set.

=============== ========== ==================================
**Parameters**   **Type**   **Description**
**chaine**       *str*       The raw string crypted message
=============== ========== ==================================

:Returns: **str list** : The list of crypted terms rebuilded from the raw string

_________________________________________________________________

**Source Code**
---------------
 
.. code-block:: python

	tmp=''
	res = []
	sep=['!','"','#','$','%','&','(',')','*','+',',','-','.','/']
	for elem in chaine:
		if(not elem in sep):
			tmp+=str(elem)
		else :
			res.append(tmp)
			tmp=''
		if(elem==''):
			break
	res=res[1:]
	res.append(tmp)
	return res