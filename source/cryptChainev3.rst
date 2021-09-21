cryptChaine
===========

.. code-block:: python	

	def cryptChaine(to_crypt,table,base)

_________________________________________________________________

**Algorithm**
-------------

The simple method to crypt an ascii string as integer list.

=============== =============== ==================================================
**Parameters**   **Type**        **Description**
**to_crypt**    *int list*      The converted int list since an ascii string
**table**       *list of list*  An array containing all fully builded Base Table
**base**        *int*           Define the Base index 
=============== =============== ==================================================

:Returns: **str list** : A string list containing all the base crypted values. Must be used as a crypted list.

_________________________________________________________________

**Source Code**
---------------
 
.. code-block:: python

	res = []
	for i in range(0,len(to_crypt)):
		res.append(table[base][to_crypt[i]])
	return res
