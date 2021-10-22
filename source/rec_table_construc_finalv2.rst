rec_table_construct_final
=========================

.. code-block:: python

	def rec_table_construct_final(table,base,lvl)

_________________________________________________________________

**Algorithm**
-------------

Recursive Construction method from the Base table.
The recursive algorithm manage array building since 2 levels of recursive construction.
=> Do not use for the first recursive building loop

=============== ========== ===============================================
**Parameters**   **Type**   **Description**
**table**        *list*      The first recursive level builded Base table 
**base**         *int*       The base to treat as integer
**lvl**          *int*       The level of recursivity in construction
=============== ========== ===============================================

:Returns: **list** : The fully specified level recursivity builded Base table

_________________________________________________________________

**Source Code**
---------------

.. code-block:: python

	res=[]
	basetable=table[0:base]
	for i in range(0,len(basetable)):
		basetable[i]=basetable[i][lvl:]
	for eat in basetable:
		for this in table:
			res.append(eat+this)
	return res