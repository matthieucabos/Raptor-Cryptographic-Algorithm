slurp3
======

.. code-block:: python	

	def slurp3(chaine)

_________________________________________________________________

**Algorithm**
-------------

This method is similar of the slurp2 method. It defined a third level of crypting management.

=============== ========== ==================================
**Parameters**   **Type**   **Description**
**chaine**      *str*       The raw string crypted message
=============== ========== ==================================

:Returns: **str list** : The list of crypted terms rebuilded from the raw string.

_________________________________________________________________

**Source Code**
---------------
 
.. code-block:: python

	tmp=''
	mesquin=['M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	for elem in chaine:
		if(not elem in mesquin):
			tmp+=str(elem)		
	return tmp
