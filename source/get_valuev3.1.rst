get_value
=========

.. code-block:: python	

	def get_value(x,table,base)

_________________________________________________________________

**Algorithm**
-------------

A value getter to obtain an index from the original Base converted string value.
This method is working as the list 'index' method and allow us to get the raw full integer corresponding to the list of list value.

=============== ============== =======================
**Parameters**  **Type**        **Description**
**x**           *str*           The value to search
**table**       *list of list*  The full Base Table 
**base**        *int*           The index of the base
=============== ============== =======================

:Returns: **int** : The real decimal value of the specified term in his own Base.

_________________________________________________________________

**Source Code**
---------------

.. code-block:: python	

	ind=0
	while(table[base][ind]!=x):
		ind+=1
	return ind