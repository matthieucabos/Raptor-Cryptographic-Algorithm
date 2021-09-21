local_table_dico
================

.. code-block:: python

	def local_table_dico(table2,base,rangeB)

_________________________________________________________________

**Algorithm**
-------------

Utils method : A method to convert a Base table to Python dictionnary

=============== ============== ======================================================
**Parameters**   **Type**      **Description**
**table2**      *list of list*  An array containing all the fully builded Base table
**base**        *int*           Define the Base index
**rangeB**      *int*           Define the max step of incrementation
=============== ============== ======================================================

:Returns: **Dictionnary** : A dictionnary representing the specified Base table

_________________________________________________________________

**Source Code**
---------------

.. code-block:: python

	str_base={}
	res = {}
	if(rangeB>base**2):
		rangeB=base**2
	for i in range (0,rangeB):
		str_base[i]=table2[base][i]
	return str_base
