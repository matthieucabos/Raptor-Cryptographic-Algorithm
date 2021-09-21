rec_manage
==========

.. code-block:: python	

	def rec_manage(table)

_________________________________________________________________

**Algorithm**
-------------

A recursivity manager to build properly the base table.
It must be used to map the numeric values into base values.
This method allow contruction of hundreds of thousand values table

=============== ========== ====================================
**Parameters**   **Type**   **Description**
**table**        *list*       The initial Base table to complete
=============== ========== ====================================

:Returns: **list** : The fully builded Base table

_________________________________________________________________

**Source Code**
---------------

.. code-block:: python

	for i in range(9,len(table)):
		# print("i = "+str(i))
		table2=table[i][:]
		table2=rec_table_construct_lvl1(table2,i+2,1,0)
		table2=rec_table_construct_final(table2,i+2,1)
		table2=rec_table_construct_final(table2,i+2,2)
		if(i<20):
			table2=rec_table_construct_final(table2,i+2,3)
		table[i]=table2[:]
	return table
